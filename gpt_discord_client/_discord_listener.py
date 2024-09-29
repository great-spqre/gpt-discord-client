import time
import threading
import websocket

from ._http_utils._discord import *
from ._listener import *

from typing_extensions import (
    Generator,
    Self,
    Dict,
    List
)


__all__: List[str] = [
    '_discord_listener'
]


class _discord_exception(Exception):
    pass


class _discord_listener(_websocket_listener):

    def __init__(self: Self, token: str) -> None:
        
        uri: str = 'wss://gateway.discord.gg/?v=6&encording=json'
        super().__init__(uri)

        self._discord_http_client: _discord_http_client = _discord_http_client(token=token)
    
    def heartbeat(self: Self, interval: float) -> None:

        heartbeatJSON: Dict = {
                    "op": 1, 
                    "d": "null"
        }

        while True:

            self.send_server(heartbeatJSON)
            time.sleep(interval)
    
    def start_heartbeat(self: Self) -> None:

        event: Dict = self.listen()
        heartbeat_interval: float = event['d']['heartbeat_interval'] / 1000

        threading.Thread(target=self.heartbeat, args=[heartbeat_interval]).start()

        try:

            self.send_server({
                "op": 2,
                "d": {
                    "token": self._discord_http_client.token,
                    "properties": {
                        "$os": "linux",
                        "$browser": "chrome",
                        "$device": "pc"
                    }
                }
            })
        
        except websocket._exceptions.WebSocketConnectionClosedException:

            raise _discord_exception('invalid token')
        
        print(f'Succsefully connected as @{self._discord_http_client.client_username}\n')
    
    def on_message(self: Self) -> Generator[Dict, None, None]:

        while True:

            event: Dict = self.listen()
            yield event