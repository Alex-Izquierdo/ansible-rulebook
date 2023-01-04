#  Copyright 2022 Red Hat, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import asyncio
from typing import Any, Dict


async def main(queue: asyncio.Queue, args: Dict[str, Any]):
    delay = args.get("delay", 0)
    str_enable = args.get("str_enable", False)
    extra_payload = args.get("extra_payload", None)

    for i in range(int(args["limit"])):
        payload = {"i": f"{i}"} if str_enable else {"i": i}
        if extra_payload:
            payload.update({"extra_payload": extra_payload})
        await queue.put(payload)
        await asyncio.sleep(delay)


if __name__ == "__main__":

    class MockQueue:
        async def put(self, event):
            print(event)

    asyncio.run(main(MockQueue(), dict(limit=5)))
