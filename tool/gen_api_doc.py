"""
自动生成API
"""
from shicong.oslib import system, walk, isfile, isdir, split_ext, curdir, getcwd, mv, join
import shicong
from shicong.stringlib import endswith, join as j2, rsplit, count

p = shicong.__path__[0]

o = getcwd()
print(p, o)

for parent,dirnames,filenames in walk(p):
    if '__py' in parent:
        continue
    prefix = 'shicong'
    count1 = 0
    for f in filenames:
        print(parent)

        if count1 == 0:
            # 如果是第一个文件
            if endswith(parent, 'shicong'):
                system('pydoc3 -w %s' % prefix)
            else:
                tmp = rsplit(parent, 'shicong/', 1)[1]
                system('pydoc3 -w %s' % j2([prefix, tmp], '.'))
        else:
            if endswith(f, '.py'):
                # 如果是python文件
                tmp1 = None
                if count(parent, 'shicong/') == 2:
                    tmp1 = rsplit(parent, 'shicong/', 1)[1]
                tmp = j2([prefix, split_ext(f)[0]], '.')
                if tmp1:
                    tmp = j2([prefix, tmp1, split_ext(f)[0]], '.')

                system('pydoc3 -w %s' % tmp)
            else:
                tmp = rsplit(parent, 'shicong/', 1)[1]
                system('pydoc3 -w %s' % j2([prefix, tmp, split_ext(f)[0]], '.'))

        # system('mv *.html  ../doc/')

        count1 += 1
    count = 0
