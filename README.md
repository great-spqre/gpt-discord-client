<h1 align="center">
  <br>
  <img src="https://i.pinimg.com/originals/70/1b/b9/701bb938126e9f8bafc7241a2b2ff42f.jpg" width="400">
  <br>
  GPT (and TTS) Discord client bot
  <br>
</h1>

## Install lib
```sh
git clone https://github.com/great-spqre/gpt-discord-client.git
```

## Install python modules
```sh
cd gpt-discord-client
pip install -r requirments.txt
```

## Import and Auth
```python
import os

from gpt_discord_client import client
from dotenv import load_dotenv

load_dotenv()

client = client(os.getenv('token'))
```
