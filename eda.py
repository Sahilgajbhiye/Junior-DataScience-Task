
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned datasets
fear_greed_df = pd.read_csv("fear_greed_cleaned.csv")
historical_data_df = pd.read_csv("historical_data_cleaned.csv")

# Convert date columns to datetime objects for merging
fear_greed_df["date"] = pd.to_datetime(fear_greed_df["date"])
historical_data_df["Timestamp IST"] = pd.to_datetime(historical_data_df["Timestamp IST"])

# Extract date from \'Timestamp IST\' for merging with fear_greed_df
historical_data_df["trade_date"] = historical_data_df["Timestamp IST"].dt.date
fear_greed_df["date"] = fear_greed_df["date"].dt.date

# Merge the datasets on date
merged_df = pd.merge(historical_data_df, fear_greed_df, left_on="trade_date", right_on="date", how="left")

# Save merged dataframe to CSV
merged_df.to_csv("merged_data.csv", index=False)

# Display info and head of the merged DataFrame
print("\nMerged DataFrame Info:")
merged_df.info()
print("\nMerged DataFrame Head:")
print(merged_df.head())

# Descriptive statistics for key numerical columns
print("\nDescriptive Statistics for Merged DataFrame:")
print(merged_df[["Execution Price", "Size Tokens", "Size USD", "Closed PnL", "Fee", "value"]].describe())

# Distribution of Classification
print("\nDistribution of Sentiment Classification:")
print(merged_df["classification"].value_counts())

# Distribution of Side
print("\nDistribution of Trade Side:")
print(merged_df["Side"].value_counts())

# Plotting distributions
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.histplot(merged_df["value"].dropna(), kde=True)
plt.title("Distribution of Fear/Greed Index Value")

plt.subplot(1, 3, 2)
sns.countplot(x="classification", data=merged_df, palette="viridis")
plt.title("Distribution of Sentiment Classification")

plt.subplot(1, 3, 3)
sns.countplot(x="Side", data=merged_df, palette="magma")
plt.title("Distribution of Trade Side")

plt.tight_layout()
plt.savefig("distributions.png")
plt.close()

print("\nExploratory data analysis complete. Merged data info, descriptive statistics, and distribution plots saved.")


