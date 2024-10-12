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
