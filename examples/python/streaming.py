"""
蓝鹰AI网关 - 流式输出示例
BlueEagle AI Gateway - Streaming Output Example
"""

from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY_HERE",  # 替换为您的API Key
    base_url="https://ahg.codes/v1"
)

def streaming_chat():
    """流式输出示例 - 实时显示AI回复"""
    print("💬 开始流式对话...\n")
    
    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": "请给我讲一个关于人工智能的短故事，大约200字。"}
        ],
        stream=True,  # 开启流式输出
        temperature=0.8
    )
    
    print("🤖 AI: ", end="", flush=True)
    
    full_response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)
            full_response += content
    
    print("\n\n✅ 流式输出完成!")
    print(f"📊 回复长度: {len(full_response)} 字符")

if __name__ == "__main__":
    streaming_chat()
