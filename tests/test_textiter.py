

import pytest

from fdiff.textiter import head, tail

text_list = [
    "line 1",
    "line 2",
    "line 3",
    "line 4",
    "line 5"
]


def test_head():
    head_res = head(text_list, 2)
    assert len(list(head_res)) == 2
    for x, line in enumerate(head_res):
        assert line == text_list[x]


def test_head_request_more_than_available():
    head_res = head(text_list, 6)
    assert len(list(head_res)) == 5
    for x, line in enumerate(head_res):
        assert line == text_list[x]


def test_tail():
    tail_res = tail(text_list, 2)
    assert len(list(tail_res)) == 2
    offset = 3
    for x, line in enumerate(tail_res):
        assert line == text_list[offset + x]


def test_tail_request_more_than_available():
    tail_res = tail(text_list, 6)
    assert len(list(tail_res)) == 5
    for x, line in enumerate(tail_res):
        assert line == text_list[x]