import os
import sys

print(sys.argv)
if sys.argv[0].startswith('test'):
    sys.path.insert(0, os.getcwd())
else:
    path = os.getcwd().rsplit('/', 1)[0]
    print(path)
    sys.path.insert(0, path)
    import PYSTUDY
