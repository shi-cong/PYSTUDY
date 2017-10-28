import os
import sys

print(sys.argv)
if sys.argv[0].startswith('test'):
    sys.path.insert(0, os.getcwd())
else:
    sys.path.insert(0, '../')
