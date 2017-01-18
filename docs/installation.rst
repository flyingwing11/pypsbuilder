============
Installation
============

At the command line::

    $ easy_install pypsbuilder

If you use virtual env with virtualenvwrapper installed::

    $ mkvirtualenv pypsbuilder
    $ pip install pypsbuilder

For Anaconda distribution (for now only Linux64 supported) you can install from personal channel::

    $ conda install -c https://conda.anaconda.org/ondrolexa pypsbuilder

For Anaconda distribution on Windows you can install all dependencies from official channel::

    $ conda install numpy matplotlib networkx pyqt

and install pypsbuilder directly from github using pip::

    $ pip install https://github.com/ondrolexa/pypsbuilder/archive/master.zip

To upgrade to laste version use::

    $ pip install --upgrade --upgrade-strategy only-if-needed  https://github.com/ondrolexa/pypsbuilder/archive/master.zip