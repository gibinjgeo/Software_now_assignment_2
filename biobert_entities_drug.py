from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import csv

# Load the BioBERT model and tokenizer for drug entity recognition
tokenizer = AutoTokenizer.from_pretrained("d4data/biomedical-ner-all")
model = AutoModelForTokenClassification.from_pretrained("d4data/biomedical-ner-all")

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
with open('biobert_entities_drug.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ENTITY', 'LABEL'])

# Process each chunk and extract drug/chemical entities
for i, chunk in enumerate(chunks):
    print(f"Processing chunk {i + 1}/{len(chunks)}...")
    result = ner_pipeline(chunk)

    # To store the combined medication names
    drugs = []
    drug = ''

    # Open the CSV file for appending extracted entities
    with open('biobert_entities_drug.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        for entity in result:
            if entity["entity"].startswith("B-Medication"):
                # Append the current drug to the list before starting a new one
                if drug != '' and len(drug) > 3:  # Only append if the drug is longer than 3 characters
                    writer.writerow([drug, 'DRUG'])  # Write the drug to the CSV
                    drugs.append(drug)
                    drug = ''

                drug = entity['word'].replace('#', '')  # Start a new drug name

            elif entity["entity"].startswith("I-Medication") and drug:
                drug += entity['word'].replace('#', '')  # Continue the drug name

        # After processing, write the final drug if any
        if drug:
            writer.writerow([drug, 'DRUG'])  # Write the final drug to the CSV
            drugs.append(drug)

print("Entities extraction completed and written to 'biobert_entities_drug.csv'.")
