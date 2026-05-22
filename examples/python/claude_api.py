"""
蓝鹰AI网关 - Claude API 兼容调用示例
BlueEagle AI Gateway - Claude API Compatible Example
"""

from anthropic import Anthropic

# 初始化客户端 - 通过蓝鹰网关使用Claude
client = Anthropic(
    api_key="YOUR_API_KEY_HERE",  # 替换为您的API Key
    base_url="https://ahg.codes/v1"  # 蓝鹰网关统一入口
)

def claude_chat():
    """Claude 3.5 Sonnet 对话示例"""
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "请用三句话解释量子计算的核心概念。"
            }
        ]
    )
    
    print("🧠 Claude 回复:")
    print(message.content[0].text)
    print(f"\n📊 消耗Token: {message.usage.input_tokens + message.usage.output_tokens}")

def claude_with_system():
    """Claude 带系统提示的示例"""
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        system="你是一位经验丰富的软件架构师，擅长设计可扩展的系统。",
        messages=[
            {
                "role": "user",
                "content": "如何设计一个高并发的消息队列系统？请给出关键设计要点。"
            }
        ]
    )
    
    print("🧠 Claude (架构师模式) 回复:")
    print(message.content[0].text)

if __name__ == "__main__":
    print("=" * 50)
    print("📌 Claude 基础对话")
    print("=" * 50)
    claude_chat()
    
    print("\n" + "=" * 50)
    print("📌 Claude 带系统提示")
    print("=" * 50)
    claude_with_system()
