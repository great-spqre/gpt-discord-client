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