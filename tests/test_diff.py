import os

import pytest

from fdiff.diff import u_diff

ROBOTO_BEFORE_PATH = os.path.join("tests", "testfiles", "Roboto-Regular.subset1.ttf")
ROBOTO_AFTER_PATH = os.path.join("tests", "testfiles", "Roboto-Regular.subset2.ttf")
ROBOTO_UDIFF_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_expected.txt")
ROBOTO_UDIFF_COLOR_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_color_expected.txt")

# Setup: define the expected diff text for unified diff
with open(ROBOTO_UDIFF_EXPECTED_PATH, "r") as robo_udiff:
    ROBOTO_UDIFF_EXPECTED = robo_udiff.read()

# Setup: define the expected diff text for unified color diff
with open(ROBOTO_UDIFF_COLOR_EXPECTED_PATH, "r") as robo_udiff_color:
    ROBOTO_UDIFF_COLOR_EXPECTED = robo_udiff_color.read()


def test_unified_diff_default():
    res = u_diff(ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH)
    res_string = "".join(res)
    assert res_string == ROBOTO_UDIFF_EXPECTED



