# Changelog

## v0.2.0

- Added support for OpenType table include and exclude filters
	- `fdiff` executable: added `--include` option and defined comma delimited syntax for OpenType table command line definitions
	- `fdiff` executable: added `--exclude` option and defined comma delimited syntax for OpenType table command line defintions
	- `fdiff` executable: added validation check for use of mutually exclusive `--include` and `--exclude` options
	- Library: added new `fdiff.utils.get_tables_argument_list` function
	- Library: updated `fdiff.diff.u_diff` function with new `include_tables` and `exclude_tables` arguments
	- Library: added OpenType table validations for user-specified name values in the `fdiff.diff.u_diff` function.  These checks confirm that at least one of the requested files includes tables specified with the new `--include` and `--exclude` options

## v0.1.0

- Initial release with support for the following features:
    - local font file unified diff of OpenType table data dumped from the font binaries in the TTX data serialization format
    - ANSI escape code colored diff renders with the `-c` or `--color` command line options
- Custom version of the third party Python standard library `difflib` module that includes a modification of the "autojunk" heuristics approach to achieve a significant unified diff performance improvement with large text files like those that are encountered in the typical TTX dump from fonts 

## v0.0.1

- pre-release version that did not include executable source code
