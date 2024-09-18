from collections import Counter
import csv

with open('combined_text.txt', 'r') as file:
    text = file.read()

words = text.split()

word_counts = Counter(words)

top_words = word_counts.most_common(30)

with open('top_30_words_Using_in_build_functions.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Word', 'Count'])
    writer.writerows(top_words)