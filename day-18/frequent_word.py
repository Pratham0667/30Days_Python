#What is the most frequent word in the following paragraph?

from collections import Counter
import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love'

words = re.findall(r'\b\w+\b', paragraph.lower())
word_counts = Counter(words)

sorted_counts = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
print(sorted_counts)
