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

from gtts import gTTS
from typing import List


__all__: List[str] = [
    '_create_tts_file'
]

# etc: you can use silero-tts module if you have a powerful device
def _create_tts_file(file_name: str, content: str, lang: str = 'en') -> None:

    gTTS(text=content, lang=lang).save(file_name)
