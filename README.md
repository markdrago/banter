##Banter

Banter creates code reviews on crucible from the command line.

You can run whatever tool you like which produces a diff and pipe that in to
banter to submit that diff for review on crucible.

###Getting Banter
Banter is available in the Python Package Index, so you can install it with
either easy_install or pip.  Here's
[Banter's page on PyPI](http://pypi.python.org/pypi/banter).

- sudo pip install banter **or** sudo easy_install banter
    - You can get pip on ubuntu/debian by running: sudo apt-get install python-pip

###Setup
Before using banter you'll need to let it know where your installation of
crucible lives, what your username is, etc.  You can run:

    $ banter --setup

to start the setup tool which will ask you a few questions.  It will ask you to
enter your crucible password, but it will not store it.  Instead it uses your
password to request an auth token from crucible and uses that auth token for
the rest of its interactions with crucible.  Banter will write its
configuration file to $HOME/.config/banter/banter.conf.

###Creating Reviews
Provided you have completed the setup you can use banter by doing the following:

    $ git diff | banter
    http://crucible.dev.company.com/fisheye/cru/CR-15

Banter will create a review from the patch provided to it and print out the URL
for the new crucible review.  You can access that URL to make any modifications
that you need to make and then start the review.