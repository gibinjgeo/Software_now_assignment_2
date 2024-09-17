import spacy
import csv

# Load the SpaCy 'en_ner_bc5cdr_md' model
nlp_ner = spacy.load("en_ner_bc5cdr_md")

# Read the text file
with open('combined_text.txt', 'r') as file:
    text = file.read()


# Function to split text into chunks of a specified size
def split_text(text, chunk_size=1000000):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


# Split the text into chunks
chunks = split_text(text)

# Open the CSV file once and write the header
with open('spacy_en_ner_bc5cdr_md_entities.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Entity', 'Label'])  # Write the header once

# Process each chunk and append the results to the CSV file
for i, chunk in enumerate(chunks):
    print(f"Processing chunk {i + 1}/{len(chunks)}...")

    # Run the NER model on each chunk
    doc_ner = nlp_ner(chunk)
    entities_ner_chunk = [(ent.text, ent.label_) for ent in doc_ner.ents if ent.label_ in ["DISEASE", "DRUG"]]

    # Append the chunk results to the CSV file
    with open('spacy_en_ner_bc5cdr_md_entities.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(entities_ner_chunk)

print(f"Entities extraction completed and written to 'spacy_en_ner_bc5cdr_md_entities.csv'.")
