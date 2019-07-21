.. image:: https://travis-ci.org/takahi-i/hideout.svg?branch=master
    :alt: Build status
    :target: https://travis-ci.org/takahi-i/hideout


=====================================================
hideout 
=====================================================

Data processing programs such as machine learning takes sorts of input data. After input data are loaded, program creates intermediate objects using input data.
Getting or converting data takes large amount of the time. This problem prevents programmers to refactor data processing programs.


Install
--------

We can install hideout with pip. Run the following command.

::

    $ pip install hideout


Usage
------

We apply hideout with :code:`with` clause. When

::

    with hideout.resume(file_prefix="want-to-load-object") as want_to_load_object:
        if not want_to_load_object.succeeded_to_load():
            want_to_load_object.set(self.__generate_object())
        return want_to_load_object.get()

For Developers
---------------


Install to local environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   $ python setup.py install

Upload to pypi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ python setup.py sdist upload
