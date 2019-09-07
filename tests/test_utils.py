import os
import re

from fdiff.utils import get_file_modtime, get_tables_argument_list, file_exists

import pytest


def test_file_exists_true():
    assert file_exists(os.path.join("tests", "testfiles", "test.txt")) is True


def test_file_exists_false():
    assert file_exists(os.path.join("tests", "testfiles", "bogus.jpg")) is False


def test_get_file_modtime():
    modtime = get_file_modtime(os.path.join("tests", "testfiles", "test.txt"))
    assert modtime.startswith("2019-09-0") is True
    regex = re.compile(r"""\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+[-+]\d{2}:\d{2}""")
    assert regex.fullmatch(modtime) is not None


def test_get_tables_argument_list():
    string1 = "head"
    string2 = "head,post"
    string3 = "head,post,cvt"
    assert get_tables_argument_list(string1) == ["head"]
    assert get_tables_argument_list(string2) == ["head", "post"]
    assert get_tables_argument_list(string3) == ["head", "post", "cvt "]
