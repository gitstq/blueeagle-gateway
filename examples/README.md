# BlueEagle AI Gateway Examples

本目录包含蓝鹰AI网关的各种调用示例。

## 📁 目录结构

```
examples/
├── python/          # Python 示例
│   ├── basic_chat.py
│   ├── streaming.py
│   ├── claude_api.py
│   └── embeddings.py
├── curl/            # cURL 示例
│   ├── gpt-4o.sh
│   ├── claude-35-sonnet.sh
│   └── models.sh
└── nodejs/          # Node.js 示例
    ├── basic.js
    ├── streaming.mjs
    └── claude.mjs
```

## 🚀 快速使用

### 1. 设置环境变量

```bash
export BLUEEAGLE_API_KEY="your-api-key-here"
```

### 2. 运行示例

```bash
# Python 示例
python examples/python/basic_chat.py

# cURL 示例
bash examples/curl/gpt-4o.sh

# Node.js 示例
node examples/nodejs/basic.js
```

## 📝 获取 API Key

访问 [https://ahg.codes](https://ahg.codes) 注册并获取API Key

## ⚠️ 注意事项

- 所有请求的 `base_url` 必须设置为 `https://ahg.codes/v1`
- 请妥善保管您的API Key，不要泄露给他人
