# Junior Data Scientist – Trader Behavior Insights

## Assignment Overview
This assignment explores the relationship between trader performance and market sentiment, uncovers hidden patterns, and delivers insights that can drive smarter trading strategies. Two primary datasets were used:
1. Bitcoin Market Sentiment Dataset (Fear/Greed Index)
2. Historical Trader Data from Hyperliquid

## Data Acquisition and Preprocessing

### Data Sources
The Bitcoin Market Sentiment Dataset was obtained from [https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing](https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing). The Historical Trader Data from Hyperliquid was obtained from [https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing](https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing).

### Preprocessing Steps
1. **Loading Data**: Both `fear_greed_index.csv` and `historical_data.csv` were loaded into pandas DataFrames.
2. **Data Inspection**: Initial inspection using `.info()` and `.head()` revealed data types and potential issues. Missing values were checked using `.isnull().sum()`, and no significant missing data was found.
3. **Date Conversion**: The `date` column in the `fear_greed_df` and `Timestamp IST` and `Timestamp` columns in `historical_data_df` were converted to datetime objects for proper time-series analysis and merging. Specific format strings were used to handle the date formats correctly.
4. **Merging Datasets**: The two datasets were merged based on the date. A `trade_date` column was extracted from `Timestamp IST` in the historical data to align with the daily granularity of the sentiment data. A left merge was performed to ensure all historical trade data was retained, with sentiment data joined where available.
5. **Saving Cleaned Data**: The preprocessed and merged dataframes were saved as `fear_greed_cleaned.csv`, `historical_data_cleaned.csv`, and `merged_data.csv` for subsequent analysis.

## Exploratory Data Analysis (EDA)

### Overview
Exploratory Data Analysis was conducted to understand the distributions of key variables and identify initial patterns. This involved generating descriptive statistics and visualizing the distributions of sentiment values, sentiment classifications, and trade sides.

### Key Observations from EDA
- **Fear/Greed Index Value Distribution**: The distribution of the Fear/Greed Index `value` showed multiple peaks, indicating that certain sentiment levels are more common than others. This suggests a non-uniform distribution of market sentiment over time.
- **Sentiment Classification Distribution**: The `classification` column revealed that 'Fear' was the most frequent sentiment, followed by 'Greed', 'Extreme Greed', 'Neutral', and 'Extreme Fear'. This highlights periods of market apprehension being more common.
- **Trade Side Distribution**: The `Side` column (BUY/SELL) showed a relatively balanced distribution, with a slightly higher count of SELL orders. This indicates active two-way trading activity.

## Analysis of Trader Performance and Market Sentiment

### Correlation Analysis
A correlation analysis between the Fear/Greed Index `value` and `Closed PnL` was performed. The correlation coefficient was found to be **0.01**, indicating a very weak positive linear relationship. This suggests that while there might be a slight tendency for profitability to increase with higher sentiment values, the relationship is not strong enough to be a direct predictor of individual trade performance.

### PnL by Sentiment Classification
Aggregating the total `Closed PnL` by `classification` revealed significant differences:

| Classification | Total Closed PnL (USD) |
|----------------|------------------------|
| Fear           | 3,357,155              |
| Extreme Greed  | 2,715,171              |
| Greed          | 2,150,129              |
| Neutral        | 1,292,921              |
| Extreme Fear   | 739,110                |

Surprisingly, the highest total `Closed PnL` was observed during 'Fear' periods, suggesting that these periods might offer more profitable trading opportunities. Conversely, 'Extreme Fear' periods yielded the lowest total `Closed PnL`.

### Average Trade Size by Sentiment Classification
The average trade size (`Size USD`) also varied across sentiment classifications:

| Classification | Average Trade Size (USD) |
|----------------|--------------------------|
| Fear           | 7,816.11                 |
| Greed          | 5,736.88                 |
| Extreme Fear   | 5,349.73                 |
| Neutral        | 4,782.73                 |
| Extreme Greed  | 3,112.25                 |

'Fear' periods were associated with the largest average trade sizes, reinforcing the idea that more substantial trading activity and potentially more confident traders are active during these times.

### Visualizations
- **Daily Average PnL by Sentiment Classification**: This plot illustrates the fluctuations in average daily PnL across different sentiment states over time. It shows that while there isn't a consistently clear pattern, certain spikes in average PnL can be observed during specific sentiment periods.
- **Closed PnL Distribution by Sentiment Classification**: This box plot visualizes the spread and outliers of profitability for each sentiment. It highlights that significant profits or losses can occur regardless of the prevailing sentiment, emphasizing the role of individual trading strategies.

## Insights and Trading Strategy Recommendations

### 1. Capitalize on 'Fear' Periods
Given that 'Fear' periods correspond to the highest total `Closed PnL` and largest average trade sizes, traders could consider adopting contrarian strategies during these times. This might involve identifying fundamentally strong assets that are temporarily undervalued due to market apprehension and taking calculated long positions. Conversely, short-selling opportunities might also arise from overreactions to negative news during fearful periods. It is crucial to combine this with thorough fundamental and technical analysis to identify genuine opportunities rather than falling into value traps.

### 2. Exercise Caution During 'Extreme Fear' and 'Extreme Greed'
'Extreme Fear' periods resulted in the lowest total `Closed PnL`, suggesting that these are highly volatile and unpredictable times where even experienced traders struggle to find consistent profitability. It might be prudent for traders to reduce exposure or even temporarily exit the market during such periods to preserve capital. Similarly, 'Extreme Greed' periods, characterized by smaller average trade sizes, could indicate market tops or overextension. Traders should be wary of FOMO (Fear Of Missing Out) and consider taking profits or reducing risk during these times.

### 3. Focus on Risk Management and Individual Strategy
The low correlation between the Fear/Greed Index value and `Closed PnL`, coupled with the wide distribution of PnL across all sentiment categories, underscores that market sentiment alone is not a guarantee of profitability. Effective risk management, including setting stop-loss orders and managing position sizes, remains paramount. Furthermore, developing and adhering to a well-defined individual trading strategy, incorporating technical analysis, fundamental analysis, and understanding of market microstructure, is more critical than solely relying on sentiment indicators.

### 4. Utilize Sentiment as a Confluence Factor, Not a Sole Indicator
The Fear/Greed Index should be used as a confluence factor rather than a standalone trading signal. For instance, if a trader identifies a strong technical setup for a long position, and the market sentiment is in 'Fear', this could provide additional conviction for the trade. Conversely, if a setup suggests a short position during 'Greed', it could reinforce the decision. Sentiment can help gauge overall market psychology, but it should be combined with other analytical tools for robust decision-making.

### 5. Adapt Trade Size to Sentiment
The observation that average trade sizes are larger during 'Fear' and smaller during 'Extreme Greed' could inform dynamic position sizing. Traders might consider increasing their position sizes during periods of 'Fear' (assuming other technical and fundamental indicators align) and decreasing them during 'Extreme Greed' to manage risk and optimize returns.

## Conclusion
While market sentiment, as captured by the Fear & Greed Index, provides valuable insights into the psychological state of the Bitcoin market, its direct correlation with individual trade profitability is weak. However, when analyzed in conjunction with aggregated PnL and trade size data, distinct patterns emerge. Profitable opportunities appear to be more prevalent during 'Fear' periods, while 'Extreme Fear' and 'Extreme Greed' warrant increased caution. Ultimately, successful trading hinges on a combination of robust risk management, a well-defined personal strategy, and the judicious use of sentiment as a complementary indicator within a broader analytical framework.


