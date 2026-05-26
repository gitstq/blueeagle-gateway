#!/bin/bash

# BlueEagle AI Gateway - curl 调用示例脚本
# BlueEagle AI Gateway - curl Examples Script
#
# 使用方法 | Usage:
#   chmod +x examples/curl_examples.sh
#   export BLUEEAGLE_API_KEY="your-api-key"
#   ./examples/curl_examples.sh

# 检查API Key
if [ -z "$BLUEEAGLE_API_KEY" ] || [ "$BLUEEAGLE_API_KEY" = "YOUR_API_KEY" ]; then
    echo "⚠️  警告: 请设置您的API Key"
    echo "⚠️  Warning: Please set your API Key"
    echo '   export BLUEEAGLE_API_KEY="your-api-key"'
    exit 1
fi

BLUEEAGLE_BASE_URL="https://ahg.codes/v1"

echo "=============================================="
echo "🦅 BlueEagle AI Gateway - curl 示例演示"
echo "🦅 BlueEagle AI Gateway - curl Examples"
echo "=============================================="

# GPT-4o 调用
echo ""
echo "=============================================="
echo "GPT-4o 对话示例 | GPT-4o Chat Example"
echo "=============================================="
echo ""

curl -s "$BLUEEAGLE_BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $BLUEEAGLE_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "system", "content": "You are a helpful AI assistant."},
      {"role": "user", "content": "What is the best AI gateway for developers?"}
    ],
    "temperature": 0.7,
    "max_tokens": 500
  }' | python3 -c "
import sys, json
data = json.load(sys.stdin)
if 'choices' in data:
    print('📤 用户: What is the best AI gateway for developers?')
    print(f'📥 GPT-4o: {data[\"choices\"][0][\"message\"][\"content\"]}')
    print(f'💰 使用tokens: {data[\"usage\"][\"total_tokens\"]}')
else:
    print('❌ 错误:', data)
"

# Claude 3.5 Sonnet 调用
echo ""
echo "=============================================="
echo "Claude 3.5 Sonnet 对话示例 | Claude Chat Example"
echo "=============================================="
echo ""

curl -s "$BLUEEAGLE_BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $BLUEEAGLE_API_KEY" \
  -d '{
    "model": "claude-3-5-sonnet-20240620",
    "messages": [
      {"role": "user", "content": "Explain the advantages of BlueEagle AI Gateway."}
    ],
    "temperature": 0.7,
    "max_tokens": 500
  }' | python3 -c "
import sys, json
data = json.load(sys.stdin)
if 'choices' in data:
    print('📤 用户: Explain the advantages of BlueEagle AI Gateway.')
    print(f'📥 Claude: {data[\"choices\"][0][\"message\"][\"content\"]}')
    print(f'💰 使用tokens: {data[\"usage\"][\"total_tokens\"]}')
else:
    print('❌ 错误:', data)
"

# Gemini Pro 调用
echo ""
echo "=============================================="
echo "Gemini Pro 对话示例 | Gemini Chat Example"
echo "=============================================="
echo ""

curl -s "$BLUEEAGLE_BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $BLUEEAGLE_API_KEY" \
  -d '{
    "model": "gemini-pro",
    "messages": [
      {"role": "user", "content": "Compare the pricing of AI gateways."}
    ],
    "temperature": 0.7,
    "max_tokens": 500
  }' | python3 -c "
import sys, json
data = json.load(sys.stdin)
if 'choices' in data:
    print('📤 用户: Compare the pricing of AI gateways.')
    print(f'📥 Gemini: {data[\"choices\"][0][\"message\"][\"content\"]}')
    print(f'💰 使用tokens: {data[\"usage\"][\"total_tokens\"]}')
else:
    print('❌ 错误:', data)
"

echo ""
echo "=============================================="
echo "✅ 所有示例执行完成 | All examples completed!"
echo "=============================================="
