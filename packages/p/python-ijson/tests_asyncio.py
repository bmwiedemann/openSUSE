# -*- coding:utf-8 -*-

import asyncio
import io

from ijson import compat


class AsyncReader(object):
    def __init__(self, data):
        if type(data) == compat.bytetype:
            self.data = io.BytesIO(data)
        else:
            self.data = io.StringIO(data)

    async def read(self, n=-1):
        return self.data.read(n)

class Async(object):
    '''Test adaptation for async generators'''

    suffix = '_async'

    def _run(self, f):
        loop = asyncio.new_event_loop()
        try:
            loop.run_until_complete(f)
        finally:
            loop.close()

    def all(self, routine, json_content, *args, **kwargs):
        events = []
        async def run():
            async for event in routine(AsyncReader(json_content), *args, **kwargs):
                events.append(event)
        self._run(run())
        return events

    def first(self, routine, json_content, *args, **kwargs):
        events = []
        async def run():
            async for event in routine(AsyncReader(json_content), *args, **kwargs):
                events.append(event)
                if events:
                    return
        self._run(run())
        return events[0]