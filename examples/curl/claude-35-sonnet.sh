#!/bin/bash
# 蓝鹰AI网关 - Claude 3.5 Sonnet 调用示例
# BlueEagle AI Gateway - Claude 3.5 Sonnet Example

# 设置API Key
API_KEY="${BLUEEAGLE_API_KEY:-YOUR_API_KEY_HERE}"

# API地址
BASE_URL="https://ahg.codes/v1"

echo "🧠 蓝鹰AI网关 - Claude 3.5 Sonnet 调用示例"
echo "=========================================="

# 调用Claude 3.5 Sonnet
echo -e "\n📤 发送请求到 Claude 3.5 Sonnet...\n"

response=$(curl -s -X POST "${BASE_URL}/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${API_KEY}" \
  -d '{
    "model": "claude-3-5-sonnet-20240620",
    "messages": [
      {"role": "user", "content": "请用三句话解释为什么Python是现代AI开发的首选语言。"}
    ],
    "max_tokens": 500,
    "temperature": 0.7
  }')

echo "📥 AI回复:"
echo "$response" | python3 -c "
import sys, json
data = json.load(sys.stdin)
if 'choices' in data:
    print(data['choices'][0]['message']['content'])
    if 'usage' in data:
        print(f\"\\n📊 消耗Token: {data['usage']['total_tokens']}\")
elif 'error' in data:
    print(f\"❌ 错误: {data['error']['message']}\")
"

echo -e "\n✅ 请求完成!"
