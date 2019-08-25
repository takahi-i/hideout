.. image:: https://travis-ci.org/takahi-i/hideout.svg?branch=master
    :alt: Build status
    :target: https://travis-ci.org/takahi-i/hideout

.. image:: https://img.shields.io/badge/python-3.5-blue.svg
    :alt: Supported Python version
    :target: https://www.python.org/downloads/release/python-350/


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

        large_object = hideout.resume_or_generate(
            label="large_object",
            func=generate_large_object,
            func_args={"source": "s3-northeast-8.amazonaws.com/large-dic.txt"}
        )


:code:`hideout.resume` have :code:`func_args` option which contains the parameters of specified function to generate the expected object.
We can specify the prefix of cache file with `label` option. When we do not specify the :code:`label` option, :code:`resume_or_generate` method automatically
name the cache file from function name and the arguments.

Enable / Disable Cache
~~~~~~~~~~~~~~~~~~~~~~~

In default, Hideout is not activated and therefore does not save and load cache files. To enable cache we set the provided environment variable
:code:`HIDOUT_ENABLE_CACHE` to :code:`True`.

::

    $ HIDEOUT_ENBALE_CACHE=True your_data_engineering_program.py


Disable Cache for Specified Stages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


::

    $ HIDEOUT_SKIP_STAGES=preliminaries,integrate your_data_engineering_program.py

Directory to Store Cache Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In default, Hideout saves the cache files in :code:`caches` under the top project directory. If we specify the directory, we specify it with environment variable
:code:`HIDEOUT_BASE_DIR`.


Inject logger
~~~~~~~~~~~~~~

When you want to apply the logger which you use throughout an application, you can inject the logger with
:code:`hideout.set_logger()` function.

For Developers
---------------

We can install the hideout package and upload it to pypi repository.

Install to local environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   $ python setup.py install

Upload to pypi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ python setup.py sdist upload
