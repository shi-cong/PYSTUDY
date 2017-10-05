"""
自动生成API
"""
from shicong.oslib import system, walk, isfile, isdir, split_ext, curdir, getcwd, mv, join
import shicong
from shicong.stringlib import endswith, join as j2

p = shicong.__path__[0]

o = getcwd()
print(p, o)

for parent,dirnames,filenames in walk(p):
    if '__py' in parent:
        continue
    prefix = 'shicong'
    print(prefix)

    count = 0
    for f in filenames:
        if count == 0:
            system('pydoc3 -w %s' % prefix)

        if endswith(f, '.py'):
            tmp = j2([prefix, split_ext(f)[0]], '.')
            print(tmp)
            system('pydoc3 -w %s' % tmp)
        system('mv *.html  ../docs/')

        count += 1
    count = 0

