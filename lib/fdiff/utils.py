#!/usr/bin/env python3

import os

from datetime import datetime, timezone


def path_exists(path, include_dir_paths=False):
    """Validates existing paths.  The include_dir_paths parameter
    toggles acceptance of dir paths in addition to file paths."""
    if include_dir_paths:
        return os.path.exists(path)
    else:
        return os.path.isfile(path)


def get_file_modtime(path):
    """Returns ISO formatted file modification time in local system timezone"""
    return (
        datetime.fromtimestamp(os.stat(path).st_mtime, timezone.utc)
        .astimezone()
        .isoformat()
    )


def get_tables_argument_list(table_string):
    """Converts a comma separated OpenType table string into a Python list or return None if
    the table_string was not defined (i.e., it was not included in an option on the command line).
    Tables that are composed of three characters must be right padded with a space."""
    if table_string is None:
        return None
    else:
        return [
            table + " " if len(table) == 3 else table
            for table in table_string.split(",")
        ]
