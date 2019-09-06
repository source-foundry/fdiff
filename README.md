<img src="https://raw.githubusercontent.com/source-foundry/fdiff/img/img/fdiff_logo-crunch.png" width="250" />
<br/>

## An OpenType table diff tool for fonts

[![GitHub license](https://img.shields.io/github/license/source-foundry/fdiff?color=blue)](https://github.com/source-foundry/fdiff/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/source-foundry/fdiff.svg?branch=master)](https://travis-ci.org/source-foundry/fdiff)
[![Build status](https://ci.appveyor.com/api/projects/status/eafvbkc4iyv78dip/branch/master?svg=true)](https://ci.appveyor.com/project/chrissimpkins/fdiff/branch/master)
[![codecov](https://codecov.io/gh/source-foundry/fdiff/branch/master/graph/badge.svg)](https://codecov.io/gh/source-foundry/fdiff)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b58954eda44b4fd88ad8f4fa06e8010b)](https://www.codacy.com/app/SourceFoundry/fdiff)


## About

`fdiff` is a Python command line comparison tool that demonstrates differences in the OpenType table data between font files.  The tool provides cross-platform support on macOS, Windows, and Linux systems with a Python v3.6+ interpreter.

## What it does

- Takes two font file path arguments for comparison
- Dumps OpenType table data in the fontTools library TTX format (XML)
- Compares the OpenType table data across the two files using the Python standard library unified diff format
- Supports optional color coding of the diff lines in the terminal

## Installation

`fdiff` requires a Python 3.6+ interpreter.

Installation in a [Python3 virtual environment](https://docs.python.org/3/library/venv.html) is recommended as dependencies are pinned to versions that are confirmed to work with this project.

Use any of the following installation approaches:

### pip install from PyPI

```
$ pip3 install fdiff
```

### pip install from source

```
$ git clone https://github.com/source-foundry/fdiff.git
$ cd fdiff
$ pip3 install .
```

### Developer install from source

The following approach installs the project and associated optional developer dependencies so that source changes are available without the need for re-installation.

```
$ git clone https://github.com/source-foundry/fdiff.git
$ cd fdiff
$ pip3 install --ignore-installed -r requirements.txt -e ".[dev]"
```

## Usage

```
$ fdiff [OPTIONS] [PRE-FONT FILE PATH] [POST-FONT FILE PATH]
```

By default, an uncolored unified diff is performed on the two files.  To view a colored diff in your terminal, include either the `-c` or `--color` option in your command:

##### Color diffs

```
$ fdiff --color [PRE-FONT FILE PATH] [POST-FONT FILE PATH]
```

### Other Options

Use `fdiff -h` to view all available options.

## Issues

Please report issues on the [project issue tracker](https://github.com/source-foundry/fdiff/issues).

## Contributing

Contributions are warmly welcomed.  A development dependency environment can be installed in editable mode with the developer installation documentation above. 

Please use the standard Github pull request approach to propose source changes.

### Source file linting

Python source files are linted with `flake8`.  See the Makefile `test-lint` target for details.

### Source file static type checks

Static type checks are performed on Python source files with `pytype`.  See the Makefile `test-type-check` target for details.

### Testing

The project runs continuous integration testing on [Travis CI](https://travis-ci.org/source-foundry/fdiff) and [Appveyor CI](https://ci.appveyor.com/project/chrissimpkins/fdiff) with the `pytest` and `tox` testing toolchain.  Test modules are located in the `tests` directory of the repository.

Local testing by Python interpreter version can be performed with the following command executed from the root of the repository:

```
$ tox -e [PYTHON INTERPRETER VERSION]
```

Please see the `tox` documentation for additional details.

### Test coverage

Unit test coverage is executed with the `coverage` tool.  See the Makefile `test-coverage` target for details.

## Acknowledgments

`fdiff` is built with the fantastic [fontTools free software library](https://github.com/fonttools/fonttools) and performs text diffs of binary font files using the TTX OpenType table data serialization format defined by that project.  The implementation of unified text file diffs is based on a (slightly) modified version of the Python `difflib` standard library source.  The modifications address performance issues with large text files like those encountered with the ttx dumps of font binary data used in this project.

## Licenses

### fdiff Project

Copyright 2019 Source Foundry Authors and Contributors

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

### Third Party Licenses

#### CPython `difflib` library

This project distributes a modified version of third party source code from the [Python programming language standard library](https://github.com/python/cpython).  The `difflib.py` v3.7.4 module is Copyright © 2001-2019 Python Software Foundation; All Rights Reserved. This source is modified and distributed in this project under the [PSF LICENSE AGREEMENT FOR PYTHON 3.7.4](https://github.com/source-foundry/fdiff/blob/master/lib/fdiff/thirdparty/PYTHON_LICENSE).  The module is renamed to `fdifflib.py` to distinguish it from the upstream source and modifications made here are documented in comments at the head of the module.


