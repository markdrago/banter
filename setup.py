from setuptools import setup

setup(
    name='banter',
    version='0.1.2',
    author='Mark Drago',
    author_email='markdrago@gmail.com',
    url='http://github.com/markdrago/banter',
    download_url='http://pypi.python.org/pypi/banter',
    description='Create crucible code reviews from the command line',
    license='MIT',
    packages=['banter'],
    entry_points={
        'console_scripts': [
            'banter = banter.banter:main'
        ]
    },
    install_requires=['requests>=1.0', 'argparse'],
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
**Banter makes it easy to create code reviews from the command line.**

Currently it only supports the crucible code review tool created by
Atlassian.
"""
)
