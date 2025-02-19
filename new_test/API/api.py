import os
from openai import OpenAI

client = OpenAI(
        api_key="sk-c97ddcecdb034abf93eba386d3f7100c",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

completion = client.chat.completions.create(
    model="qwen-omni-turbo",
    messages=[
    {
        "role": "user",
        "content": "你的名字是什么"
    }
],
    # 设置输出数据的模态，当前支持两种：["text","audio"]、["text"]
    modalities=["text","audio"],
    audio={"voice": "Cherry", "format": "wav"},
    # stream 必须设置为 True，否则会报错
    stream=True
    )

for chunk in completion:
    print(chunk.choices[0].delta)