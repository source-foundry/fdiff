from fdiff.color import color_unified_diff_line

import pytest

TEST_LINE_PLUS = "+ A line with a plus"
TEST_LINE_MINUS = "- A line with a minus"
TEST_LINE_AT = "@@ -69705,5 +30839,3 @@"
TEST_LINE_PLUS3 = "+++ /Users/chris/Desktop/tests/dehinter-tests/Ubuntu-Regular-dehinted.ttf       2019-08-22T19:04:40.307911-04:00"
TEST_LINE_MINUS3 = "--- /Users/chris/Desktop/tests/dehinter-tests/Ubuntu-Regular.ttf        2010-12-15T00:00:00-05:00"
TEST_LINE_CONTEXT = " This is a line of context"


def test_color_unified_diff_line_addition():
    line_response = color_unified_diff_line(TEST_LINE_PLUS)
    assert line_response.startswith("\033[32m") is True
    assert line_response.endswith("\033[0m") is True


def test_color_unified_diff_line_removal():
    line_response = color_unified_diff_line(TEST_LINE_MINUS)
    assert line_response.startswith("\033[31m") is True
    assert line_response.endswith("\033[0m") is True


def test_color_unified_diff_line_range():
    line_response = color_unified_diff_line(TEST_LINE_AT)
    assert line_response.startswith("\033[36m") is True
    assert line_response.endswith("\033[0m") is True


def test_color_unified_diff_line_left_file():
    line_response = color_unified_diff_line(TEST_LINE_MINUS3)
    assert line_response.startswith("\033[31m") is True
    assert line_response.endswith("\033[0m") is True


def test_color_unified_diff_line_right_file():
    line_response = color_unified_diff_line(TEST_LINE_PLUS3)
    assert line_response.startswith("\033[32m") is True
    assert line_response.endswith("\033[0m") is True


def test_color_unified_diff_context_line():
    line_response = color_unified_diff_line(TEST_LINE_CONTEXT)
    assert line_response.startswith("\033") is False
    assert line_response.endswith("\033") is False
    assert line_response == TEST_LINE_CONTEXT
