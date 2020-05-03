import os
import re

from fdiff.utils import get_file_modtime, get_tables_argument_list, path_exists

import pytest


def test_path_exists_default_true():
    assert (
        path_exists(
            os.path.join("tests", "testfiles", "test.txt"), include_dir_paths=False
        )
        is True
    )


def test_path_exists_default_false():
    assert (
        path_exists(
            os.path.join("tests", "testfiles", "bogus.jpg"), include_dir_paths=False
        )
        is False
    )


def test_path_exists_default_dirpath_fails():
    assert (
        path_exists(os.path.join("tests", "testfiles"), include_dir_paths=False)
        is False
    )


def test_path_exists_default_dirpath_toggle_succeeds():
    assert (
        path_exists(os.path.join("tests", "testfiles"), include_dir_paths=True) is True
    )


def test_get_file_modtime():
    modtime = get_file_modtime(os.path.join("tests", "testfiles", "test.txt"))
    regex = re.compile(r"""\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+[-+]\d{2}:\d{2}""")
    assert regex.fullmatch(modtime) is not None


def test_get_tables_argument_list():
    string1 = "head"
    string2 = "head,post"
    string3 = "head,post,cvt"
    assert get_tables_argument_list(string1) == ["head"]
    assert get_tables_argument_list(string2) == ["head", "post"]
    assert get_tables_argument_list(string3) == ["head", "post", "cvt "]
