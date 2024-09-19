from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import csv

tokenizer = AutoTokenizer.from_pretrained("ugaray96/biobert_ncbi_disease_ner")
model = AutoModelForTokenClassification.from_pretrained("ugaray96/biobert_ncbi_disease_ner")

ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)

with open('combined_text.txt', 'r') as file:
    text = file.read()

def split_text(text, chunk_size=512):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

chunks = split_text(text)

with open('biobert_entities.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ENTITY', 'LABEL'])

for i, chunk in enumerate(chunks):
    print(f"Processing chunk {i + 1}/{len(chunks)}...")
    result = ner_pipeline(chunk)
    diseases = []

    for entity in result:
        if entity["entity"] == "Disease":
            diseases.append(entity["word"])
        elif entity["entity"] == "Disease Continuation" and diseases:
            if "#" in entity["word"]:
                entity["word"].strip('#')
                diseases[-1] += f"{entity['word'].strip('#')}"
            else:
                diseases[-1] += f" {entity['word']}"

    with open('biobert_entities_disease.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for disease in diseases:
            writer.writerow([disease, 'DISEASE'])


print("Entities extraction completed and written to 'biobert_entities.csv'.")
