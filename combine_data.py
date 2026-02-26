import pandas as pd

# Load CSV files
df_2022 = pd.read_csv("data/auction_2022.csv")
df_2023 = pd.read_csv("data/auction_2023.csv")
df_2025 = pd.read_csv("data/auction_2025.csv")

# Add Year column
df_2022["Year"] = 2022
df_2023["Year"] = 2023
df_2025["Year"] = 2025

# Combine all years
combined_df = pd.concat(
    [df_2022, df_2023, df_2025],
    ignore_index=True
)

print("Total Rows:", combined_df.shape[0])
print("Total Columns:", combined_df.shape[1])

print("\nColumn Names:")
print(combined_df.columns)

print("\nFirst 5 rows:")
print(combined_df.head())

# Save combined dataset
combined_df.to_csv("data/combined_auction_data.csv", index=False)

print("\nCombined dataset saved successfully.")