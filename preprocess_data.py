
import pandas as pd

# Load the datasets
fear_greed_df = pd.read_csv("fear_greed_index.csv")
historical_data_df = pd.read_csv("historical_data.csv")

# Display initial info and head of each DataFrame
print("Fear Greed Index DataFrame Info:")
fear_greed_df.info()
print("\nFear Greed Index DataFrame Head:")
print(fear_greed_df.head())

print("\nHistorical Data DataFrame Info:")
historical_data_df.info()
print("\nHistorical Data DataFrame Head:")
print(historical_data_df.head())

# Check for missing values
print("\nMissing values in Fear Greed Index DataFrame:")
print(fear_greed_df.isnull().sum())

print("\nMissing values in Historical Data DataFrame:")
print(historical_data_df.isnull().sum())

# Convert 'date' column to datetime in fear_greed_df
fear_greed_df["date"] = pd.to_datetime(fear_greed_df["date"])

# Convert 'Timestamp IST' and 'Timestamp' to datetime in historical_data_df
historical_data_df["Timestamp IST"] = pd.to_datetime(historical_data_df["Timestamp IST"], format="%d-%m-%Y %H:%M")
historical_data_df["Timestamp"] = pd.to_datetime(historical_data_df["Timestamp"], unit="ms") # Changed unit to milliseconds

# Save cleaned dataframes to new CSV files
fear_greed_df.to_csv("fear_greed_cleaned.csv", index=False)
historical_data_df.to_csv("historical_data_cleaned.csv", index=False)

print("\nData preprocessing complete. Cleaned files saved as fear_greed_cleaned.csv and historical_data_cleaned.csv")


