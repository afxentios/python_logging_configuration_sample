Sample for the config-logger and python logging configuration setup
===================================================================


Description
-----------

This repository contains an example of logging configuration which is required to be passed to the python module
`config-logger`_, in order to configure your logging for a python project. The logging configuration exists in the three
differentT formats that `config-logger`_  supports - YAML, JSON, Dictionary. The contents of this dictionary are
described in `Configuration dictionary schema`_.

In addition, the dictionary example - `logging.py`_ - can be also used as an example for the configuration of the
standard python module logging and passed to its method `dictConfig()`_.

License
-------

This project is licensed under the MIT license.

.. _config-logger: https://github.com/afxentios/config-logger
.. _Configuration dictionary schema: https://docs.python.org/2.7/library/logging.config.html#logging-config-dictschema
.. _logging.py: https://github.com/afxentios/python_logging_configuration_sample/blob/master/logging.py
.. _dictConfig(): https://docs.python.org/2.7/library/logging.config.html#logging.config.dictConfig