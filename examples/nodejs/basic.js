/**
 * 蓝鹰AI网关 - 基础对话示例
 * BlueEagle AI Gateway - Basic Chat Example
 */

import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY_HERE', // 替换为您的API Key
  baseURL: 'https://ahg.codes/v1' // 重要：使用蓝鹰网关地址
});

async function basicChat() {
  console.log('🚀 蓝鹰AI网关 - GPT-4o 基础对话示例\n');

  const response = await client.chat.completions.create({
    model: 'gpt-4o',
    messages: [
      { role: 'system', content: '你是一个有帮助的AI助手。' },
      { role: 'user', content: '请解释什么是API，并举一个实际的例子。' }
    ],
    temperature: 0.7,
    max_tokens: 500
  });

  console.log('📥 AI回复:');
  console.log(response.choices[0].message.content);
  console.log(`\n📊 消耗Token: ${response.usage.total_tokens}`);
}

async function multiTurnChat() {
  console.log('\n💬 多轮对话示例\n');

  const messages = [
    { role: 'system', content: '你是一位资深的技术顾问。' },
    { role: 'user', content: '我想学习人工智能，应该从哪里开始？' }
  ];

  const response = await client.chat.completions.create({
    model: 'gpt-4o',
    messages: messages,
    temperature: 0.7,
    max_tokens: 500
  });

  console.log('📥 AI回复:');
  console.log(response.choices[0].message.content);
}

basicChat()
  .then(() => multiTurnChat())
  .then(() => console.log('\n✅ 示例完成!'))
  .catch(console.error);
