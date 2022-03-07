beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
from collections import defaultdict

L = len(beginWord)
all_combo_dict = defaultdict(list)
for word in wordList:
    for i in range(L):
        all_combo_dict[f'{word[:i]}*{word[i + 1:]}'].append(word)
queue = [(beginWord, 1)]
visited = {beginWord}
while queue:
    current_word, level = queue.pop(0)
    for i in range(L):
        intermediate_word = f'{current_word[:i]}*{current_word[i + 1:]}'
        for word in all_combo_dict[intermediate_word]:
            if word == endWord:
                print(level + 1)
            if word not in visited:
                visited.add(word)
                queue.append((word, level + 1))
print(0)
