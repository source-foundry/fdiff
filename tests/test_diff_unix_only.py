import os
import sys
import pytest

from fdiff.diff import external_diff

# these tests rely on a PATH install of `diff` executable on Unix
# they are not executed on Windows platforms
if sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)

ROBOTO_BEFORE_PATH = os.path.join("tests", "testfiles", "Roboto-Regular.subset1.ttf")
ROBOTO_AFTER_PATH = os.path.join("tests", "testfiles", "Roboto-Regular.subset2.ttf")
ROBOTO_EXTDIFF_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_expected.txt")
ROBOTO_EXTDIFF_COLOR_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_color_expected.txt")

ROBOTO_BEFORE_URL = "https://github.com/source-foundry/fdiff/raw/master/tests/testfiles/Roboto-Regular.subset1.ttf"
ROBOTO_AFTER_URL = "https://github.com/source-foundry/fdiff/raw/master/tests/testfiles/Roboto-Regular.subset2.ttf"


# Setup: define the expected diff text for unified diff
with open(ROBOTO_EXTDIFF_EXPECTED_PATH, "r") as robo_extdiff:
    ROBOTO_EXTDIFF_EXPECTED = robo_extdiff.read()

# Setup: define the expected diff text for unified color diff
with open(ROBOTO_EXTDIFF_COLOR_EXPECTED_PATH, "r") as robo_extdiff_color:
    ROBOTO_EXTDIFF_COLOR_EXPECTED = robo_extdiff_color.read()


def test_external_diff_default():
    res = external_diff("diff -u", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH)
    expected_string_list = ROBOTO_EXTDIFF_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on remote CI testing services vs.
    # my local testing platform...
    for x, line in enumerate(res):
        # treat top two lines of the diff as comparison of first 3 chars only
        if x in (0, 1):
            assert line[0][0:2] == expected_string_list[x][0:2]
        elif x in range(2, 10):
            assert line[0] == expected_string_list[x] + os.linesep
        else:
            # skip lines beyond first 10
            pass


def test_external_diff_without_mp_optimizations():
    res = external_diff("diff -u", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH, use_multiprocess=False)
    expected_string_list = ROBOTO_EXTDIFF_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on remote CI testing services vs.
    # my local testing platform...
    for x, line in enumerate(res):
        # treat top two lines of the diff as comparison of first 3 chars only
        if x in (0, 1):
            assert line[0][0:2] == expected_string_list[x][0:2]
        elif x in range(2, 10):
            assert line[0] == expected_string_list[x] + os.linesep
        else:
            # skip lines beyond first 10
            pass


def test_external_diff_remote_fonts():
    res = external_diff("diff -u", ROBOTO_BEFORE_URL, ROBOTO_AFTER_URL)
    expected_string_list = ROBOTO_EXTDIFF_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on remote CI testing services vs.
    # my local testing platform...
    for x, line in enumerate(res):
        # treat top two lines of the diff as comparison of first 3 chars only
        if x in (0, 1):
            assert line[0][0:2] == expected_string_list[x][0:2]
        elif x in range(2, 10):
            assert line[0] == expected_string_list[x] + os.linesep
        else:
            # skip lines beyond first 10
            pass
