import os
import tempfile

import pytest

from fdiff.aio import async_write_bin


@pytest.mark.asyncio
async def test_async_write():
    with tempfile.TemporaryDirectory() as tmpdirname:
        test_path = os.path.join(tmpdirname, "test.bin")
        await async_write_bin(test_path, b"test")
        assert os.path.exists(test_path) is True
        with open(test_path, "rb") as f:
            res = f.read()
            assert res == b"test"
