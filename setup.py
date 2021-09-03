#!/usr/bin/python
# -*- coding: utf-8 -*-
__version__ = "1.1.4.0"

import atexit
from os.path import join, dirname
from traceback import format_exc

from setuptools import setup, find_packages
from setuptools.command.install import install


class CustomInstall(install):
    def run(self):

        print ("HELLO!")


        packages=find_packages()

        def _post_install():
            import os.path, re

            print ("POST INSTALL STEPS")

            def find_modules_path():
                import sys

                return ['/usr/local/lib/python%s.%s/dist-packages/%s'%(sys.version_info[0],sys.version_info[1],packages[0])]

                xp=[]
                for p in sys.path:
                    if re.search('/python[0-9.]+/',p):
                        for my_name in packages:
                            if os.path.isdir(p) and my_name in os.listdir(p):
                                xp.append(os.path.join(p, my_name))

                return xp
            install_paths = find_modules_path()
            print ("INSTALL PATHS:%s"%install_paths)

            pyc_files = []
            py_files = []

            bsf='#/bin/bash\n'
            for ip in install_paths:
                for root, dirnames, filenames in os.walk(ip):
                    for filename in filenames:
                        if filename.endswith('.pyc'):
                            pyc_files.append(os.path.join(root, filename))
                        elif filename.endswith('.py'):
                            py_files.append(os.path.join(root, filename))
                for py_file in py_files:
                    if py_file + 'c' in pyc_files:
                        if not re.search('/kiosk_',py_file):
                            try:
                                bsf+='rm -f %s\n'%py_file
                                os.remove(py_file)
                            except:
                                pass
            print ("BYE!")
        atexit.register(_post_install)
        install.run(self)
setup(
    cmdclass={'install': CustomInstall},
    name='bot',
    version=__version__,
    description='Part project',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author='k.e.p',
    author_email='kravec.egor@gmail.com',
    license='BSD',
    install_requires=open(join(dirname(__file__), 'requirements.txt')).read(),
    packages=find_packages(),
    data_files=[('bot', ['bot/chromedriver.exe'])],
    include_package_data=True,
    zip_safe=False,
    keywords='bot',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]

)

