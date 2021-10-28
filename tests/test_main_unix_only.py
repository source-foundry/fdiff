#!/usr/bin/env python3

import os
import sys
from unittest.mock import MagicMock

import pytest

from fdiff.__main__ import run

ROBOTO_BEFORE_PATH = os.path.join("tests", "testfiles", "Roboto-Regular.subset1.ttf")
ROBOTO_AFTER_PATH = os.path.join("tests", "testfiles", "Roboto-Regular.subset2.ttf")
ROBOTO_EXTDIFF_EXPECTED_PATH = os.path.join(
    "tests", "testfiles", "roboto_extdiff_expected.txt"
)
ROBOTO_EXTDIFF_COLOR_EXPECTED_PATH = os.path.join(
    "tests", "testfiles", "roboto_extdiff_color_expected.txt"
)

ROBOTO_BEFORE_URL = "https://github.com/source-foundry/fdiff/raw/master/tests/testfiles/Roboto-Regular.subset1.ttf"
ROBOTO_AFTER_URL = "https://github.com/source-foundry/fdiff/raw/master/tests/testfiles/Roboto-Regular.subset2.ttf"


# Setup: define the expected diff text for unified diff
with open(ROBOTO_EXTDIFF_EXPECTED_PATH, "r") as robo_extdiff:
    ROBOTO_EXTDIFF_EXPECTED = robo_extdiff.read()

# Setup: define the expected diff text for unified color diff
with open(ROBOTO_EXTDIFF_COLOR_EXPECTED_PATH, "r") as robo_extdiff_color:
    ROBOTO_EXTDIFF_COLOR_EXPECTED = robo_extdiff_color.read()


# # these tests rely on a PATH install of `diff` executable on Unix
# # they are not executed on Windows platforms
if sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)


def test_main_external_diff_default(capsys):
    args = ["--external", "diff -u", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]
    expected_string_list = ROBOTO_EXTDIFF_EXPECTED.split("\n")

    with pytest.raises(SystemExit):
        run(args)

    captured = capsys.readouterr()
    res_string_list = captured.out.split("\n")
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 3 chars only
        if x in (0, 1):
            assert line[0:2] == expected_string_list[x][0:2]
        elif x in range(2, 10):
            assert line == expected_string_list[x]
        else:
            # skip lines beyond first 10
            pass


def test_main_external_diff_remote(capsys):
    args = ["--external", "diff -u", ROBOTO_BEFORE_URL, ROBOTO_AFTER_URL]
    expected_string_list = ROBOTO_EXTDIFF_EXPECTED.split("\n")

    with pytest.raises(SystemExit):
        run(args)

    captured = capsys.readouterr()
    res_string_list = captured.out.split("\n")
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 3 chars only
        if x in (0, 1):
            assert line[0:2] == expected_string_list[x][0:2]
        elif x in range(2, 10):
            assert line == expected_string_list[x]
        else:
            # skip lines beyond first 10
            pass


def test_main_external_diff_color(capsys):
    # prior to v3.0.0, the `-c` / `--color` option was required for color output
    # this is the default as of v3.0.0 and the test arguments were
    # modified here
    args = ["--external", "diff -u", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]
    # we also need to patch sys.stdout.isatty because color does not
    # show when this returns False
    sys.stdout.isatty = MagicMock(return_value=True)
    # expected_string_list = ROBOTO_EXTDIFF_COLOR_EXPECTED.split("\n")

    with pytest.raises(SystemExit):
        run(args)

    captured = capsys.readouterr()

    # spot checks for escape code start sequence
    res_string_list = captured.out.split("\n")
    assert captured.out.startswith("\x1b")
    assert res_string_list[10].startswith("\x1b")
    assert res_string_list[71].startswith("\x1b")
    assert res_string_list[180].startswith("\x1b")
    assert res_string_list[200].startswith("\x1b")
    assert res_string_list[238].startswith("\x1b")


def test_main_external_diff_with_head_fails(capsys):
    args = ["--external", "diff -u", "--head", "1", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]

    with pytest.raises(SystemExit) as exit_info:
        run(args)

    captured = capsys.readouterr()
    assert "[ERROR] The head and tail options are not supported" in captured.err
    assert exit_info.value.code == 1


def test_main_external_diff_with_tail_fails(capsys):
    args = ["--external", "diff -u", "--tail", "1", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]

    with pytest.raises(SystemExit) as exit_info:
        run(args)

    captured = capsys.readouterr()
    assert "[ERROR] The head and tail options are not supported" in captured.err
    assert exit_info.value.code == 1


def test_main_external_diff_with_lines_fails(capsys):
    args = [
        "--external",
        "diff -u",
        "--lines",
        "1",
        ROBOTO_BEFORE_PATH,
        ROBOTO_AFTER_PATH,
    ]

    with pytest.raises(SystemExit) as exit_info:
        run(args)

    captured = capsys.readouterr()
    assert "[ERROR] The lines option is not supported" in captured.err
    assert exit_info.value.code == 1
