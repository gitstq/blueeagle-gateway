/**
 * 蓝鹰AI网关 - Claude API 兼容调用示例
 * BlueEagle AI Gateway - Claude API Compatible Example
 * 
 * 使用 OpenAI SDK 兼容格式调用 Claude
 */

import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY_HERE', // 替换为您的API Key
  baseURL: 'https://ahg.codes/v1'
});

async function claudeChat() {
  console.log('🧠 蓝鹰AI网关 - Claude 3.5 Sonnet 调用示例\n');

  // 使用 OpenAI 兼容格式调用 Claude
  const response = await client.chat.completions.create({
    model: 'claude-3-5-sonnet-20240620',
    messages: [
      { 
        role: 'user', 
        content: '请用简洁的语言解释：什么是大语言模型(LLM)？它与传统程序有什么区别？' 
      }
    ],
    max_tokens: 800,
    temperature: 0.7
  });

  console.log('📥 AI回复:');
  console.log(response.choices[0].message.content);
  console.log(`\n📊 消耗Token: ${response.usage.total_tokens}`);
}

async function claudeWithSystem() {
  console.log('\n💡 Claude 带系统提示示例\n');

  const response = await client.chat.completions.create({
    model: 'claude-3-5-sonnet-20240620',
    messages: [
      { 
        role: 'system', 
        content: '你是一位严谨的数据科学家，回答问题时要引用相关的技术概念。' 
      },
      { 
        role: 'user', 
        content: '深度学习和机器学习有什么区别？' 
      }
    ],
    max_tokens: 800,
    temperature: 0.7
  });

  console.log('📥 AI回复:');
  console.log(response.choices[0].message.content);
}

claudeChat()
  .then(() => claudeWithSystem())
  .then(() => console.log('\n✅ 示例完成!'))
  .catch(console.error);
