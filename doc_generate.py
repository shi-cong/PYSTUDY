from sclib.oslib import system, walk, isfile, isdir, split_ext, curdir, getcwd, mv, join
import sclib
from sclib.stringlib import endswith, join as j2

p = sclib.__path__[0]

o = getcwd()
print(p, o)

for parent,dirnames,filenames in walk(p):
    if '__py' in parent:
        continue
    prefix = 'sclib' + j2(parent.split('sclib')[1].split('/'), '.')
    print(prefix)

    count = 0
    for f in filenames:
        if count == 0:
            system('pydoc3 -w %s' % prefix)
            # mv(join([o, prefix]), join([o, 'doc']))
        if endswith(f, '.py'):
            tmp = j2([prefix, split_ext(f)[0]], '.')
            print(tmp)
            system('pydoc3 -w %s' % tmp)
            # mv(join([o, tmp]), join([o, 'doc']))

        count += 1
    count = 0

