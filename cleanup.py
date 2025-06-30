import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data.xlsx")

# Example cleaning
df['Sales'] = df['Sales'].fillna(df['Sales '])
df.drop(columns=['Sales '], inplace=True)
df.dropna(subset=['Sales'], inplace=True)

# Summarize
summary = df.groupby('Month')['Sales'].sum()
print(summary)

# Plot
summary.plot(kind='bar')
plt.title('Monthly Sales')
plt.ylabel('KES')
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
