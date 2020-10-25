# Changelog

## v2.1.1

- Add cPython 3.9 interpreter unit testing
- Add CodeQL static source testing 
- Bump fonttools dependency to v4.16.1
- Bump aiohttp dependency to v3.6.3
- Bump multidict dependency to v5.0.0
- Bump yarl dependency to v1.6.2

## v2.1.0

- Add type annotations to all Python source files
- Refactor `remote.py` module namedtuple to Py3.6+ style `NamedTuple` derived class with type annotations
- Transition from pytype to mypy as static type checker
- Add GitHub Action static type check configuration
- Refactor import statements with default `isort` formatting
- Bump fonttools dependency to v4.15.0

## v2.0.2

- update cffi dependency to bug fix release v1.14.3

## v2.0.1

- Refactor to maintain line length < 90
- Add flake8 linting as part of the CI
- Transition to GitHub Actions CI testing service
- Bump attrs dependency to v20.2.0
- Bump cffi dependency to v1.14.2
- Bump fonttools dependency to v4.14.0
- Bump idna dependency to v2.10
- Bump multidict dependency to v4.7.6
- Bump yarl dependendency to v1.5.1

## v2.0.0

- Backward incompatible change in the default unified diff approach for large files (fixes #54)
- Transition to the upstream cPython implementation of `difflib.unified_diff` for diff execution
- Remove cPython `difflib` derivative that was distributed with this project
- Eliminate dual license structure with removal of cPython license and transition to Apache License, v2.0 only

## v1.0.2

- Bump cffi to 1.14.0
- Bump fonttools to 4.6.0
- Bump idna to 2.9
- Bump multidict to 4.7.5
- Bump pycares to 3.1.1
- Bump pycparser to 2.20
- Source formatting (black)
- Add Py3.8 CI testing on Linux
- Add Py3.6 64-bit testing, Py3.8 64-bit testing on Windows
- Use pinned dependency versions in CI testing with tox

## v1.0.1

- Bump fonttools from 4.2.2 to 4.2.4
- Bump multidict from 4.7.3 to 4.7.4
- Bump pycares from 3.1.0 to 3.1.1

## v1.0.0

- `fdiff` executable: added support for external executable tool diff execution with a new `--external` option
- Library: major refactor of the `fdiff.diff` module
- Library: add new public `external_diff` function to the `fdiff.diff` module
- Library: minor refactor of `fdiff.color` module (removed unnecessary import)
- [bugfix] Library: fixed bug in ANSI color output
- updated fontTools dependency to v4.2.2
- updated aiohttp dependency to v3.6.2
- pinned the versions of the following dependencies of dependencies in the requirements.txt file: async-timeout, attrs, cffi, chardet, idna, multidict, pycares, pycparser, yarl

## v0.5.1

- `fdiff` executable: Fix help message - added information about pre/post file argument support for URL in addition to local file paths

## v0.5.0

- Performance optimizations - Library: New default parallel TTX XML dump on systems that have more than one CPU, falls back to sequential execution on single CPU systems - `fdiff` executable: New `--nomp` option that overrides the default multi processor optimizations
- `fdiff` executable: Added new default standard output user notification that no difference was identified when the files under evaluation are the same. This replaces no output in the standard output stream and an exit status code of zero as the indicators that there were no differences identified between the files.

## v0.4.0

- Added support for remote font files with asynchronous I/O GET requests. This feature supports combinations of local and remote font file comparisons.
  - `fdiff` executable: added support for remote font files with command line URL arguments
  - `fdiff` executable: refactored unified diff error message formatting
  - Library: add new `fdiff.remote` module
  - Library: add new `fdiff.aio` module
  - Library: add new `fdiff.exceptions` module
  - Library: refactored `fdiff.diff.unified_diff()` function to support remote files through URL
  - Library: refactored local file path checks to support remote files via URL
  - added new aiohttp, aiodns, aiofiles dependencies to requirements.txt
  - added new aiohttp, aiodns, aiofiles dependencies to setup.py
  - added pytest-asyncio dependency to setup.py [dev] install target
  - added pytest-asyncio dependency instatllation to tox.ini, .travis.yml, .appveyor.yml configuration files
- Py3.6+ updates: removed `# -*- coding: utf-8 -*-` header definitions (Thanks Niko!)
- updated fontTools dependency to v4.0.1 (from v4.0.0)
- Updated README.md documentation

## v0.3.0

- Added support for head and tail diff output filter functionality - `fdiff` executable: add support for filtered diff output by top n lines with new `--head` option - `fdiff` executable: add support for filtered diff output by last n lines with new `--tail` option - Library: add new `fdiff.textiter` module
- Add README.md table of contents

## v0.2.0

- Added support for OpenType table include and exclude filters - `fdiff` executable: added `--include` option and defined comma delimited syntax for OpenType table command line definitions - `fdiff` executable: added `--exclude` option and defined comma delimited syntax for OpenType table command line defintions - `fdiff` executable: added validation check for use of mutually exclusive `--include` and `--exclude` options - Library: added new `fdiff.utils.get_tables_argument_list` function - Library: updated `fdiff.diff.u_diff` function with new `include_tables` and `exclude_tables` arguments - Library: added OpenType table validations for user-specified name values in the `fdiff.diff.u_diff` function. These checks confirm that at least one of the requested files includes tables specified with the new `--include` and `--exclude` options

## v0.1.0

- Initial release with support for the following features:
  - local font file unified diff of OpenType table data dumped from the font binaries in the TTX data serialization format
  - ANSI escape code colored diff renders with the `-c` or `--color` command line options
- Custom version of the third party Python standard library `difflib` module that includes a modification of the "autojunk" heuristics approach to achieve a significant unified diff performance improvement with large text files like those that are encountered in the typical TTX dump from fonts

## v0.0.1

- pre-release version that did not include executable source code
