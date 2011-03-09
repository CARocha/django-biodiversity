#!/home/simasnio/bin/python
from django.core.management import execute_manager
import sys

sys.path.insert(0, "/home/simasnio/projects/")
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\n$
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
