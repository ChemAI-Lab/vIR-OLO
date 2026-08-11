'''Development launcher.

Equivalent to the installed `virolo` console script, but runnable straight from
a checkout (no install required) by putting `src/` on the import path first.
'''

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from virolo.cli import main

if __name__ == "__main__":
    sys.exit(main())
