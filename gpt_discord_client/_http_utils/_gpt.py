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

import re

from requests import (
    Response,
    post
)

from typing_extensions import (
    Self,
    Optional,
    List,
    Dict
)


__all__: List[str] = [
    '_gpt_http_client'
]


class _gpt_http_client_exception(Exception):
    pass


class _gpt_http_client:

    def __init__(self: Self, history_len: int = 4, gpt_style: str = '') -> None:

        self.history: List[Optional[Dict]] = []
        self.history_len: int = history_len
        self.gpt_style: str = gpt_style

        super().__init__()
    
    def clear_history(self: Self) -> None:

        self.history: List[Optional[Dict]] = []
    
    def cut_history(self: Self) -> None:

        self.history: List[Dict] = self.history[:-2]

    def response_to_gpt(self: Self, content: str) -> str:

        local_history: List[Optional[Dict]] = []

        if len(local_history) == 0:

            local_history.append({'content': self.gpt_style + '\n' + content, 'role': 'user'})
        
        else:

            local_history.append({'content': content, 'role': 'user'})

        response: Response = post(
            url='https://www.blackbox.ai/api/chat',
            json={
                "messages": local_history,
                "previewToken":None,
                "userId":None,
                "codeModelMode":True,
                "agentMode":{},
                "trendingAgentMode":{},
                "isMicMode":False,
                "userSystemPrompt":None,
                "maxTokens":1024,
                "playgroundTopP":0.9,
                "playgroundTemperature":0.5,
                "isChromeExt":False,
                "githubToken":None,
                "clickedAnswer2":False,
                "clickedAnswer3":False,
                "clickedForceWebSearch":False,
                "visitFromDelta":False,
                "mobileClient":False,
                "userSelectedModel":None
            }
        )

        if not response.text:

            raise _gpt_http_client_exception('gpt empty answer error')

        local_history.append({'content': response.text, 'role': 'assistant'})

        if len(local_history) > self.history_len:
            local_history = local_history[2:]
            local_history[0]['content'] = self.gpt_style + '\n' + local_history[0]['content']

        self.history: List[Dict] = local_history

        start_index: int = response.text.find("$~~~$")

        if start_index != -1:

            print(response.text)

            return re.sub(r'\$~~~\$(.*?)\$~~~\$', '', re.sub(r'\$@\$(.*?)\$@\$', '', response.text[start_index:]))
        
        else:

            return re.sub(r'\$@\$(.*?)\$@\$', '', response.text)
