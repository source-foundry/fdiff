<img src="https://raw.githubusercontent.com/source-foundry/fdiff/img/img/fdiff_logo-crunch.png" width="250" />
<br/>

## An OpenType table diff tool for fonts

[![PyPI](https://img.shields.io/pypi/v/fdiff?color=blueviolet&label=PyPI&logo=python&logoColor=white)](https://pypi.org/project/fdiff/)
[![GitHub license](https://img.shields.io/github/license/source-foundry/fdiff?color=blue)](https://github.com/source-foundry/fdiff/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/source-foundry/fdiff.svg?branch=master)](https://travis-ci.org/source-foundry/fdiff)
[![Build status](https://ci.appveyor.com/api/projects/status/eafvbkc4iyv78dip/branch/master?svg=true)](https://ci.appveyor.com/project/chrissimpkins/fdiff/branch/master)
[![codecov](https://codecov.io/gh/source-foundry/fdiff/branch/master/graph/badge.svg)](https://codecov.io/gh/source-foundry/fdiff)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b58954eda44b4fd88ad8f4fa06e8010b)](https://www.codacy.com/app/SourceFoundry/fdiff)


## About

`fdiff` is a Python command line comparison tool for assessment of differences in the OpenType table data between font files.  The tool provides cross-platform support for local and remote font diffs on macOS, Windows, and GNU/Linux systems with a Python v3.6+ interpreter.

<p align="center">
<img src="https://raw.githubusercontent.com/source-foundry/fdiff/img/img/diff-example-crunch.png" width="500"/>
</p>

## What it does

- Takes two font file path arguments (or URL for remote fonts) for the font comparison
- Dumps OpenType table data in the fontTools library TTX format (XML)
- Compares the OpenType table data across the two files using the unified diff format with 3 lines of surrounding context

## Optional Features

- View colored diffs in the terminal with the `-c` or `--color` flag
- Filter OpenType tables with the `--include` or `--exclude` options
- Modify the number of context lines displayed in the diff with the `-l` or `--lines` option
- Display the first n lines of the diff output with the `--head` option
- Display the last n lines of the diff output with the `--tail` option
- Execute the diff with an external diff tool using the `--external` option

Run `fdiff --help` to view all available options.

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [Issues](#issues)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [Licenses](#licenses)

## Installation

`fdiff` requires a Python 3.6+ interpreter.

Installation in a [Python3 virtual environment](https://docs.python.org/3/library/venv.html) is recommended.

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

The following approach installs the project and associated optional developer dependencies, so that source changes are available without the need for re-installation.

```
$ git clone https://github.com/source-foundry/fdiff.git
$ cd fdiff
$ pip3 install --ignore-installed -r requirements.txt -e ".[dev]"
```

## Usage

#### Local font files

```
$ fdiff [OPTIONS] [PRE-FONT FILE PATH] [POST-FONT FILE PATH]
```

#### Remote font files

`fdiff` supports GET requests for publicly accessible remote font files.  Replace the file path arguments with URL:

```
$ fdiff [OPTIONS] [PRE-FONT FILE URL] [POST-FONT FILE URL]
```

`fdiff` works with any combination of local and remote font files. For example, to compare a local post font file with a remote pre font file to assess local changes against a font file that was previously pushed to a remote, use the following syntax:

```
$ fdiff [OPTIONS] [PRE-FONT FILE URL] [POST-FONT FILE FILE PATH]
```

⭐ **Tip**: Remote git repository hosting services (like Github) support access to files on different git branches by URL.  Use these repository branch URL to compare fonts across git branches in your repository.

### Options

#### Color diffs

Uncolored diffs are performed by default.

To view a colored diff in your terminal, include either the `-c` or `--color` option in your command:

```
$ fdiff --color [PRE-FONT FILE PATH] [POST-FONT FILE PATH]
```

#### Filter OpenType tables

To include only specified tables in your diff, use the `--include` option with a comma-separated list of table names:

```
$ fdiff --include head,post [PRE-FONT FILE PATH] [POST-FONT FILE PATH]
```

To exclude specified tables in your diff, use the `--exclude` option with a comma-separated list of table names:

```
$ fdiff --exclude glyf,OS/2 [PRE-FONT FILE PATH] [POST-FONT FILE PATH]
```

**Do not include spaces** between the comma-separated table name values!

#### Change number of context lines

To change the number of lines of context above/below lines that have differences, use the `-l` or `--lines` option with an integer value for the desired number of lines.  The following command reduces the contextual information to a single line above and below lines with differences: 

```
$ fdiff -l 1 [PRE-FONT FILE PATH] [POST-FONT FILE PATH]
```

#### Display the first n lines of output

Use the `--head` option followed by an integer for the number of lines at the beginning of the output.  For example, the following command displays the first 20 lines of the diff:

```
$ fdiff --head 20 [PRE-FONT FILE PATH] [POST-FONT FILE PATH]
```

#### Display the last n lines of output

Use the `--tail` option followed by an integer for the number of lines at the end of the output.  For example, the following command displays the last 20 lines of the diff:

```
$ fdiff --tail 20 [PRE-FONT FILE PATH] [POST-FONT FILE PATH]
```

#### Use an external diff tool <img src="https://img.shields.io/badge/beta-feature-orange" />

**Please Note**: This feature has not been tested across all supported platforms.  Please report any issues that you come across on the project issue tracker.  

By default, fdiff performs diffs with Python source.  If you run into performance issues with this approach, you can use compiled diff executables that are available on your platform.  fdiff will dump the ttx files and run the command that you provide on the command line passing the pre and post font ttx dump file paths as the first and second positional arguments to your command.

For example, you may run the `diff -u` command on GNU/Linux or macOS like this:

```
$ fdiff --external="diff -u" [PRE-FONT FILE PATH] [POST-FONT FILE PATH]
```

fdiff supports built-in color formatting and OpenType table filtering when used with external diff tools.  The context line, head, and tail options are not supported with the use of external diff tools.


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

`fdiff` is built with the fantastic [fontTools free software library](https://github.com/fonttools/fonttools) and performs text diffs of binary font files using dumps of the TTX OpenType table data serialization format as defined in the fontTools library.  The implementation of unified text file diffs is based on a (slightly) modified version of the Python `difflib` standard library source.  The modifications address diff performance issues with the lengthy text output from TTX dumps of font OpenType data. 

## Licenses

### fdiff

Copyright 2019 Source Foundry Authors and Contributors

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

### Third-Party Licenses

#### CPython `difflib` library

This project distributes a modified version of third party source code from the [Python programming language standard library](https://github.com/python/cpython).  The `difflib.py` v3.7.4 module is Copyright © 2001-2019 Python Software Foundation; All Rights Reserved. This source is modified and distributed in this project under the [PSF LICENSE AGREEMENT FOR PYTHON 3.7.4](https://github.com/source-foundry/fdiff/blob/master/lib/fdiff/thirdparty/PYTHON_LICENSE).  The module is renamed to `fdifflib.py` to distinguish it from the upstream source, and modifications made here are documented in comments at the head of the module.


