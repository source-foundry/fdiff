import os
import tempfile

import pytest

import aiohttp

from fdiff.remote import _get_filepath_from_url, async_fetch, async_fetch_and_write, create_async_get_request_session_and_run

REMOTE_FONT_1 = "https://github.com/source-foundry/fdiff/raw/master/tests/testfiles/Roboto-Regular.subset1.ttf"
REMOTE_FONT_2 = "https://github.com/source-foundry/fdiff/raw/master/tests/testfiles/Roboto-Regular.subset2.ttf"

URL_200 = "https://httpbin.org/status/200"
URL_404 = "https://httpbin.org/status/404"


def test_get_temp_filepath_from_url():
    res = _get_filepath_from_url(REMOTE_FONT_1, os.path.join("test", "path"))
    assert res == os.path.join("test", "path", "Roboto-Regular.subset1.ttf")


@pytest.mark.asyncio
async def test_async_fetch_200():
    async with aiohttp.ClientSession() as session:
        url, status, binary = await async_fetch(session, URL_200)
        assert url == URL_200
        assert status == 200
        assert binary is not None


@pytest.mark.asyncio
async def test_async_fetch_404():
    async with aiohttp.ClientSession() as session:
        url, status, binary = await async_fetch(session, URL_404)
        assert url == URL_404
        assert status == 404
        assert binary is None


@pytest.mark.asyncio
async def test_async_fetch_and_write_200():
    with tempfile.TemporaryDirectory() as tmpdirname:
        async with aiohttp.ClientSession() as session:
            fwres = await async_fetch_and_write(session, REMOTE_FONT_1, tmpdirname)
            assert fwres.url == REMOTE_FONT_1
            assert fwres.filepath == _get_filepath_from_url(REMOTE_FONT_1, tmpdirname)
            assert fwres.http_status == 200
            assert fwres.write_success is True


@pytest.mark.asyncio
async def test_async_fetch_and_write_404():
    with tempfile.TemporaryDirectory() as tmpdirname:
        async with aiohttp.ClientSession() as session:
            fwres = await async_fetch_and_write(session, URL_404, tmpdirname)
            assert fwres.url == URL_404
            assert fwres.filepath is None
            assert fwres.http_status == 404
            assert fwres.write_success is False


@pytest.mark.asyncio
async def test_create_async_get_request_session_and_run_200():
    urls = [REMOTE_FONT_1, REMOTE_FONT_2]
    with tempfile.TemporaryDirectory() as tmpdirname:
        tasks = await create_async_get_request_session_and_run(urls, tmpdirname)
        for x, task in enumerate(tasks):
            assert task.exception() is None
            assert task.result().url == urls[x]
            assert task.result().http_status == 200
            assert os.path.exists(task.result().filepath)
            assert task.result().write_success is True


@pytest.mark.asyncio
async def test_create_async_get_request_session_and_run_404_single():
    urls = [REMOTE_FONT_1, URL_404]
    with tempfile.TemporaryDirectory() as tmpdirname:
        tasks = await create_async_get_request_session_and_run(urls, tmpdirname)
        for x, task in enumerate(tasks):
            if x == 0:
                assert task.exception() is None
                assert task.result().url == urls[x]
                assert task.result().http_status == 200
                assert os.path.exists(task.result().filepath)
                assert task.result().write_success is True
            else:
                assert task.exception() is None
                assert task.result().url == urls[x]
                assert task.result().http_status == 404
                assert task.result().filepath is None
                assert task.result().write_success is False


@pytest.mark.asyncio
async def test_create_async_get_request_session_and_run_404_both():
    urls = [URL_404, URL_404]
    with tempfile.TemporaryDirectory() as tmpdirname:
        tasks = await create_async_get_request_session_and_run(urls, tmpdirname)
        for x, task in enumerate(tasks):
            assert task.exception() is None
            assert task.result().url == urls[x]
            assert task.result().http_status == 404
            assert task.result().filepath is None
            assert task.result().write_success is False
