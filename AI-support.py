
from zhipuai import ZhipuAI  

class AIInterface:
    def __init__(self, apikey):
        self.client = ZhipuAI(apikey=apikey)

    def send_message(self, message):
        response = self.client.chat.completions.create(
            model="glm-4",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response['choices'][0]['message']['content']

# Example usage:
# ai = AIInterface('your_api_key')
# reply = ai.send_message("Hello")
# print(reply)
