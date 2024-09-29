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

import os

from ._tts import *
from ._discord_listener import *
from ._http_utils._gpt import *

from typing_extensions import (
    Self,
    Union,
    List
)


__all__: List[str] = [
    '_gpt_discord_client'
]


class _gpt_discord_client(_discord_listener):

    def __init__(self: Self, token: str, gpt_history_len: int = 4, gpt_style: str = ''):

        super().__init__(token)

        self._gpt_http_client: _gpt_http_client = _gpt_http_client(gpt_history_len, gpt_style)

        self.token = token

        self.start_heartbeat()

    def reply_with_gpt(self: Self, content: str, message_id: Union[str, int], channel_id: Union[str, int], guild_id: Union[str, int]) -> None:

        ans_from_gpt: str = self._gpt_http_client.response_to_gpt(content)[:2000]
        self._discord_http_client.reply_message(
            content=ans_from_gpt,
            message_id=message_id,
            channel_id=channel_id,
            guild_id=guild_id
        )

    def reply_with_voice_message(self: Self, content: str, message_id: Union[str, int], channel_id: Union[str, int], guild_id: Union[str, int], file_name: str = 'file.mp3', delete_after: bool = False, lang: str = 'en') -> None:

        _create_tts_file(file_name, content, lang=lang)

        self._discord_http_client.reply_voice_message(file_path=file_name,
                                                      message_id=message_id,
                                                      channel_id=channel_id,
                                                      guild_id=guild_id)
        
        if delete_after:

            os.remove(file_name)
