"""
Используйте списковое включение, чтобы из следующего списка вернуть
список всех слов, содержащих более четырех символов: 
["selftaught", "code", "sit", "eat", "programming", "dinner", "one", "two", "coding", "a", "tech"].
"""

words = ["selftaught", "code", "sit", "eat", "programming", "dinner", "one", "two", "coding", "a", "tech"]
long_words = [word for word in words if len(word) > 4]
print(long_words)