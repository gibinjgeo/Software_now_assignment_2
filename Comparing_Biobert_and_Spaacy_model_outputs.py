import pandas as pd
import matplotlib.pyplot as plt


def process_entities(file_path):
    df = pd.read_csv(file_path)

    df.columns = df.columns.str.strip().str.lower()

    if 'entity' in df.columns:
        entities = df['entity'].str.lower().unique()
        return set(entities)
    else:
        print(f"Error: 'entity' column not found in {file_path}")
        return set()


Spacy_Disease_and_drug_ntities = process_entities('spacy_en_ner_bc5cdr_md_entities.csv')
Biobert_drug_entities = process_entities('biobert_entities_drug.csv')
Biobert_disease_entities = process_entities('biobert_entities_disease.csv')

total_entities_Spacy = len(Spacy_Disease_and_drug_ntities)
total_entities_Biobert_Drug = len(Biobert_drug_entities)
total_entities_Biobert_Disease = len(Biobert_disease_entities)

common_Drug = Spacy_Disease_and_drug_ntities.intersection(Biobert_drug_entities)
common_Disease = Spacy_Disease_and_drug_ntities.intersection(Biobert_disease_entities)

unique_to_file1_against_file2 = Spacy_Disease_and_drug_ntities.difference(Biobert_drug_entities)
unique_to_file1_against_file3 = Spacy_Disease_and_drug_ntities.difference(Biobert_disease_entities)

output_data = {
    "Metric": [
        "Total entities in file1", "Total entities in file2", "Total entities in file3",
        "Common entities between file1 and file2", "Common entities between file1 and file3",
        "Unique entities in file1 compared to file2", "Unique entities in file1 compared to file3"
    ],
    "Value": [
        total_entities_Spacy, total_entities_Biobert_Drug, total_entities_Biobert_Disease,
        len(common_Drug), len(common_Disease),
        len(unique_to_file1_against_file2), len(unique_to_file1_against_file3)
    ]
}

output_df = pd.DataFrame(output_data)

output_df.to_csv('comparison_summary.csv', index=False)
pd.DataFrame(list(common_Drug), columns=['Common Entities (file1 & file2)']).to_csv(
    'common_entities_Drug.csv', index=False)
pd.DataFrame(list(common_Disease), columns=['Common Entities (file1 & file3)']).to_csv(
    'common_entities_Disease.csv', index=False)

pd.DataFrame(list(unique_to_file1_against_file2), columns=['Unique Entities (file1 vs file2)']).to_csv(
    'unique_entities_Drug.csv', index=False)
pd.DataFrame(list(unique_to_file1_against_file3), columns=['Unique Entities (file1 vs file3)']).to_csv(
    'unique_entities_Disease.csv', index=False)

labels = ['Spacy', 'Bibert_Drug', 'Bibert_Disease', 'Common_Drug', 'Common_Disease']
values = [total_entities_Spacy, total_entities_Biobert_Drug, total_entities_Biobert_Disease,
          len(common_Drug), len(common_Disease)]

plt.figure(figsize=(10, 6))
plt.bar(labels, values, color=['blue', 'orange', 'green', 'red', 'purple'])
plt.xlabel('Entity Groups')
plt.ylabel('Count')
plt.title('Total and Common Entities Count')
plt.show()
plt.savefig('Bar_graph_Comparison')
