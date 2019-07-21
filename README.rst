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

We apply hideout with :code:`with` clause. When we use 'want-to-load-object', we use `hideout.resume`
from cache. The `hideout.resume` returns `Keeper` object which load the object from cache if the file exists,
if not `Keeper.succeeded_to_load` returns `False`.

When `Keeper.succeeded_to_load` returns `False`, we generate the object and set the object with `Keeper.set` method.
`hideout` automatically saves the object into the cache file leaving `with` clause, and therefore the `hideout.resume` loads the
object from the cache file. This leads the program to get the generated objct with minimum cost.

The followiing is the sample of code with `hideout.resume`.

::

    with hideout.resume(file_prefix="want-to-load-object") as keeper:
        if not keeper.succeeded_to_load():
            keeper.set(generate_object())
        want_to_load_objct = keeper.get()

The above code try to load cache file with `want-to-load-object` prefix. When the load succeeded, the object is set with `get` method.
Otherwise the code generate the object with `generate_object` function and set the object to the `hideout.Keeper` object. The set object is
automattically saved the program leaves the `with` clause.

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
