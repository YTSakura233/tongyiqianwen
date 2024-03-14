"""
阿里云-通义千问VL模型
@author YTSakura
"""
from http import HTTPStatus
from time import time

import dashscope


def aliyun(path, question, module):
    dashscope.api_key = ""  # 请替换这里的apikey
    messages = [{
            'role': 'system',
            'content': [{
                'text': ''  # 请在这里输入调试命令
            }]
        }, {
            "role": "user",
            "content": [
                {"image": rf"{path}"},
                {"text": f"{question}"}
            ]
        }
    ]
    response = dashscope.MultiModalConversation.call(model=module,
                                                     messages=messages,
                                                     seed=time())
    if response.status_code == HTTPStatus.OK:
        print(response.output.choices[0].message.content[0].get('text'))
        return response.output.choices[0].message.content[0].get('text')
    else:
        print(response.code)
        print(response.message)
