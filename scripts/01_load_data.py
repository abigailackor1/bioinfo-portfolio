import pandas as pd
import gzip

filepath = "data/raw/GSE138198_series_matrix.txt.gz"

with gzip.open(filepath, 'rt') as f:
    for i, line in enumerate(f):
        print(line.strip())
        if i > 30:
            break


df = pd.read_csv(filepath, sep='\t', comment='!', compression='gzip')
print(df.shape)
print(df.head())

# Define sample groups
ht_samples = ['GSM4101749','GSM4101750','GSM4101751','GSM4101752',
              'GSM4101753','GSM4101754','GSM4101755','GSM4101756',
              'GSM4101757','GSM4101758','GSM4101759','GSM4101760',
              'GSM4101761']

tn_samples = ['GSM4101782','GSM4101783','GSM4101784']

# Keep only HT and TN columns plus the ID
keep_cols = ['ID_REF'] + ht_samples + tn_samples
df_filtered = df[keep_cols]

print(df_filtered.shape)
print(df_filtered.head())

df_filtered.to_csv("data/processed/filtered_data.csv", index=False)
print("Filtered data saved to data/processed/filtered_data.csv")

git add. 
git commit -m "Load and filter data, save to processed folder"
git push