import argparse
import inspect
from argparse import Namespace


def init_arguments() -> Namespace:
    """
    Parses arguments from execution using argparse library

    Return values:

    Namespace: object of type Namespace from argparse library within we can access attributes
                which represents arguments
    """
    parser = argparse.ArgumentParser(
        description=inspect.cleandoc(
            """
            Example console application for logging notifications from postgresql database.
            Before usage of this script, please make sure you edit properly settings.ini.
            """
        )
    )

    parser.add_argument(
        '-f',
        '--file',
        help='Loads specific config file. By default: settings.ini',
        default='settings.ini',
        metavar='PATH'
    )

    parser.add_argument(
        '-t',
        '--table',
        help='Specifies the name of table.',
        type=str,
        required=False
    )

    parser.add_argument(
        '--create',
        help='Create a table in database.',
        action='store_true'
    )

    parser.add_argument(
        '--insert',
        help='Insert a new row into `items` table in database.',
        action='store_true'
    )

    return parser.parse_args()
