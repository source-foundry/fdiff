import os
import tempfile

import pytest

from fontTools.ttLib import TTFont

from fdiff.diff import u_diff, _ttfont_save_xml
from fdiff.exceptions import AIOError

ROBOTO_BEFORE_PATH = os.path.join("tests", "testfiles", "Roboto-Regular.subset1.ttf")
ROBOTO_AFTER_PATH = os.path.join("tests", "testfiles", "Roboto-Regular.subset2.ttf")
ROBOTO_UDIFF_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_expected.txt")
ROBOTO_UDIFF_COLOR_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_color_expected.txt")
ROBOTO_UDIFF_1CONTEXT_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_1context_expected.txt")
ROBOTO_UDIFF_HEADONLY_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_headonly_expected.txt")
ROBOTO_UDIFF_HEADPOSTONLY_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_headpostonly_expected.txt")
ROBOTO_UDIFF_EXCLUDE_HEADPOST_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_ex_headpost_expected.txt")

ROBOTO_BEFORE_URL = "https://github.com/source-foundry/fdiff/raw/master/tests/testfiles/Roboto-Regular.subset1.ttf"
ROBOTO_AFTER_URL = "https://github.com/source-foundry/fdiff/raw/master/tests/testfiles/Roboto-Regular.subset2.ttf"

URL_404 = "https://httpbin.org/status/404"

# Setup: define the expected diff text for unified diff
with open(ROBOTO_UDIFF_EXPECTED_PATH, "r") as robo_udiff:
    ROBOTO_UDIFF_EXPECTED = robo_udiff.read()

# Setup: define the expected diff text for unified color diff
with open(ROBOTO_UDIFF_COLOR_EXPECTED_PATH, "r") as robo_udiff_color:
    ROBOTO_UDIFF_COLOR_EXPECTED = robo_udiff_color.read()

# Setup: define the expected diff text for unified color diff
with open(ROBOTO_UDIFF_1CONTEXT_EXPECTED_PATH, "r") as robo_udiff_contextlines:
    ROBOTO_UDIFF_1CONTEXT_EXPECTED = robo_udiff_contextlines.read()

# Setup: define the expected diff text for head table only diff
with open(ROBOTO_UDIFF_HEADONLY_EXPECTED_PATH, "r") as robo_udiff_headonly:
    ROBOTO_UDIFF_HEADONLY_EXPECTED = robo_udiff_headonly.read()

# Setup: define the expected diff text for head and post table only diff
with open(ROBOTO_UDIFF_HEADPOSTONLY_EXPECTED_PATH, "r") as robo_udiff_headpostonly:
    ROBOTO_UDIFF_HEADPOSTONLY_EXPECTED = robo_udiff_headpostonly.read()

# Setup: define the expected diff text for head and post table only diff
with open(ROBOTO_UDIFF_EXCLUDE_HEADPOST_EXPECTED_PATH, "r") as robo_udiff_ex_headpost:
    ROBOTO_UDIFF_EXCLUDE_HEADPOST_EXPECTED = robo_udiff_ex_headpost.read()


def test_unified_diff_default_no_diff():
    res = u_diff(ROBOTO_BEFORE_PATH, ROBOTO_BEFORE_PATH)
    res_string = "".join(res)
    assert res_string == ""


def test_unified_diff_default():
    res = u_diff(ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH)
    res_string = "".join(res)
    res_string_list = res_string.split("\n")
    expected_string_list = ROBOTO_UDIFF_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on remote CI testing services vs.
    # my local testing platform...
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x in (0, 1):
            assert line[0:9] == expected_string_list[x][0:9]
        else:
            assert line == expected_string_list[x]


def test_unified_diff_without_mp_optimizations():
    res = u_diff(ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH, use_multiprocess=False)
    res_string = "".join(res)
    res_string_list = res_string.split("\n")
    expected_string_list = ROBOTO_UDIFF_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on remote CI testing services vs.
    # my local testing platform...
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x in (0, 1):
            assert line[0:9] == expected_string_list[x][0:9]
        else:
            assert line == expected_string_list[x]


def test_unified_diff_context_lines_1():
    res = u_diff(ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH, context_lines=1)
    res_string = "".join(res)
    res_string_list = res_string.split("\n")
    expected_string_list = ROBOTO_UDIFF_1CONTEXT_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on remote CI testing services vs.
    # my local testing platform...
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x in (0, 1):
            assert line[0:9] == expected_string_list[x][0:9]
        else:
            assert line == expected_string_list[x]


def test_unified_diff_head_table_only():
    res = u_diff(ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH, include_tables=["head"])
    res_string = "".join(res)
    res_string_list = res_string.split("\n")
    expected_string_list = ROBOTO_UDIFF_HEADONLY_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on remote CI testing services vs.
    # my local testing platform...
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x in (0, 1):
            assert line[0:9] == expected_string_list[x][0:9]
        else:
            assert line == expected_string_list[x]


def test_unified_diff_headpost_table_only():
    res = u_diff(ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH, include_tables=["head", "post"])
    res_string = "".join(res)
    res_string_list = res_string.split("\n")
    expected_string_list = ROBOTO_UDIFF_HEADPOSTONLY_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on remote CI testing services vs.
    # my local testing platform...
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x in (0, 1):
            assert line[0:9] == expected_string_list[x][0:9]
        else:
            assert line == expected_string_list[x]


def test_unified_diff_exclude_headpost_tables():
    res = u_diff(ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH, exclude_tables=["head", "post"])
    res_string = "".join(res)
    res_string_list = res_string.split("\n")
    expected_string_list = ROBOTO_UDIFF_EXCLUDE_HEADPOST_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on remote CI testing services vs.
    # my local testing platform...
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x in (0, 1):
            assert line[0:9] == expected_string_list[x][0:9]
        else:
            assert line == expected_string_list[x]


def test_unified_diff_include_with_bad_table_definition():
    with pytest.raises(KeyError):
        u_diff(ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH, include_tables=["bogus"])


def test_unified_diff_exclude_with_bad_table_definition():
    with pytest.raises(KeyError):
        u_diff(ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH, exclude_tables=["bogus"])


def test_unified_diff_remote_fonts():
    res = u_diff(ROBOTO_BEFORE_URL, ROBOTO_AFTER_URL)
    res_string = "".join(res)
    res_string_list = res_string.split("\n")
    expected_string_list = ROBOTO_UDIFF_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x == 0:
            assert line[0:9] == "--- https"
        elif x == 1:
            assert line[0:9] == "+++ https"
        else:
            assert line == expected_string_list[x]


def test_unified_diff_remote_and_local_fonts():
    res = u_diff(ROBOTO_BEFORE_URL, ROBOTO_AFTER_PATH)
    res_string = "".join(res)
    res_string_list = res_string.split("\n")
    expected_string_list = ROBOTO_UDIFF_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x == 0:
            assert line[0:9] == "--- https"
        elif x == 1:
            assert line[0:9] == expected_string_list[x][0:9]
        else:
            assert line == expected_string_list[x]


def test_unified_diff_local_and_remote_fonts():
    res = u_diff(ROBOTO_BEFORE_PATH, ROBOTO_AFTER_URL)
    res_string = "".join(res)
    res_string_list = res_string.split("\n")
    expected_string_list = ROBOTO_UDIFF_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x == 0:
            assert line[0:9] == expected_string_list[x][0:9]
        elif x == 1:
            assert line[0:9] == "+++ https"
        else:
            assert line == expected_string_list[x]


def test_unified_diff_remote_404_first_file():
    with pytest.raises(AIOError):
        u_diff(URL_404, ROBOTO_AFTER_URL)


def test_unified_diff_remote_404_second_file():
    with pytest.raises(AIOError):
        u_diff(ROBOTO_BEFORE_URL, URL_404)


def test_unified_diff_remote_non_url_exception():
    """This raises an exception in the aiohttp get request call"""
    with pytest.raises(AIOError):
        u_diff("https:bogus", "https:bogus")


#
#
#  Private functions
#
#

def test_ttfont_save_xml():
    tt = TTFont(ROBOTO_BEFORE_PATH)
    with tempfile.TemporaryDirectory() as tmpdirname:
        path = os.path.join(tmpdirname, "test.ttx")
        _ttfont_save_xml(tt, path, None, None)
        assert os.path.isfile(path)