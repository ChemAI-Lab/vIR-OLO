'''Allows the app to be launched with `python -m virolo`.'''

import sys

from .cli import main

if __name__ == "__main__":
    sys.exit(main())
