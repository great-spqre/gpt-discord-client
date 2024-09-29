import os

from ._voice_message_utils import *

from requests import (
    Response,
    post,
    put
)

from typing_extensions import (
    Union,
    Dict,
    List
)


__all__: List[str] = [
    '_discord_voice_message_sender'
]


class _voice_message_exception(Exception):
    pass


class _discord_voice_message_sender:
    
    @staticmethod
    def get_url(file_path: str, auth_headers: Dict, channel_id: Union[int, str]) -> List:

        with open(file_path, 'rb') as file:

            file.seek(0, os.SEEK_END)
            
            response: Response = post(
                url=f'https://discord.com/api/v9/channels/{channel_id}/attachments',
                headers=auth_headers,
                json={
                    "files": [{
                        "filename": os.path.basename(file.name),
                        "file_size": file.tell(),
                        "id": "261"
                    }]
                }
            )

            if 'attachments' not in response.json():
                raise _voice_message_exception(f'There aren`t any attachments in {response.json()}')
            
            return response.json()['attachments']
    
    @staticmethod
    def upload_file(file_path: str, url: List) -> None:

        with open(file_path, 'rb') as file:

            _: Response = put(
                url=url[0]['upload_url'],
                headers={
                    'authority': 'discord-attachments-uploads-prd.storage.googleapis.com',
                    'content-type': 'audio/ogg'
                },
                data=file.read()
            )
    
    @staticmethod
    def send_voice_message(file_path: str, auth_headers: Dict, channel_id: Union[int, str], url: List) -> None:

        with open(file_path, 'rb') as file:

            file.seek(0, os.SEEK_END)

            _: Response = post(
                url=f'https://discord.com/api/v9/channels/{channel_id}/messages',
                headers=auth_headers,
                json={
                    "content": "",
                    "channel_id": channel_id,
                    "type": 0,
                    "sticker_ids": [],
                    "attachments": [{
                        "content_type": "audio/ogg",
                        "duration_secs": _voice_message_utils.audio_duration(file_path),
                        "filename": "voice-message.ogg",
                        "id": channel_id,
                        "size": 4096,
                        "uploaded_filename": url[0]['upload_filename'],
                        "waveform": _voice_message_utils.encode_to_b64(_voice_message_utils.generate_waveform()),
                        "spoiler": False,
                        "sensitive": False
                }],
                "flags": 8192,
                }
            )
    
    @staticmethod
    def reply_voice_message(file_path: str, auth_headers: Dict, message_id: Union[int, str], channel_id: Union[int, str], guild_id: Union[int, str], url: List) -> None:

        with open(file_path, 'rb') as file:

            file.seek(0, os.SEEK_END)

            _: Response = post(
                url=f'https://discord.com/api/v9/channels/{channel_id}/messages',
                headers=auth_headers,
                json={
                    "content": "",
                    "message_reference": {
                        "guild_id": guild_id,
                        "channel_id": channel_id,
                        "message_id": message_id
                    },
                    "channel_id": channel_id,
                    "type": 0,
                    "sticker_ids": [],
                    "attachments": [{
                        "content_type": "audio/ogg",
                        "duration_secs": _voice_message_utils.audio_duration(file_path),
                        "filename": "voice-message.ogg",
                        "id": channel_id,
                        "size": 4096,
                        "uploaded_filename": url[0]['upload_filename'],
                        "waveform": _voice_message_utils.encode_to_b64(_voice_message_utils.generate_waveform()),
                        "spoiler": False,
                        "sensitive": False
                }],
                "flags": 8192,
                }
            )