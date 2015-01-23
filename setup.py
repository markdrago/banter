from setuptools import setup

setup(
    name='banter',
    version='0.2.1',
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
    install_requires=['requests>=2.5.1'],
    tests_require=['mock'],
    test_suite='test',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
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
