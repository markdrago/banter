##Dejavu

Dejavu creates code reviews on crucible from the command line.

You can run whatever tool you like which produces a diff and pipe that in to
dejavu to submit that diff for review on crucible.

###Getting Dejavu
Dejavu is available in the Python Package Index, so you can install it with
either easy_install or pip.  Here's
[Dejavu's page on PyPI](http://pypi.python.org/pypi/dejavu).

- sudo pip install dejavu **or** sudo easy_install dejavu
    - You can get pip on ubuntu/debian by running: sudo apt-get install python-pip

###Setup
Before using dejavu you'll need to let it know where your installation of
crucible lives, what your username is, etc.  You can run:

    $ dejavu --setup

to start the setup tool which will ask you a few questions.  It will ask you to
enter your crucible password, but it will not store it.  Instead it uses your
password to request an auth token from crucible and uses that auth token for
the rest of its interactions with crucible.  Dejavu will write its
configuration file to $HOME/.config/dejavu/dejavu.conf.

###Creating Reviews
Provided you have completed the setup you can use dejavu by doing the following:

    $ git diff | dejavu
    http://crucible.dev.company.com/fisheye/cru/CR-15

Dejavu will create a review from the patch provided to it and print out the URL
for the new crucible review.  You can access that URL to make any modifications
that you need to make and then start the review.