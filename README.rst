=====================================================
hideout 
=====================================================


Install
--------


`pip install hideout`


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

$ python setup.py install

Upload to pypi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

$ python setup.py sdist upload
