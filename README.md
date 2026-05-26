# 🦅 BlueEagle AI Gateway

<div align="center">

![Stars](https://img.shields.io/github/stars/blueeagle/blueeagle-gateway?style=flat-square)
![License](https://img.shields.io/github/license/blueeagle/blueeagle-gateway?style=flat-square)
![Price Ratio](https://img.shields.io/badge/Price%20Ratio-0.09x-brightgreen?style=flat-square)
![Recharge](https://img.shields.io/badge/Recharge-1%3A1-blue?style=flat-square)
![Native Pool](https://img.shields.io/badge/Native%20Pool-100%25%20Official-orange?style=flat-square)

**🚀 One Gateway, All AI — 统一API网关，极致性价比**

*全球顶尖大模型统一API网关 | 0.09x定价 | 1:1充值 | 原生官方号池*

[🌐 官网](https://ahg.codes) | [📖 快速开始](#-quick-start) | [🔥 支持模型](#-supported-models) | [💰 价格说明](#-pricing)

</div>

---

## 🎯 项目简介 | Project Overview

BlueEagle AI Gateway（蓝鹰AI网关）是一款**高性能、高可用、高性价比**的AI大模型统一API网关，为开发者提供一站式接入所有主流AI模型的能力。

### 核心优势 | Key Advantages

| 特性 | BlueEagle | 其他平台 |
|------|-----------|----------|
| 价格倍率 | **0.09x** (仅为官方9%) | 通常 0.15x ~ 0.3x |
| 充值比例 | **1:1** (1元=1美元额度) | 通常 1:0.6 ~ 1:0.8 |
| 额度有效期 | **永久有效不清零** | 通常有有效期限制 |
| 号池类型 | **100%原生官方** | 可能有共享/二手号 |
| 智能负载 | 多账号自动均衡 + 故障切换 | 单一账号 |

---

## ✨ 核心优势 | Core Features

- 🏆 **0.09x 超低价格** — 仅为官方定价的9%，极致性价比
- 💰 **1:1 充值比例** — 充1元人民币 = 1美元官方额度
- 🔐 **原生官方号池** — 100%官方账号，无掺假、无共享、无二次中转
- ⚡ **免费测试** — 注册即送测试额度，零风险体验
- 🔄 **智能负载均衡** — 多账号自动分配请求，毫秒级故障切换
- 🔧 **零代码迁移** — 完全兼容OpenAI接口规范，即接即用

---

## 🤖 支持模型 | Supported Models

| 模型 | 状态 | 说明 |
|------|------|------|
| OpenAI GPT-4o / GPT-4-turbo / GPT-3.5-turbo | ✅ 已支持 | 全系列GPT模型 |
| Anthropic Claude 3.5 Sonnet / Claude 3 Opus | ✅ 已支持 | 全系列Claude模型 |
| Google Gemini Pro / Gemini Ultra | ✅ 已支持 | 全系列Gemini模型 |
| Antigravity | ✅ 已支持 | 最新模型支持 |
| DeepSeek V3 / DeepSeek Coder | 🔜 即将支持 | 开发中 |
| Qwen 通义千问 | 🔜 即将支持 | 开发中 |
| Llama 3 / Llama 2 | 🔜 即将支持 | 开发中 |

---

## 🚀 快速开始 | Quick Start

### 1. 获取API Key

访问 [https://ahg.codes](https://ahg.codes) 注册并获取您的API Key

### 2. API调用示例 | Code Examples

#### 🌐 curl 调用示例

```bash
# OpenAI GPT-4o 调用
curl https://ahg.codes/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Hello, world!"}]
  }'

# Anthropic Claude 3.5 Sonnet 调用
curl https://ahg.codes/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "claude-3-5-sonnet-20240620",
    "messages": [{"role": "user", "content": "Hello, Claude!"}]
  }'
```

#### 🐍 Python 调用示例

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://ahg.codes/v1"  # 重要：使用蓝鹰网关地址
)

# GPT-4o 调用
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the meaning of life?"}
    ]
)
print(response.choices[0].message.content)

# Claude 3.5 Sonnet 调用
response = client.chat.completions.create(
    model="claude-3-5-sonnet-20240620",
    messages=[
        {"role": "user", "content": "Explain quantum computing in simple terms."}
    ]
)
print(response.choices[0].message.content)
```

#### 📦 Node.js 调用示例

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://ahg.codes/v1'  // 重要：使用蓝鹰网关地址
});

// GPT-4o 调用
async function chatWithGPT() {
  const response = await client.chat.completions.create({
    model: 'gpt-4o',
    messages: [
      { role: 'user', content: 'Hello, world!' }
    ]
  });
  console.log(response.choices[0].message.content);
}

// Claude 3.5 Sonnet 调用
async function chatWithClaude() {
  const response = await client.chat.completions.create({
    model: 'claude-3-5-sonnet-20240620',
    messages: [
      { role: 'user', content: 'What is AI?' }
    ]
  });
  console.log(response.choices[0].message.content);
}
```

---

## 💰 充值与计费 | Pricing

### 价格优势对比

| 充值比例 | 价格倍率 | 实际成本对比 |
|----------|----------|--------------|
| **BlueEagle: 1:1** | **0.09x** | 官价 × 9% = **官价的1折** |
| 其他平台A | 1:0.7 | 官价 × 0.21x = **官价的2.1折** |
| 其他平台B | 1:0.6 | 官价 × 0.18x = **官价的1.8折** |

### 计费示例

```
官方GPT-4o定价: $0.005/1K tokens (输入)
BlueEagle价格:   ¥0.005/1K tokens (输入)
                        ↓
实际成本: 仅为官方的 0.09倍 (9%)
```

### 计费特点

- ✅ **按量计费** — 用多少付多少，无最低消费
- ✅ **额度永久有效** — 充值额度不清零
- ✅ **透明定价** — 无隐藏费用

---

## ⚔️ 竞品对比 | Comparison

| 平台 | 价格倍率 | 充值比例 | 号池类型 | 额度有效期 | 免费额度 |
|------|----------|----------|----------|------------|----------|
| **BlueEagle** | **0.09x** | **1:1** | **原生官方** | **永久有效** | **✅ 有** |
| 平台A | 0.15x | 1:0.7 | 混合 | 1年 | ❌ 无 |
| 平台B | 0.2x | 1:0.6 | 共享 | 6个月 | ❌ 无 |
| 官方直连 | 1.0x | 1:7.2 | 原生官方 | 无限制 | $5 |

---

## 🔧 SDK兼容 | SDK Compatibility

BlueEagle 完全兼容 OpenAI Python SDK 和 Node.js SDK：

```bash
# Python SDK 安装
pip install openai

# Node.js SDK 安装
npm install openai
```

只需修改 `base_url` 为 `https://ahg.codes/v1`，即可零成本迁移！

---

## 📞 联系与支持 | Contact & Support

- 🌐 **官网**: [https://ahg.codes](https://ahg.codes)
- 📧 **商务合作**: 官网联系表单
- 📖 **使用文档**: 访问官网查看完整文档

---

## ⚠️ 免责声明 | Disclaimer

1. 本项目为 BlueEagle AI Gateway 的官方GitHub展示仓库
2. 所有API服务由 [https://ahg.codes](https://ahg.codes) 提供
3. 使用API服务即表示您同意服务提供商的使用条款
4. 价格信息可能随官方政策调整而变化，请以官网最新公告为准
5. 本项目不对第三方服务负责，使用前请自行评估风险

---

<div align="center">

**如果这个项目对您有帮助，请给我们一个 ⭐ Star！**

*Built with ❤️ by BlueEagle Team*

</div>
