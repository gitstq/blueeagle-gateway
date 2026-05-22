"""
蓝鹰AI网关 - GPT-4o 基础对话示例
BlueEagle AI Gateway - GPT-4o Basic Chat Example
"""

from openai import OpenAI

# 初始化客户端
client = OpenAI(
    api_key="YOUR_API_KEY_HERE",  # 替换为您的API Key
    base_url="https://ahg.codes/v1"  # 重要：使用蓝鹰网关地址
)

def basic_chat():
    """基础对话示例"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "你是一个有帮助的AI助手。"},
            {"role": "user", "content": "请用简单的语言解释什么是机器学习。"}
        ],
        temperature=0.7,
        max_tokens=500
    )
    
    print("🤖 AI回复:")
    print(response.choices[0].message.content)
    print(f"\n📊 消耗Token: {response.usage.total_tokens}")

def multi_turn_chat():
    """多轮对话示例"""
    messages = [
        {"role": "system", "content": "你是一个专业的Python编程导师。"},
        {"role": "user", "content": "什么是装饰器？"},
    ]
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )
    
    assistant_reply = response.choices[0].message.content
    print("🤖 AI回复:", assistant_reply)
    
    # 添加AI回复到对话历史
    messages.append({"role": "assistant", "content": assistant_reply})
    messages.append({"role": "user", "content": "能给我一个实际的例子吗？"})
    
    # 继续对话
    response2 = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )
    
    print("\n🤖 AI继续回复:")
    print(response2.choices[0].message.content)

if __name__ == "__main__":
    print("=" * 50)
    print("📌 基础对话示例")
    print("=" * 50)
    basic_chat()
    
    print("\n" + "=" * 50)
    print("📌 多轮对话示例")
    print("=" * 50)
    multi_turn_chat()
