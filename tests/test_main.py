#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import pytest

from fdiff.__main__ import run

ROBOTO_BEFORE_PATH = os.path.join("tests", "testfiles", "Roboto-Regular.subset1.ttf")
ROBOTO_AFTER_PATH = os.path.join("tests", "testfiles", "Roboto-Regular.subset2.ttf")
ROBOTO_UDIFF_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_expected.txt")
ROBOTO_UDIFF_COLOR_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_color_expected.txt")
ROBOTO_UDIFF_1CONTEXT_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_1context_expected.txt")
ROBOTO_UDIFF_HEADONLY_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_headonly_expected.txt")
ROBOTO_UDIFF_HEADPOSTONLY_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_headpostonly_expected.txt")
ROBOTO_UDIFF_EXCLUDE_HEADPOST_EXPECTED_PATH = os.path.join("tests", "testfiles", "roboto_udiff_ex_headpost_expected.txt")


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

#
# File path validations tests
#


def test_main_filepath_validations_false_firstfont(capsys):
    test_path = os.path.join("tests", "testfiles", "bogus-font.ttf")
    args = [test_path, test_path]

    with pytest.raises(SystemExit) as exit_info:
        run(args)
        captured = capsys.readouterr()
        assert captured.error.startswith("[*] ERROR: The file path")
        assert exit_info.value.code == 1


def test_main_filepath_validations_false_secondfont(capsys):
    test_path_2 = os.path.join("tests", "testfiles", "bogus-font.ttf")
    args = [ROBOTO_BEFORE_PATH, test_path_2]

    with pytest.raises(SystemExit) as exit_info:
        run(args)
        captured = capsys.readouterr()
        assert captured.error.startswith("[*] ERROR: The file path")
        assert exit_info.value.code == 1


#
#  Mutually exclusive argument tests
#

def test_main_include_exclude_defined_simultaneously(capsys):
    args = ["--include", "head", "--exclude", "head", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]

    with pytest.raises(SystemExit) as exit_info:
        run(args)
        captured = capsys.readouterr()
        assert captured.error.startswith("[*] Error: --include and --exclude are mutually exclusive options")
        assert exit_info.value.code == 1


#
#  Unified diff integration tests
#

def test_main_run_unified_default(capsys):
    args = [ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]

    run(args)
    captured = capsys.readouterr()

    res_string_list = captured.out.split("\n")
    expected_string_list = ROBOTO_UDIFF_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on different remote CI testing services
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x in (0, 1):
            assert line[0:9] == expected_string_list[x][0:9]
        else:
            assert line == expected_string_list[x]


def test_main_run_unified_color(capsys):
    args = ["-c", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]

    run(args)
    captured = capsys.readouterr()

    res_string_list = captured.out.split("\n")
    expected_string_list = ROBOTO_UDIFF_COLOR_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on different remote CI testing services
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x in (0, 1):
            assert line[0:9] == expected_string_list[x][0:9]
        else:
            assert line == expected_string_list[x]


def test_main_run_unified_context_lines_1(capsys):
    args = ["-l", "1", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]

    run(args)
    captured = capsys.readouterr()

    res_string_list = captured.out.split("\n")
    expected_string_list = ROBOTO_UDIFF_1CONTEXT_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on different remote CI testing services
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x in (0, 1):
            assert line[0:9] == expected_string_list[x][0:9]
        else:
            assert line == expected_string_list[x]


def test_main_run_unified_head_table_only(capsys):
    args = ["--include", "head", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]

    run(args)
    captured = capsys.readouterr()

    res_string_list = captured.out.split("\n")
    expected_string_list = ROBOTO_UDIFF_HEADONLY_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on different remote CI testing services
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x in (0, 1):
            assert line[0:9] == expected_string_list[x][0:9]
        else:
            assert line == expected_string_list[x]


def test_main_run_unified_head_post_tables_only(capsys):
    args = ["--include", "head,post", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]

    run(args)
    captured = capsys.readouterr()

    res_string_list = captured.out.split("\n")
    expected_string_list = ROBOTO_UDIFF_HEADPOSTONLY_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on different remote CI testing services
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x in (0, 1):
            assert line[0:9] == expected_string_list[x][0:9]
        else:
            assert line == expected_string_list[x]


def test_main_run_unified_exclude_head_post_tables(capsys):
    args = ["--exclude", "head,post", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]

    run(args)
    captured = capsys.readouterr()

    res_string_list = captured.out.split("\n")
    expected_string_list = ROBOTO_UDIFF_EXCLUDE_HEADPOST_EXPECTED.split("\n")

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on different remote CI testing services
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x in (0, 1):
            assert line[0:9] == expected_string_list[x][0:9]
        else:
            assert line == expected_string_list[x]


def test_main_include_with_bad_table_definition(capsys):
    args = ["--include", "bogus", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]

    with pytest.raises(SystemExit) as exit_info:
        run(args)
        captured = capsys.readouterr()
        assert captured.error.startswith("[*] ERROR:")
        assert exit_info.value.code == 1


def test_main_include_with_bad_table_definition_in_multi_table_request(capsys):
    args = ["--include", "head,bogus", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]

    with pytest.raises(SystemExit) as exit_info:
        run(args)
        captured = capsys.readouterr()
        assert captured.error.startswith("[*] ERROR:")
        assert exit_info.value.code == 1


def test_main_exclude_with_bad_table_definition(capsys):
    args = ["--exclude", "bogus", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]

    with pytest.raises(SystemExit) as exit_info:
        run(args)
        captured = capsys.readouterr()
        assert captured.error.startswith("[*] ERROR:")
        assert exit_info.value.code == 1


def test_main_exclude_with_bad_table_definition_in_multi_table_request(capsys):
    args = ["--exclude", "head,bogus", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]

    with pytest.raises(SystemExit) as exit_info:
        run(args)
        captured = capsys.readouterr()
        assert captured.error.startswith("[*] ERROR:")
        assert exit_info.value.code == 1


def test_main_head_request(capsys):
    args = ["--head", "4", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]

    run(args)
    captured = capsys.readouterr()
    res_string_list = captured.out.split("\n")

    # includes a newline at the end of the last line of output
    # which makes the total # of lines in the list == n + 1
    assert len(res_string_list) == 5

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on different remote CI testing services
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x == 0:
            assert line.startswith("---")
        elif x == 1:
            assert line.startswith("+++")
        elif x == 2:
            assert line == "@@ -4,34 +4,34 @@"
        elif x == 3:
            assert line == "   <GlyphOrder>"
        else:
            assert line == ""


def test_main_tail_request(capsys):
    args = ["--tail", "2", ROBOTO_BEFORE_PATH, ROBOTO_AFTER_PATH]

    run(args)
    captured = capsys.readouterr()
    res_string_list = captured.out.split("\n")

    # includes a newline at the end of the last line of output
    # which makes the total # of lines in the list == n + 1
    assert len(res_string_list) == 3

    # have to handle the tests for the top two file path lines
    # differently than the rest of the comparisons because
    # the time is defined using local platform settings
    # which makes tests fail on different remote CI testing services
    for x, line in enumerate(res_string_list):
        # treat top two lines of the diff as comparison of first 10 chars only
        if x == 0:
            assert line == "       </Lookup>"
        elif x == 1:
            assert line == "     </LookupList>"
        else:
            assert line == ""
