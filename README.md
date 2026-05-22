# BlueEagle AI Gateway - 蓝鹰AI网关

<p align="center">
  <img src="https://ahg.codes/logo.png" alt="BlueEagle Logo" width="200"/>
</p>

<p align="center">
  <a href="https://github.com/blueeagleai/blueeagle-gateway/stargazers">
    <img src="https://img.shields.io/github/stars/blueeagleai/blueeagle-gateway?style=social" alt="Stars"/>
  </a>
  <a href="https://ahg.codes">
    <img src="https://img.shields.io/badge/Price-0.09x-brightgreen" alt="Price"/>
  </a>
  <a href="https://ahg.codes">
    <img src="https://img.shields.io/badge/Ratio-1:1-blue" alt="Ratio"/>
  </a>
  <a href="https://ahg.codes">
    <img src="https://img.shields.io/badge/Official-100%25%20Native-orange" alt="Official"/>
  </a>
</p>

<h1 align="center">
  🌟 One Gateway, All AI Models 🌟
</h1>

<h2 align="center">
  统一API网关 | 一站式接入全球顶尖AI
</h2>

<p align="center">
  <strong>0.09x Price, 100% Quality</strong><br/>
  <strong>极致性价比 · 100%原生官方号池</strong>
</p>

<p align="center">
  <a href="https://ahg.codes">🌐 Official Website</a> ·
  <a href="https://ahg.codes/register">📝 Get Free Credits</a> ·
  <a href="https://ahg.codes/docs">📚 Documentation</a>
</p>

---

## 📖 项目简介 | Project Introduction

**蓝鹰AI网关 (BlueEagle AI Gateway)** 是全球顶尖大模型统一API网关，为开发者提供一站式接入所有主流AI模型的能力。

只需一个API Key，即可调用 OpenAI GPT、Anthropic Claude、Google Gemini、Antigravity 等顶尖AI模型，享受 **0.09倍官方定价** 的极致性价比！

> 🔥 **核心亮点**：充值比例 1:1，消耗倍率仅 0.09x，用多少付多少，额度永久有效！

---

## ✨ 核心优势 | Key Advantages

| 优势 | 说明 |
|------|------|
| 🔥 **0.09x 超低倍率** | 仅为官方定价的9%，极致性价比 |
| 💰 **1:1 充值比例** | 充1元人民币 = 1美元官方额度 |
| 🛡️ **100% 原生号池** | 官方一手资源，无掺假、无共享、无二次中转 |
| ⚡ **智能负载均衡** | 多账号自动负载，毫秒级故障切换 |
| 🔄 **零代码迁移** | 完全兼容OpenAI接口规范，即接即用 |
| 🎁 **免费测试额度** | 注册即送测试额度，先体验再付费 |

---

## 📋 支持模型 | Supported Models

| 模型系列 | 模型名称 | 状态 |
|---------|---------|------|
| 🤖 **OpenAI** | GPT-4o, GPT-4 Turbo, GPT-4, GPT-3.5 Turbo | ✅ 已上线 |
| 🧠 **Anthropic** | Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Sonnet, Claude 3 Haiku | ✅ 已上线 |
| ✨ **Google** | Gemini Pro, Gemini Pro Vision, Gemini Ultra | ✅ 已上线 |
| 🚀 **Antigravity** | All models | ✅ 已上线 |
| 🔮 **DeepSeek** | DeepSeek Coder, DeepSeek Chat | 🚧 即将上线 |
| 🇨🇳 **通义千问** | Qwen Turbo, Qwen Plus, Qwen Max | 🚧 即将上线 |
| 🦙 **Llama 3** | Llama 3 70B, Llama 3 8B | 🚧 即将上线 |

---

## 🚀 快速开始 | Quick Start

### 1. 获取API Key

🔗 访问 [https://ahg.codes](https://ahg.codes) 注册账号，获取您的专属API Key

### 2. Python 示例 | Python Examples

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY_HERE",
    base_url="https://ahg.codes/v1"  # 重要：使用蓝鹰网关地址
)

# 调用 GPT-4o
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, explain quantum computing in simple terms."}
    ],
    temperature=0.7,
    max_tokens=500
)

print(response.choices[0].message.content)
```

### 3. cURL 示例 | cURL Examples

```bash
# GPT-4o 调用
curl https://ahg.codes/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY_HERE" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "temperature": 0.7,
    "max_tokens": 500
  }'

# Claude 3.5 Sonnet 调用
curl https://ahg.codes/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY_HERE" \
  -d '{
    "model": "claude-3-5-sonnet-20240620",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ]
  }'
```

### 4. Node.js 示例 | Node.js Examples

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY_HERE',
  baseURL: 'https://ahg.codes/v1'  // 重要：使用蓝鹰网关地址
});

// 调用 GPT-4o
async function main() {
  const response = await client.chat.completions.create({
    model: 'gpt-4o',
    messages: [
      { role: 'user', content: 'Hello!' }
    ],
    temperature: 0.7,
    max_tokens: 500
  });
  
  console.log(response.choices[0].message.content);
}

main();
```

### 5. Claude API 兼容调用 | Claude API Compatible

```python
from anthropic import Anthropic

client = Anthropic(
    api_key="YOUR_API_KEY_HERE",
    base_url="https://ahg.codes/v1"  # 蓝鹰网关统一入口
)

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

print(message.content)
```

---

## 💰 充值与计费 | Pricing & Billing

### 价格对比 | Price Comparison

| 服务商 | 充值比例 | 消耗倍率 | 实际成本 |
|--------|---------|---------|---------|
| **蓝鹰AI网关** | **1:1** | **0.09x** | **仅需9%** |
| OpenAI 官方 | 7.2:1 (美元) | 1x | 100% |
| 其他中转 | 1:1 | 0.5x~1.5x | 不稳定 |

### 计费示例 | Billing Examples

```
📊 GPT-4o 输入成本计算：

官方定价：$0.005 / 1K tokens
蓝鹰定价：$0.005 × 0.09 = $0.00045 / 1K tokens

节省比例：91% ❗

📊 以100万tokens为例：
官方费用：$5.00
蓝鹰费用：$0.45 (仅需0.45美元！)
```

### 计费特点

- ✅ **按量计费**：用多少付多少，无最低消费
- ✅ **额度永久有效**：不清零、不过期
- ✅ **实时账单**：透明消费，随时查询

---

## ⚔️ 竞品对比 | Comparison

| 功能 | 蓝鹰AI网关 | 其他中转 | 官方API |
|------|----------|---------|--------|
| **原生号池** | ✅ 100%官方一手 | ❌ 共享/二手 | ✅ |
| **价格倍率** | **0.09x** | 0.5x~1.5x | 1x |
| **充值比例** | **1:1** | 不稳定 | 7.2:1 |
| **故障切换** | ✅ 毫秒级自动 | ❌ 手动 | ✅ |
| **负载均衡** | ✅ 智能多账号 | ❌ 无 | ❌ |
| **接口兼容** | ✅ 100%兼容 | ⚠️ 部分兼容 | ✅ |
| **免费额度** | ✅ 注册即送 | ❌ 无 | ❌ |

---

## 🔧 高级功能 | Advanced Features

### 智能负载均衡 | Smart Load Balancing

```python
# 开启智能负载均衡（自动分配请求到多个账号）
client = OpenAI(
    api_key="YOUR_API_KEY_HERE",
    base_url="https://ahg.codes/v1",
    max_retries=3,  # 自动重试
    timeout=60      # 超时设置
)
```

### 模型列表查询 | List Models

```bash
curl https://ahg.codes/v1/models \
  -H "Authorization: Bearer YOUR_API_KEY_HERE"
```

### Embeddings 支持 | Embeddings API

```python
response = client.embeddings.create(
    model="text-embedding-3-large",
    input="The quick brown fox jumps over the lazy dog"
)
print(response.data[0].embedding)
```

---

## 📞 联系与支持 | Contact & Support

| 渠道 | 链接 |
|------|------|
| 🌐 **官方网站** | [https://ahg.codes](https://ahg.codes) |
| 📧 **商务合作** | contact@ahg.codes |
| 💬 **技术交流** | [Discord社区](https://discord.gg/ahg) |
| 📖 **开发文档** | [文档中心](https://ahg.codes/docs) |
| 🐛 **问题反馈** | [GitHub Issues](https://github.com/blueeagleai/blueeagle-gateway/issues) |

---

## ⚠️ 免责声明 | Disclaimer

1. 本项目仅作为蓝鹰AI网关的官方宣传与文档仓库
2. 蓝鹰AI网关不对第三方修改或使用本项目代码导致的任何问题负责
3. 请遵守各AI服务提供商的使用条款和政策
4. 价格信息以官网实时更新为准
5. 本项目不提供任何付费服务的中介或代理

---

## 📄 License

MIT License - 详见 [LICENSE](LICENSE) 文件

---

<p align="center">
  <strong>Made with ❤️ by BlueEagle AI Team</strong><br/>
  <a href="https://ahg.codes">🌐 https://ahg.codes</a>
</p>

<p align="center">
  ⭐ 如果这个项目对你有帮助，请给我们一个Star！⭐
</p>
