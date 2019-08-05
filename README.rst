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


Basic Usage 
~~~~~~~~~~~~

Hideout save and load object with `hideout.resume`. If the cache file for the object exist, hideout
loads it otherwise call specified function to generate expected object.

::

        large_object = hideout.resume(
            label="large_object",
            func=generate_large_object,
            func_args={"source": "s3-northeast-8.amazonaws.com/large-dic.txt"}
        )


`hideout.resume` have `func_args` option which contains the parameters of specified function to generate the expected object.

Enable / Disable Cache
~~~~~~~~~~~~~~~~~~~~~~~

In default, Hideout is not activated and therefore does not save and load cache files. To enable cache we set the provided environment variable
`HIDOUT_ENABLE_CACHE` to `True`.

::

    $ HIDEOUT_ENBALE_CACHE=True your_data_engineering_program.py


Disable Cache for Specified Stages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TBD

Directory to Store Cache Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In default, Hideout saves the cache files in `caches` under the top project directory. If we specify the directory, we specify it with environment variable
`HIDEOUT_BASE_DIR`.

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
