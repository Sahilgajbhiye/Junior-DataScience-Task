
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


merged_df = pd.read_csv("merged_data.csv")

merged_df["trade_date"] = pd.to_datetime(merged_df["trade_date"])
merged_df["date"] = pd.to_datetime(merged_df["date"])

daily_pnl_sentiment = merged_df.groupby([merged_df["trade_date"].dt.date, "classification"])["Closed PnL"].mean().unstack()

plt.figure(figsize=(12, 6))
daily_pnl_sentiment.plot(kind="line", ax=plt.gca())
plt.title("Daily Average PnL by Sentiment Classification")
plt.xlabel("Date")
plt.ylabel("Average Closed PnL")
plt.grid(True)
plt.tight_layout()
plt.savefig("daily_pnl_by_sentiment.png")
plt.close()

plt.figure(figsize=(10, 6))
sns.boxplot(x="classification", y="Closed PnL", data=merged_df, palette="viridis")
plt.title("Closed PnL Distribution by Sentiment Classification")
plt.xlabel("Sentiment Classification")
plt.ylabel("Closed PnL")
plt.tight_layout()
plt.savefig("pnl_distribution_by_sentiment.png")
plt.close()

correlation = merged_df[["value", "Closed PnL"]].corr().iloc[0, 1]
print(f"\nCorrelation between Fear/Greed Index Value and Closed PnL: {correlation:.2f}")

pnl_by_classification = merged_df.groupby("classification")["Closed PnL"].sum().sort_values(ascending=False)
print("\nTotal Closed PnL by Sentiment Classification:")
print(pnl_by_classification)

avg_trade_size_sentiment = merged_df.groupby("classification")["Size USD"].mean().sort_values(ascending=False)
print("\nAverage Trade Size (USD) by Sentiment Classification:")
print(avg_trade_size_sentiment)

print("\nAnalysis of trader performance and market sentiment complete. Plots and statistics saved.")


