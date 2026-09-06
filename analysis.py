import pandas as pd
from scipy.stats import fisher_exact

df = pd.read_csv("data.csv")

# Conversion rate for each group
conversion = df.groupby("group")["converted"].mean() * 100

print("Conversion rate:")
print(conversion)

# Create a 2x2 table
a_converted = df[(df["group"] == "A") & (df["converted"] == 1)].shape[0]
a_not_converted = df[(df["group"] == "A") & (df["converted"] == 0)].shape[0]

b_converted = df[(df["group"] == "B") & (df["converted"] == 1)].shape[0]
b_not_converted = df[(df["group"] == "B") & (df["converted"] == 0)].shape[0]

table = [
    [a_converted, a_not_converted],
    [b_converted, b_not_converted]
]

odds_ratio, p_value = fisher_exact(table)

print("\nP-value:", round(p_value, 4))

if p_value < 0.05:
    print("The difference is statistically significant.")
else:
    print("The difference is not statistically significant.")
