import os.path
import urllib.parse

from collections import namedtuple

import aiohttp
import asyncio

from fdiff.aio import async_write_bin


def _get_filepath_from_url(url, dirpath):
    url_path_list = urllib.parse.urlsplit(url)
    abs_filepath = url_path_list.path
    basepath = os.path.split(abs_filepath)[-1]
    return os.path.join(dirpath, basepath)


async def async_fetch(session, url):
    async with session.get(url) as response:
        status = response.status
        if status != 200:
            binary = None
        else:
            binary = await response.read()
        return url, status, binary


async def async_fetch_and_write(session, url, dirpath):
    FWResponse = namedtuple(
        "FWRes", ["url", "filepath", "http_status", "write_success"]
    )
    url, status, binary = await async_fetch(session, url)
    if status != 200:
        filepath = None
        write_success = False
    else:
        filepath = _get_filepath_from_url(url, dirpath)
        await async_write_bin(filepath, binary)
        write_success = True

    return FWResponse(
        url=url, filepath=filepath, http_status=status, write_success=write_success
    )


async def create_async_get_request_session_and_run(urls, dirpath):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            # use asyncio.ensure_future instead of .run() here to maintain
            # Py3.6 compatibility
            task = asyncio.ensure_future(async_fetch_and_write(session, url, dirpath))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)
        return tasks
