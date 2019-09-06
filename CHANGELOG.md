# Changelog

## v0.1.0

- Initial release with support for the following features:
    - local font file unified diff of OpenType table data dumped from the font binaries in the TTX data serialization format
    - ANSI escape code colored diff renders with the `-c` or `--color` command line options
- Custom version of the third party Python standard library `difflib` module that includes a modification of the "autojunk" heuristics approach to achieve a significant unified diff performance improvement with large text files like those that are encountered in the typical TTX dump from fonts 

## v0.0.1

- pre-release version that did not include executable source code
