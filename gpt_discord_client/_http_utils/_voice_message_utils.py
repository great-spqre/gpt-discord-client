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
import re
import base64
import math

from mutagen.mp3 import MP3

from typing_extensions import List


__all__: List[str] = [
    '_voice_message_utils'
]


class _voice_message_utils:

    @staticmethod
    def generate_waveform(length: int = 64) -> str:

        characters: str = " !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~Çüéâäàå"
        random_string: str = ''.join(random.choice(characters) for _ in range(length))
        return random_string
    
    @staticmethod
    def clean_string(string: str) -> str:

        cleaned_string: str = re.sub(r'[^a-zA-Z0-9\s]', '', string)
        return cleaned_string
    
    @staticmethod
    def encode_to_b64(string: str) -> str:

        encoded_bytes = base64.b64encode(string.encode('utf-8'))
        encoded_string = encoded_bytes.decode('utf-8')
        return encoded_string
    
    @staticmethod
    def audio_duration(file_path: str) -> float:

        audio = MP3(file_path)
        return math.floor(audio.info.length * 10) / 10
