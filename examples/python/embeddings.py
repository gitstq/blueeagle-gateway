"""
蓝鹰AI网关 - Embeddings 向量嵌入示例
BlueEagle AI Gateway - Embeddings Example
"""

from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY_HERE",  # 替换为您的API Key
    base_url="https://ahg.codes/v1"
)

def basic_embeddings():
    """基础文本嵌入示例"""
    print("📝 生成文本嵌入向量...\n")
    
    response = client.embeddings.create(
        model="text-embedding-3-large",
        input="The quick brown fox jumps over the lazy dog"
    )
    
    embedding = response.data[0].embedding
    print(f"✅ 嵌入向量维度: {len(embedding)}")
    print(f"📊 前5个维度值: {embedding[:5]}")
    print(f"💰 消耗Token: {response.usage.total_tokens}")

def batch_embeddings():
    """批量文本嵌入示例"""
    print("\n📚 批量生成嵌入向量...\n")
    
    texts = [
        "人工智能将改变世界",
        "机器学习是AI的核心技术",
        "深度学习推动了计算机视觉的进步",
        "自然语言处理让人机交互更自然"
    ]
    
    response = client.embeddings.create(
        model="text-embedding-3-large",
        input=texts
    )
    
    for i, data in enumerate(response.data):
        print(f"文本 {i+1}: {texts[i][:20]}...")
        print(f"  向量维度: {len(data.embedding)}")
        print(f"  前3个值: {data.embedding[:3]}")
        print()

def semantic_search_demo():
    """语义搜索示例 - 计算文本相似度"""
    print("🔍 语义搜索示例 - 计算文本相似度\n")
    
    texts = [
        "如何学习Python编程？",
        "Python入门教程推荐",
        "今天天气真好啊",
        "机器学习算法有哪些？",
        "深度学习框架比较"
    ]
    
    query = "Python教程和入门指南"
    
    # 为查询和所有文本生成嵌入
    query_embedding = client.embeddings.create(
        model="text-embedding-3-large",
        input=query
    ).data[0].embedding
    
    text_embeddings = client.embeddings.create(
        model="text-embedding-3-large",
        input=texts
    ).data
    
    # 计算余弦相似度
    import math
    
    def cosine_similarity(a, b):
        dot_product = sum(x * y for x, y in zip(a, b))
        norm_a = math.sqrt(sum(x * x for x in a))
        norm_b = math.sqrt(sum(x * x for x in b))
        return dot_product / (norm_a * norm_b)
    
    print(f"查询: '{query}'")
    print("\n相似度排名:")
    similarities = []
    for i, data in enumerate(text_embeddings):
        sim = cosine_similarity(query_embedding, data.embedding)
        similarities.append((sim, texts[i]))
    
    similarities.sort(reverse=True)
    
    for i, (sim, text) in enumerate(similarities, 1):
        print(f"  {i}. {text} (相似度: {sim:.4f})")

if __name__ == "__main__":
    basic_embeddings()
    batch_embeddings()
    semantic_search_demo()
