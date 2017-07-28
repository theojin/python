from distutils.core import setup

setup(
    name = 'module_name',
    version = '1.0.0',
    py_modules = ['module_names'],
    author = 'Jin Yoon',
    author_email = 'theojini@gmail.com',
    url = 'http://storycompiler.com',
    description = 'Test',
    )

#python3 setup.py sdist #make a package for distribution
#python3 setup.py install
#python3 setup.py register #login in pypi
#python3 setup.py sdist upload
