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

::

        large_object = hideout.resume(
            label="large_object",
            func=generate_large_object,
            func_args={"source": "s3-northeast-8.amazonaws.com/large-dic.txt"}
        )
        
Enable / Disable Cache
~~~~~~~~~~~~~~~~~~~~~~~


Directory to Store Cache Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


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
