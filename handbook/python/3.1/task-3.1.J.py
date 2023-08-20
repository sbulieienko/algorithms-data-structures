lines = []
line = ''

while True:
    line = input()
    if line == 'ФИНИШ':
        break
    lines.append(line)

char_freq = dict()

for line in lines:
    for item in line:
        char = item.lower()
        if not char.isalpha():
            continue
        elif char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

max_key = None
max_value = None

for item in char_freq:
    if max_key is None:
        max_key = item
        max_value = char_freq[item]
        continue
    if char_freq[item] > max_value:
        max_key = item
        max_value = char_freq[item]
    elif char_freq[item] == max_value and item < max_key: 
        max_key = item
        max_value = char_freq[item]

print(max_key)
