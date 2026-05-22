#!/bin/bash
# 蓝鹰AI网关 - GPT-4o 调用示例
# BlueEagle AI Gateway - GPT-4o Example

# 设置API Key
API_KEY="${BLUEEAGLE_API_KEY:-YOUR_API_KEY_HERE}"

# API地址
BASE_URL="https://ahg.codes/v1"

echo "🚀 蓝鹰AI网关 - GPT-4o 调用示例"
echo "=================================="

# 调用GPT-4o
echo -e "\n📤 发送请求到 GPT-4o...\n"

response=$(curl -s -X POST "${BASE_URL}/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${API_KEY}" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "system", "content": "你是一个有帮助的AI助手，请用简洁的语言回答。"},
      {"role": "user", "content": "什么是API网关？它有什么作用？"}
    ],
    "temperature": 0.7,
    "max_tokens": 500
  }')

echo "📥 AI回复:"
echo "$response" | python3 -c "
import sys, json
data = json.load(sys.stdin)
if 'choices' in data:
    print(data['choices'][0]['message']['content'])
    print(f\"\\n📊 消耗Token: {data['usage']['total_tokens']}\")
elif 'error' in data:
    print(f\"❌ 错误: {data['error']['message']}\")
"

echo -e "\n✅ 请求完成!"
