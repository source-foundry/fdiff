import os

import pytest

from fdiff.diff import u_diff

ROBOTO_BEFORE_PATH = os.path.join("tests", "testfiles", "Roboto-Regular.subset1.ttf")
ROBOTO_AFTER_PATH = os.path.join("tests", "testfiles", "Roboto-Regular.subset2.ttf")
ROBOTO_UDIFF_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_expected.txt")
ROBOTO_UDIFF_COLOR_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_color_expected.txt")
ROBOTO_UDIFF_1CONTEXT_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_1context_expected.txt")

# Setup: define the expected diff text for unified diff
with open(ROBOTO_UDIFF_EXPECTED_PATH, "r") as robo_udiff:
    ROBOTO_UDIFF_EXPECTED = robo_udiff.read()

# Setup: define the expected diff text for unified color diff
with open(ROBOTO_UDIFF_COLOR_EXPECTED_PATH, "r") as robo_udiff_color:
    ROBOTO_UDIFF_COLOR_EXPECTED = robo_udiff_color.read()

# Setup: define the expected diff text for unified color diff
with open(ROBOTO_UDIFF_1CONTEXT_EXPECTED_PATH, "r") as robo_udiff_contextlines:
    ROBOTO_UDIFF_1CONTEXT_EXPECTED = robo_udiff_contextlines.read()


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




