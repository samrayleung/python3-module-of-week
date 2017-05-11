import asyncio
import functools


def set_event(event):
    print('setting event in callback')
    event.set()


async def coro1(event):
    print('corol waiting for event')
    await event.wait()
    print('corol triggred')


async def coro2(event):
    print('coro2 waiting for event')
    await event.wait()
    print('coro2 triggred')


async def main(loop):
    # Create a shared event
    event = asyncio.Event()
    print('event start state:{}')

    loop.call_later(
        0.1, functools.partial(set_event, event)
    )
    await asyncio.wait([coro1(event), coro2(event)])
    print('event end state: {}'.format(event.is_set()))

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()