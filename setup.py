from setuptools import setup

setup(
    name='dejaview',
    version='0.1',
    author='Mark Drago',
    author_email='markdrago@gmail.com',
    url='http://github.com/markdrago/dejaview',
    download_url='http://pypi.python.org/pypi/dejaview',
    description='Create crucible code reviews from the command line',
    license='MIT',
    packages=['dejaview'],
    entry_points={
        'console_scripts': [
            'dejaview = dejaview.dejaview:main'
        ]
    },
    install_requires=['requests', 'argparse'],
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
**DejaView makes it easy to create code reviews from the command line.**

Currently it only supports the crucible code review tool created by
Atlassian.
"""
)
