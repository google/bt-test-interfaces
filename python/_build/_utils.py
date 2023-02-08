# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Generated python gRPC helpers."""

import asyncio
import queue
import grpc

from typing import Any, Generic, Iterator, AsyncIterator, TypeVar


_T_co = TypeVar('_T_co', covariant=True)
_T = TypeVar('_T')


class Stream(Iterator[_T_co], grpc.RpcContext): ...


class AioStream(AsyncIterator[_T_co], grpc.RpcContext): ...


class Sender(Iterator[_T]):
    _inner: queue.Queue[_T]

    def __init__(self) -> None:
        self._inner = queue.Queue()

    def __iter__(self) -> Iterator[_T]:
        return self

    def __next__(self) -> _T:
        return self._inner.get()

    def send(self, item: _T) -> None:
        self._inner.put(item)


class AioSender(AsyncIterator[_T]):
    _inner: asyncio.Queue[_T]

    def __init__(self) -> None:
        self._inner = asyncio.Queue()

    def __iter__(self) -> AsyncIterator[_T]:
        return self

    async def __anext__(self) -> _T:
        return await self._inner.get()

    async def send(self, item: _T) -> None:
        await self._inner.put(item)

    def send_nowait(self, item: _T) -> None:
        self._inner.put_nowait(item)


class StreamStream(Generic[_T, _T_co], Iterator[_T_co], grpc.RpcContext):
    _sender: Sender[_T]
    _receiver: Stream[_T_co]

    def __init__(self, sender: Sender[_T], receiver: Stream[_T_co]) -> None:
        self._sender = sender
        self._receiver = receiver

    def send(self, item: _T) -> None:
        self._sender.send(item)

    def __iter__(self) -> Iterator[_T_co]:
        return self._receiver.__iter__()

    def __next__(self) -> _T_co:
        return self._receiver.__next__()

    def is_active(self) -> bool:
        return self._receiver.is_active()  # type: ignore

    def time_remaining(self) -> float:
        return self._receiver.time_remaining()  # type: ignore

    def cancel(self) -> None:
        self._receiver.cancel()  # type: ignore

    def add_callback(self, callback: Any) -> None:
        self._receiver.add_callback(callback)  # type: ignore


class AioStreamStream(Generic[_T, _T_co], AsyncIterator[_T_co], grpc.RpcContext):
    _sender: AioSender[_T]
    _receiver: AioStream[_T_co]

    def __init__(self, sender: AioSender[_T], receiver: AioStream[_T_co]) -> None:
        self._sender = sender
        self._receiver = receiver

    def __aiter__(self) -> AsyncIterator[_T_co]:
        return self._receiver.__aiter__()

    async def __anext__(self) -> _T_co:
        return await self._receiver.__aiter__().__anext__()

    async def send(self, item: _T) -> None:
        await self._sender.send(item)

    def send_nowait(self, item: _T) -> None:
        self._sender.send_nowait(item)

    def is_active(self) -> bool:
        return self._receiver.is_active()  # type: ignore

    def time_remaining(self) -> float:
        return self._receiver.time_remaining()  # type: ignore

    def cancel(self) -> None:
        self._receiver.cancel()  # type: ignore

    def add_callback(self, callback: Any) -> None:
        self._receiver.add_callback(callback)  # type: ignore
