# pyeccodes

This is an experiment of a pure Python GRIB decoder based on eccodes https://github.com/ecmwf/eccodes. The code is automatically generated from the definition files and tables.

The package does not support encoding. 

The difference with other Python bindings are:

* All arrays and lists are returns as numpy arrays
* Missing data values are set to numpy.NaN
* Asking for a missing key is not an error. The value None is returned
* If a key returns a missing value  (e.g. 255), None is returned instead

You can use pyeccodes with cfgrib with a version greater or equal to 0.9.8.1.