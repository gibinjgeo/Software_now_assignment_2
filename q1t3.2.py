from transformers import AutoTokenizer
from collections import Counter
import csv

tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")

token_counts = Counter()

with open('combined_text.txt', 'r') as file:
    for line in file:
        tokens = tokenizer.tokenize(line)
        token_counts.update(tokens)

top_50_tokens = token_counts.most_common(50)
top_30_tokens = [i for i in top_50_tokens if i[0].isalpha()]

with open('top_30_tokens_using_AutoTokenizer.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Token', 'Count'])
    writer.writerows(top_30_tokens)
