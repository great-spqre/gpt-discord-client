from gtts import gTTS
from typing import List


__all__: List[str] = [
    '_create_tts_file'
]

# etc: you can use silero-tts module if you have a powerful device
def _create_tts_file(file_name: str, content: str, lang: str = 'en') -> None:

    gTTS(text=content, lang=lang).save(file_name)
