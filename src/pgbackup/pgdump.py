#
#   pg_dump interface
#

import subprocess
import sys


def dump(url):
    """
    Attempts to use pg_dump utility on database.
    """
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)


def dump_file_name(url, timestamp=None):
    """
    Creates backup filename, with the option of including
    a timestamp.
    """
    db_name = url.split('/')[-1]
    db_name = db_name.split('?')[0]
    if timestamp:
        return f"{db_name}-{timestamp}.sql"
    else:
        return f"{db_name}.sql"