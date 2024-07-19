.. _ISCAN server: https://github.com/MontrealCorpusTools/ISCAN

.. _installation:

.. _Conda Installation: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

***************
Getting started
***************

PolyglotDB is the Python API for interacting with Polyglot databases and is installed through ``pip``. There are other
dependencies that must be installed prior to using a Polyglot database, depending on the user's platform.

.. note::

   Another way to use Polyglot functionality is through setting up an `ISCAN server`_.
   An Integrated Speech Corpus Analysis (ISCAN) server can be set up on a lab's central server, or you can run it on your
   local computer as well (though many
   of PolyglotDB's algorithms benefit from having more processors and memory available).  Please see the ISCAN
   documentation for more information on setting it up (http://iscan.readthedocs.io/en/latest/getting_started.html).
   The main feature benefits of ISCAN are multiple Polyglot databases (separating out different corpora and allowing any
   of them to be started or shutdown), graphical interfaces for inspecting data, and a user authentication system with different levels
   of permission for remote access through a web application.

.. _actual_install:

Installation
============

It is recommended to create a conda environment for using PolyglotDB. While it is supported to use it without a conda environment, this may result in unexpected behavior.
If you don't have conda installed on your device: 
#. Install either Anaconda, miniconda, or miniforge (`Conda Installation`_)
#. Make sure your conda is up to date :code:`conda update conda`

To install via pip:

#. Create the a conda environment via :code:`conda create -n polyglotdb -c conda-forge openjdk=21 python=3.12`
#. Activate conda environment :code:`conda activate polyglotdb`
#. :code:`pip install polyglotdb`

To install from source (primarily for development):

#. Clone or download the Git repository (https://github.com/MontrealCorpusTools/PolyglotDB).
#. Navigate to the directory via command line and create the conda environment via :code:`conda env create -f environment.yml`
#. Install PolyglotDB via :code:`pip install -e .`, which will install the ``pgdb`` utility that can be run inside your conda environment
   and manages a local database.

.. _local_setup:

Set up local database
---------------------

Installing the PolyglotDB package also installs a utility script (``pgdb``) that is then callable from the command line inside your conda environment. 
The ``pgdb`` command allows for the administration of a single Polyglot database (install/start/stop/uninstall).
Using ``pgdb`` requires that several prerequisites be installed first, and the remainder of this section will detail how
to install these on various platforms.
Please be aware that using the ``pgdb`` utility to set up a database is not recommended for larger groups or those needing
remote access.
See the `ISCAN server`_ for a more fully featured solution.

Mac & Linux
```

#. Check Java version is >= 17 via ``java --version``
#. Once PolyglotDB is installed, run :code:`pgdb install /path/to/where/you/want/data/to/be/stored`, or
   :code:`pgdb install` to save data in the default directory.

.. warning::

   Do not use ``sudo`` with this command on Macs, as it will lead to permissions issues later on.

Once you have installed PolyglotDB, to start it run :code:`pgdb start`.
Likewise, you can close PolyglotDB by running :code:`pgdb stop`.

To uninstall, run :code:`pgdb uninstall`

Windows
```````

#. Check Java version is >= 17 via ``java --version``
#. Make sure you are running as an Administrator command prompt (right-click on cmd.exe and select "Run as administrator"), as Neo4j will be installed as a Windows service. You might need to open a new command prompt for this step.
#. Inside your conda environment, run :code:`pgdb install /path/to/where/you/want/data/to/be/stored`, or
   :code:`pgdb install` to save data in the default directory.

To start the database, you likewise have to use an administrator command prompt before entering the commands :code:`pgdb start`
or :code:`pgdb stop`.

To uninstall, run :code:`pgdb uninstall` (also requires an administrator command prompt).


To view your conda environments:

.. code-block:: bash

    conda info -e

To return to your root environment:

.. code-block:: bash

    conda deactivate
