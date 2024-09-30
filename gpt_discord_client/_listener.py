"""
Copyright 2024 great-spqre

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from websocket import (
    WebSocket,
    create_connection
)

from json import (
    dumps,
    loads
)

from typing_extensions import (
    Union,
    Self,
    Dict,
    List,
)


__all__: List[str] = [
    '_websocket_listener'
]


class _websocket_listener:

    def __init__(self: Self, uri: str) -> None:

        self.uri: str = uri
        self.create_connection()

        super().__init__()
    
    def __del__(self: Self) -> None:

        self.ws.close()

    def send_server(self: Self, data: Union[Dict, str]) -> None:
        
        if isinstance(data, Dict):
            data: str = dumps(data)
        
        self.ws.send(data)

    def listen(self: Self, get_json: bool = True) -> Dict:

        data: str = self.ws.recv()

        if get_json:
            return loads(data)
        
        return data
    
    def create_connection(self: Self) -> None:

        self.ws: WebSocket = create_connection(self.uri)
