import args  # args.py
import database as db  # database.py
from configparser import ConfigParser


def cfg_load(filename: str, section: str = 'postgresql') -> dict:
    """
    Loads a configuration file important to get database parameters.

    Key parameters:
        filename (str): config file name
        section (str): name of section in the config file

    Return values:
        dict: content of config file parameters as dictionary
    """
    parser = ConfigParser()
    if not parser.read(filename):
        raise Exception(f'Configuration file {filename} not found.')
    if parser.has_section(section):
        # converts list of tuples to dictionary
        return dict(parser.items(section))
    else:
        raise Exception(f'Configuration file {filename} has no section ')


def main() -> None:
    # load arguments
    arguments = args.init_arguments()
    # load config file into params
    params = cfg_load(arguments.file)

    table_name = arguments.table if arguments.table else 'items'

    if arguments.create:
        db.db_create_tables(table_name, params)
    elif arguments.insert:
        db.db_insert_row(table_name, params)
    else:
        db.db_listen('item_change', params)


if __name__ == '__main__':
    main()
