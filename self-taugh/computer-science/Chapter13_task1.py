"""
В предлагаемой строке удалите все повторяющиеся слова. Например, вам
дана строка "I am a self-taught programmer looking for a job as a programmer.".
Ваша функция должна вернуть "I am a self-taught programmer looking for a job as a.".
"""
def remove_duplicate_words(s):
    """Удаляет все повторяющиеся слова из строки"""
    words = s.split()
    seen = set()
    result = []
    
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    
    return ' '.join(result)


# Примеры использования
text = "I am a self-taught programmer looking for a job as a programmer."
print(remove_duplicate_words(text))
# Вывод: I am a self-taught programmer looking for a job as a.

text2 = "the quick brown fox jumps over the lazy dog the fox"
print(remove_duplicate_words(text2))
# Вывод: the quick brown fox jumps over lazy dog

text3 = "hello world hello"
print(remove_duplicate_words(text3))
# Вывод: hello world