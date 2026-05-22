#!/bin/bash
# 蓝鹰AI网关 - 查询可用模型列表
# BlueEagle AI Gateway - List Available Models

# 设置API Key
API_KEY="${BLUEEAGLE_API_KEY:-YOUR_API_KEY_HERE}"

# API地址
BASE_URL="https://ahg.codes/v1"

echo "📋 蓝鹰AI网关 - 可用模型列表"
echo "=============================="

echo -e "\n📤 查询可用模型...\n"

response=$(curl -s -X GET "${BASE_URL}/models" \
  -H "Authorization: Bearer ${API_KEY}")

echo "📥 模型列表:"
echo "$response" | python3 -c "
import sys, json
data = json.load(sys.stdin)
if 'data' in data:
    models = data['data']
    print(f'共 {len(models)} 个模型可用:\\n')
    for model in models:
        model_id = model.get('id', 'N/A')
        owned_by = model.get('owned_by', 'N/A')
        print(f'  🤖 {model_id}')
elif 'error' in data:
    print(f'❌ 错误: {data[\"error\"][\"message\"]}')"
