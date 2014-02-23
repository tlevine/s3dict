from distutils.core import setup

setup(name='s3dict',
    author='Thomas Levine',
    author_email='_@thomaslevine.com',
    description='Use S3 like a dictionary',
    url='https://github.com/tlevine/s3dict.git',
    classifiers=[
        'Intended Audience :: Developers',
    ],
    packages=['s3dict'],

    install_requires = ['boto'],
    tests_require = ['nose'],

    version='0.0.1',
    license='AGPL'
)
