from ._gpt_discord_client  import *

from typing_extensions import (
    Self,
    Callable,
    Dict,
    List
)


__all__: List[str] = [
    'client'
]


class client(_gpt_discord_client):

    def __init__(self: Self, token: str, gpt_history_len: int = 4, gpt_style: str = '') -> None:

        self.token: str = token
        
        super().__init__(token, gpt_history_len, gpt_style)
    
    def event(self, func: Callable) -> Callable:

        def wrapper():
            for event in self.on_message():
                func(event)

        wrapper()