from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import csv

tokenizer = AutoTokenizer.from_pretrained("d4data/biomedical-ner-all")
model = AutoModelForTokenClassification.from_pretrained("d4data/biomedical-ner-all")

ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)

with open('combined_text.txt', 'r') as file:
    text = file.read()


def split_text(text, chunk_size=512):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


chunks = split_text(text)

with open('biobert_entities_drug.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ENTITY', 'LABEL'])

for i, chunk in enumerate(chunks):
    print(f"Processing chunk {i + 1}/{len(chunks)}...")
    result = ner_pipeline(chunk)

    drugs = []
    drug = ''

    with open('biobert_entities_drug.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        for entity in result:
            if entity["entity"].startswith("B-Medication"):
                if drug != '' and len(drug) > 3:
                    writer.writerow([drug, 'DRUG'])
                    drugs.append(drug)
                    drug = ''

                drug = entity['word'].replace('#', '')

            elif entity["entity"].startswith("I-Medication") and drug:
                drug += entity['word'].replace('#', '')

        if drug:
            writer.writerow([drug, 'DRUG'])
            drugs.append(drug)

print("Entities extraction completed and written to 'biobert_entities_drug.csv'.")
