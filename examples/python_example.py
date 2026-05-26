"""
BlueEagle AI Gateway - Python 示例代码
Python Example Code for BlueEagle AI Gateway

安装依赖 | Install dependencies:
    pip install openai

使用方法 | Usage:
    1. 设置环境变量 export BLUEEAGLE_API_KEY="your-api-key"
    2. 运行脚本 python examples/python_example.py
"""

import os
from openai import OpenAI

# 初始化客户端
# Initialize the client
client = OpenAI(
    api_key=os.environ.get("BLUEEAGLE_API_KEY", "YOUR_API_KEY"),
    base_url="https://ahg.codes/v1"  # 重要：使用蓝鹰网关地址
)


def chat_with_gpt():
    """GPT-4o 对话示例"""
    print("=" * 50)
    print("GPT-4o 对话示例 | GPT-4o Chat Example")
    print("=" * 50)
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": "Explain the concept of API gateway in simple terms."}
        ],
        temperature=0.7,
        max_tokens=500
    )
    
    print(f"\n📤 用户: Explain the concept of API gateway in simple terms.")
    print(f"\n📥 GPT-4o: {response.choices[0].message.content}")
    print(f"\n💰 使用tokens: {response.usage.total_tokens}")


def chat_with_claude():
    """Claude 3.5 Sonnet 对话示例"""
    print("\n" + "=" * 50)
    print("Claude 3.5 Sonnet 对话示例 | Claude Chat Example")
    print("=" * 50)
    
    response = client.chat.completions.create(
        model="claude-3-5-sonnet-20240620",
        messages=[
            {"role": "user", "content": "What are the benefits of using an AI gateway?"}
        ],
        temperature=0.7,
        max_tokens=500
    )
    
    print(f"\n📤 用户: What are the benefits of using an AI gateway?")
    print(f"\n📥 Claude: {response.choices[0].message.content}")
    print(f"\n💰 使用tokens: {response.usage.total_tokens}")


def chat_with_gemini():
    """Gemini Pro 对话示例"""
    print("\n" + "=" * 50)
    print("Gemini Pro 对话示例 | Gemini Chat Example")
    print("=" * 50)
    
    response = client.chat.completions.create(
        model="gemini-pro",
        messages=[
            {"role": "user", "content": "Compare GPT-4 and Claude in terms of their strengths."}
        ],
        temperature=0.7,
        max_tokens=500
    )
    
    print(f"\n📤 用户: Compare GPT-4 and Claude in terms of their strengths.")
    print(f"\n📥 Gemini: {response.choices[0].message.content}")
    print(f"\n💰 使用tokens: {response.usage.total_tokens}")


def streaming_example():
    """流式输出示例 | Streaming Example"""
    print("\n" + "=" * 50)
    print("流式输出示例 | Streaming Example")
    print("=" * 50)
    
    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": "Count to 5 and explain each number."}
        ],
        stream=True,
        max_tokens=200
    )
    
    print(f"\n📤 用户: Count to 5 and explain each number.")
    print(f"\n📥 回复: ", end="")
    
    full_response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)
            full_response += content
    
    print("\n")


def main():
    """主函数 | Main Function"""
    print("\n" + "=" * 60)
    print("🦅 BlueEagle AI Gateway - Python 示例演示")
    print("🦅 BlueEagle AI Gateway - Python Demo")
    print("=" * 60)
    
    # 检查API Key
    api_key = os.environ.get("BLUEEAGLE_API_KEY")
    if not api_key or api_key == "YOUR_API_KEY":
        print("\n⚠️  警告: 请设置您的API Key")
        print("⚠️  Warning: Please set your API Key")
        print("   export BLUEEAGLE_API_KEY='your-api-key'\n")
    
    try:
        # 运行示例
        chat_with_gpt()
        chat_with_claude()
        chat_with_gemini()
        streaming_example()
        
        print("\n✅ 所有示例执行完成 | All examples completed!")
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
