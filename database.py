import psycopg2  # for postgresql
import inspect  # for cleandoc
import pgpubsub
import datetime
import logging


def check_table_name(table_name: str) -> None:
    """
    Validation function for table name. If not specified, raises exception.

    Parameters:

    table_name(str): name of the target table

    """
    if not table_name:
        raise Exception("Table name is not specified")


def db_query(sql: str, params: dict) -> None:
    """
    Simple function for processing query onto a database.

    Parameters:

    sql (str): sql query string

    """
    conn = None
    try:
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def db_listen(channel: str, params: dict) -> None:
    """

    Function using pgpubsub for subcribing the notification channel on postgresql database

    """
    # creates a log file
    logging.basicConfig(
        filename=f'{datetime.date.today()}_LOG.log', level=logging.INFO, format='%(message)s')

    # connects to db
    pubsub = pgpubsub.connect(
        user=params['user'], database=params['database'])

    # subscribe to notification channel
    pubsub.listen(channel)
    
    print('Listening...')
    for e in pubsub.events():
        logging.info(
            f'{datetime.datetime.utcnow().isoformat()} {e.payload}')
    pubsub.unlisten(channel)


def db_init_triggers(params: dict, table_name: str) -> None:
    """

    Function that creates a notification function with trigger after insertion or updating an entry.
    This allows us to read payload as a json structure.

    """
    sql_timestamp_trigger: str = inspect.cleandoc(f"""
        CREATE OR REPLACE FUNCTION items_update_timestamp()
        RETURNS trigger as $$
        BEGIN
            NEW.updated_at = now();
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;

        CREATE TRIGGER items_update_timestamp_trigger BEFORE UPDATE on {table_name}
            FOR EACH ROW EXECUTE PROCEDURE items_update_timestamp();
    """)
    sql_notify_trigger: str = inspect.cleandoc(f"""
        CREATE OR REPLACE FUNCTION items_notify_func()
        RETURNS trigger as $$
        BEGIN
	        PERFORM pg_notify('item_change', row_to_json(NEW)::text);
	        RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;

        CREATE TRIGGER items_notify_trigger AFTER UPDATE on {table_name}
	        FOR EACH ROW EXECUTE PROCEDURE items_notify_func();
    """)
    db_query(sql_timestamp_trigger, params)
    db_query(sql_notify_trigger, params)


def db_insert_row(table_name: str, params: dict) -> None:
    """
    Insertion function for inserting new entries into the database

    Parameters:

    table_name (str): name of the target table

    """

    check_table_name(table_name)

    sql_insert: str = inspect.cleandoc(f'''
        INSERT INTO {table_name}(status, updated_at) VALUES ('OFFLINE', CURRENT_TIMESTAMP);
    ''')
    db_query(sql_insert, params)


def db_create_tables(table_name: str, params: dict) -> None:
    """
    Initializes defined tables based on parameters. This function is a main logicical layer for
    database operations.

    Parameters:

    params (dict): parameters dictionary passed from main function
    table_name (str): name of the target table

    """

    check_table_name(table_name)

    sql_create: str = inspect.cleandoc(f'''
        CREATE TABLE {table_name} (
            id BIGSERIAL PRIMARY KEY,
            status VARCHAR(32) NOT NULL,
            updated_at TIMESTAMPTZ DEFAULT NULL
        );
    ''')

    db_query(sql_create, params)
    db_init_triggers(params, table_name)
