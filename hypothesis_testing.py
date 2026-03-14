import pandas as pd
from scipy.stats import pearsonr

# Load dataset
df = pd.read_csv("cleaned_data.csv")

# Remove missing values
df = df.dropna()

# Correlation test
corr, p_value = pearsonr(df["age"], df["total_purchase_amount"])

print("Correlation between Age and Purchase Amount:", corr)
print("P-value:", p_value)

if p_value < 0.05:
    print("Result: Reject the null hypothesis.")
    print("There is a statistically significant relationship between age and purchase amount.")
else:
    print("Result: Fail to reject the null hypothesis.")
    print("Age does not significantly affect purchase amount.")