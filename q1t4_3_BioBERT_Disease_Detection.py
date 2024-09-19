from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import csv

# Load the BioBERT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("ugaray96/biobert_ncbi_disease_ner")
model = AutoModelForTokenClassification.from_pretrained("ugaray96/biobert_ncbi_disease_ner")

# Initialize the NER pipeline
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)

# Read the input text from the file
with open('combined_text.txt', 'r') as file:
    text = file.read()

# Function to split text into chunks
def split_text(text, chunk_size=512):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Split text into chunks
chunks = split_text(text)

# Open the CSV file and write the header for entities
with open('biobert_entities.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ENTITY', 'LABEL'])

# Process each chunk and write the extracted entities to the CSV file
for i, chunk in enumerate(chunks):
    print(f"Processing chunk {i + 1}/{len(chunks)}...")
    result = ner_pipeline(chunk)
    diseases = []

    # Extract disease entities
    for entity in result:
        if entity["entity"] == "Disease":
            diseases.append(entity["word"])
        elif entity["entity"] == "Disease Continuation" and diseases:
            if "#" in entity["word"]:
                entity["word"].strip('#')
                diseases[-1] += f"{entity['word'].strip('#')}"
            else:
                diseases[-1] += f" {entity['word']}"

    # Write the extracted diseases to the CSV file
    with open('biobert_entities_disease.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for disease in diseases:
            writer.writerow([disease, 'DISEASE'])  # Write each disease as a row

    # break  # Remove this break if you want to process all chunks

print("Entities extraction completed and written to 'biobert_entities.csv'.")
