from setuptools import setup

setup(
    name='dejavu',
    version='0.1',
    author='Mark Drago',
    author_email='markdrago@gmail.com',
    url='http://github.com/markdrago/dejavu',
    download_url='http://pypi.python.org/pypi/dejavu',
    description='Create crucible code reviews from the command line',
    license='MIT',
    packages=['dejavu'],
    entry_points={
        'console_scripts': [
            'dejavu = dejavu.dejavu:main'
        ]
    },
    install_requires=['requests', 'argparse'],
    tests_require=['unittest2', 'mock'],
    test_suite='unittest2.collector',
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities'
    ],
    long_description="""
**Dejavu makes it easy to create code reviews from the command line.**

Currently it only supports the crucible code review tool created by
Atlassian.
"""
)
