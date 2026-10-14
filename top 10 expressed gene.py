import pandas as pd

# Create sample gene expression data
data = {
    "Gene_ID": [
        "TP53", "GAPDH", "ACTB", "MYC", "EGFR",
        "TPH1", "INS", "BRCA1", "TNF", "IL6",
        "VEGFA", "BDNF"
    ],
    "Expression": [
        1250, 4800, 3900, 2100, 1750, 950,
        3200, 1450, 2700, 1850, 2400, 1100
    ]
}

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Sort genes by expression in descending order
df = df.sort_values(by="Expression", ascending=False)

# Select the top 10 expressed genes
top10 = df.head(10)

# Display the result
print("Top 10 Highly Expressed Genes:")
print(top10.to_string(index=False))

# Save the result as a CSV file
top10.to_csv("top10_genes.csv", index=False)