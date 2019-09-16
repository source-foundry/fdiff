from fdiff.exceptions import AIOError

import pytest


def raise_aioerror(message):
    raise AIOError(message)


def test_aioerror_raises():
    with pytest.raises(AIOError) as e:
        raise_aioerror("Test message")

    assert str(e.value) == "Test message"


