/**
 * 蓝鹰AI网关 - 流式输出示例
 * BlueEagle AI Gateway - Streaming Example
 */

import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY_HERE', // 替换为您的API Key
  baseURL: 'https://ahg.codes/v1'
});

async function streamingChat() {
  console.log('💬 蓝鹰AI网关 - 流式输出示例\n');

  const stream = await client.chat.completions.create({
    model: 'gpt-4o',
    messages: [
      { 
        role: 'user', 
        content: '请给我讲一个关于程序员的幽默故事，大约150字。' 
      }
    ],
    stream: true, // 开启流式输出
    temperature: 0.8,
    max_tokens: 500
  });

  process.stdout.write('🤖 AI: ');

  let fullResponse = '';
  for await (const chunk of stream) {
    const content = chunk.choices[0]?.delta?.content;
    if (content) {
      process.stdout.write(content);
      fullResponse += content;
    }
  }

  console.log('\n\n✅ 流式输出完成!');
  console.log(`📊 回复长度: ${fullResponse.length} 字符`);
}

streamingChat().catch(console.error);
