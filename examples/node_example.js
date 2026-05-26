/**
 * BlueEagle AI Gateway - Node.js 示例代码
 * Node.js Example Code for BlueEagle AI Gateway
 * 
 * 安装依赖 | Install dependencies:
 *     npm install openai
 * 
 * 使用方法 | Usage:
 *     1. 设置环境变量 export BLUEEAGLE_API_KEY="your-api-key"
 *     2. 运行脚本 node examples/node_example.js
 */

import OpenAI from 'openai';

// 初始化客户端
// Initialize the client
const client = new OpenAI({
  apiKey: process.env.BLUEEAGLE_API_KEY || 'YOUR_API_KEY',
  baseURL: 'https://ahg.codes/v1' // 重要：使用蓝鹰网关地址
});

/**
 * GPT-4o 对话示例
 * GPT-4o Chat Example
 */
async function chatWithGPT() {
  console.log('\n' + '='.repeat(50));
  console.log('GPT-4o 对话示例 | GPT-4o Chat Example');
  console.log('='.repeat(50));

  const response = await client.chat.completions.create({
    model: 'gpt-4o',
    messages: [
      { role: 'system', content: 'You are a helpful AI assistant.' },
      { role: 'user', content: 'Explain the concept of API gateway in simple terms.' }
    ],
    temperature: 0.7,
    max_tokens: 500
  });

  console.log('\n📤 用户: Explain the concept of API gateway in simple terms.');
  console.log(`\n📥 GPT-4o: ${response.choices[0].message.content}`);
  console.log(`\n💰 使用tokens: ${response.usage.total_tokens}`);
}

/**
 * Claude 3.5 Sonnet 对话示例
 * Claude 3.5 Sonnet Chat Example
 */
async function chatWithClaude() {
  console.log('\n' + '='.repeat(50));
  console.log('Claude 3.5 Sonnet 对话示例 | Claude Chat Example');
  console.log('='.repeat(50));

  const response = await client.chat.completions.create({
    model: 'claude-3-5-sonnet-20240620',
    messages: [
      { role: 'user', content: 'What are the benefits of using an AI gateway?' }
    ],
    temperature: 0.7,
    max_tokens: 500
  });

  console.log('\n📤 用户: What are the benefits of using an AI gateway?');
  console.log(`\n📥 Claude: ${response.choices[0].message.content}`);
  console.log(`\n💰 使用tokens: ${response.usage.total_tokens}`);
}

/**
 * Gemini Pro 对话示例
 * Gemini Pro Chat Example
 */
async function chatWithGemini() {
  console.log('\n' + '='.repeat(50));
  console.log('Gemini Pro 对话示例 | Gemini Chat Example');
  console.log('='.repeat(50));

  const response = await client.chat.completions.create({
    model: 'gemini-pro',
    messages: [
      { role: 'user', content: 'Compare GPT-4 and Claude in terms of their strengths.' }
    ],
    temperature: 0.7,
    max_tokens: 500
  });

  console.log('\n📤 用户: Compare GPT-4 and Claude in terms of their strengths.');
  console.log(`\n📥 Gemini: ${response.choices[0].message.content}`);
  console.log(`\n💰 使用tokens: ${response.usage.total_tokens}`);
}

/**
 * 流式输出示例
 * Streaming Example
 */
async function streamingExample() {
  console.log('\n' + '='.repeat(50));
  console.log('流式输出示例 | Streaming Example');
  console.log('='.repeat(50));

  const stream = await client.chat.completions.create({
    model: 'gpt-4o',
    messages: [
      { role: 'user', content: 'Count to 5 and explain each number.' }
    ],
    stream: true,
    max_tokens: 200
  });

  console.log('\n📤 用户: Count to 5 and explain each number.');
  console.log('\n📥 回复: ');

  let fullResponse = '';
  for await (const chunk of stream) {
    if (chunk.choices[0].delta.content) {
      const content = chunk.choices[0].delta.content;
      process.stdout.write(content);
      fullResponse += content;
    }
  }
  console.log('\n');
}

/**
 * 主函数
 * Main Function
 */
async function main() {
  console.log('\n' + '='.repeat(60));
  console.log('🦅 BlueEagle AI Gateway - Node.js 示例演示');
  console.log('🦅 BlueEagle AI Gateway - Node.js Demo');
  console.log('='.repeat(60));

  // 检查API Key
  const apiKey = process.env.BLUEEAGLE_API_KEY;
  if (!apiKey || apiKey === 'YOUR_API_KEY') {
    console.log('\n⚠️  警告: 请设置您的API Key');
    console.log('⚠️  Warning: Please set your API Key');
    console.log('   export BLUEEAGLE_API_KEY="your-api-key"\n');
  }

  try {
    // 运行示例
    await chatWithGPT();
    await chatWithClaude();
    await chatWithGemini();
    await streamingExample();

    console.log('\n✅ 所有示例执行完成 | All examples completed!');
  } catch (error) {
    console.error(`\n❌ 错误: ${error.message}`);
    console.error(`❌ Error: ${error.message}`);
  }
}

main();
