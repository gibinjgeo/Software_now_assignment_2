import pandas as pd

csv_files = ['CSV1.csv', 'CSV2.csv', 'CSV4.csv', 'CSV3.csv']

combined_text = ""
for file in csv_files:
    df = pd.read_csv(file)
    if 'TEXT' in df.columns:
        text = df['TEXT'].tolist()
    elif 'SHORT-TEXT' in df.columns:
        text = df['SHORT-TEXT'].tolist()

    combined_text += f' '.join(text) + '\n'

with open('combined_text.txt', 'w') as txt_file:
    txt_file.write(combined_text)
