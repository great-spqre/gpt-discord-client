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

import random

from ._discord_voice_message_sender import *

from requests import (
    Response,
    get,
    post
)

from typing_extensions import (
    Self,
    Union,
    List,
    Dict
)


__all__: List[str] = [
    '_discord_http_client'
]


class _discord_http_client:

    def __init__(self: Self, token: str) -> None:

        self.token: str = token

        super().__init__()
    
    @property
    def auth_headers(self: Self) -> Dict:

        return {'Authorization': self.token, 'Content-type': 'application/json'}
    
    @property
    def client_id(self: Self) -> str:

        response: Response = get(
            url='https://discord.com/api/v9/users/@me',
            headers=self.auth_headers
        )

        return response.json()['id']
    
    @property
    def client_username(self: Self) -> str:

        response: Response = get(
            url='https://discord.com/api/v9/users/@me',
            headers=self.auth_headers
        )

        return response.json()['username']
    
    def reply_message(self: Self, channel_id: Union[str, int], guild_id: Union[str, int], message_id: Union[str, int], content: str, tts: bool = False) -> None:

        _: Response = post(
            url=f'https://discord.com/api/v9/channels/{channel_id}/messages',
            headers=self.auth_headers,
            json={
                "mobile_network_type": "unknown",
                "content": content,
                "nonce": f'{random.randint(1000000000000000000, 9999999999999999999)}',
                "tts": tts,
                "message_reference": {
                    "guild_id": guild_id,
                    "channel_id": channel_id,
                    "message_id": message_id
                },
                "flags":0
            }
        )

    def send_message(self: Self, channel_id: Union[str, int], content: str, tts: bool = False) -> None:

        _: Response = post(
            url=f'https://discord.com/api/v9/channels/{channel_id}/messages',
            headers=self.auth_headers,
            json={
                "mobile_network_type": "unknown",
                "content": content,
                "nonce": f'{random.randint(1000000000000000000, 9999999999999999999)}',
                "tts": tts,
                "flags": 0
            }
        )
    
    def send_voice_message(self: Self, file_path: str, channel_id: Union[str, int]) -> None:

        rep: List = _discord_voice_message_sender.get_url(file_path=file_path,
                                                          auth_headers=self.auth_headers,
                                                          channel_id=channel_id)
        _discord_voice_message_sender.upload_file(file_path=file_path, url=rep)
        _discord_voice_message_sender.send_voice_message(file_path=file_path,
                                                         auth_headers=self.auth_headers,
                                                         channel_id=channel_id,
                                                         url=rep)
    
    def reply_voice_message(self: Self, file_path: str, message_id: Union[str, int], channel_id: Union[str, int], guild_id: Union[str, int]) -> None:

        rep: List = _discord_voice_message_sender.get_url(file_path=file_path,
                                                          auth_headers=self.auth_headers,
                                                          channel_id=channel_id)
        _discord_voice_message_sender.upload_file(file_path=file_path, url=rep)
        _discord_voice_message_sender.reply_voice_message(file_path=file_path,
                                                         auth_headers=self.auth_headers,
                                                         message_id=message_id,
                                                         channel_id=channel_id,
                                                         guild_id=guild_id,
                                                         url=rep)
