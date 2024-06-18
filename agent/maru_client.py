import requests
import json

class Maru:

    model = "maru-black"

    def __init__(self, model):
        self.model = model

    def get_LLM_result(self, message):
        LLM_chat_API_url = "http://maru-llm-inf.devel.kakao.com/v1/chat/completions"
        headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
        LLM_params = {
            "model": self.model,
            "messages": message,
            "max_tokens": 50,
            "temperature": 0.1,
            "stream": True
        }

        response = requests.post(url=LLM_chat_API_url, data=json.dumps(LLM_params), headers=headers)
        stream_out = []
        for object_str in response.text.split("\n\n"):
            if object_str != '':
                stream_obj = json.loads(object_str)
                choices = stream_obj['choices'][0]
                if "delta" in choices.keys():
                    delta = choices['delta']
                    if "content" in delta.keys():
                        print(delta['content'])
                        stream_out.append(MaruStreamObject(msg=delta['content']))

        return stream_out


class MaruStreamObject:
    delta = ""
    def __init__(self, msg):
        self.delta = msg