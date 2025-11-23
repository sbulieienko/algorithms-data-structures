"""
Дан список слов в алфавитном порядке. 
Напишите функцию, которая выполнит двоичный поиск слова и 
вернет ответ о том, имеется ли оно в списке.
""" 

def binary_search(word, word_list):
    left = 0
    right = len(word_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if word_list[mid] == word:
            return True
        elif word_list[mid] < word:
            left = mid + 1
        else:
            right = mid - 1
    return False

word_list = ["apple", "banana", "cherry", "date", "fig", "grape"]
word = "banana"
print(binary_search(word, word_list))  # True
