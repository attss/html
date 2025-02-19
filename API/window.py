import os
from openai import OpenAI

client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key="sk-c97ddcecdb034abf93eba386d3f7100c",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

completion = client.chat.completions.create(
    model="qwen-omni-turbo",
    messages=[
	{"role": "system",
         "content": [{"type":"text","text": "You are a helpful assistant."}]},
        {"role": "user",
         "content": [{"type": "image_url",
                    "image_url": {"url": "https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241022/emyrja/dog_and_girl.jpeg"},},
                    {"type": "text", "text": "图中描绘的是什么景象？"}]}],
    # 设置输出数据的模态，当前支持两种：["text","audio"]、["text"]
    modalities=["text","audio"],
    audio={"voice": "Cherry", "format": "wav"},
    # stream 必须设置为 True，否则会报错
    stream=True
    )

for chunk in completion:
    print(chunk.choices[0].delta)
https://attss.github.io/html/