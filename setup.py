import os
import re
import sys
from PYSTUDY.oslib import listdir, split_ext

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system("python3 setup.py sdist upload")
    os.system('twine upload dist/*')
    os.system('rm -rf dist')
    os.system('rm -rf PYSTUDY.egg-info')
    sys.exit()

if sys.argv[-1] == 'test':
    for f in listdir('test'):
        if '.py' == split_ext(f)[1] and '__' not in f:
            error = os.system('python3 test/%s' % f)
            if error != 0:
                sys.exit(error)
    sys.exit(0)

packages = [
    'PYSTUDY',
    'PYSTUDY.api',
    'PYSTUDY.image',
    'PYSTUDY.middleware',
    'PYSTUDY.ml',
    'PYSTUDY.net',
    'PYSTUDY.office',
]

install = [
    'bcrypt', # 
    'scrapy', # 该框架，我仅仅用了对html解析对模块
    'xlwt', 
    'pymongo',
    'pymysql',
    'numpy', # 线性代数计算库, 常用概率统计
    'pypdf2', 
    'reportlab',
    'pytesseract', # 可识别简单的验证码
    'pillow',
    'pika', # amqp操作库
    'requests', # http模拟库
    'tensorflow', # google深度学习库
    'tornado', # python异步非柱塞http库
    'pyyaml', # yaml文件解析库
    'selenium', # 自动化浏览器测试库
    'imghdr',  # 获取图片的真实类型
    'cv2'
]


with open('PYSTUDY/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

setup(
    name='PYSTUDY',
    version=version,
    description='learning python',
    author='shi-cong',
    author_email='shi_cong@icloud.com',
    url='https://github.com/shi-cong/PYSTUDY',
    packages=packages,
    license='Apache License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    tests_require=['pytest'],
    install_requires=install,
)
