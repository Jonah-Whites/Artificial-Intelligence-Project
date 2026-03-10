import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

path = kagglehub.dataset_download("aliafzal9323/chicago-crime-dataset-2024-2026")

df = pd.read_csv(path +  "/chicago crimes.csv")


# Count total calls per year
total_calls = df.groupby("Year").size()
print(total_calls)
# Count domestic calls per year
domestic_calls = df[df["Domestic"] == 1].groupby("Year").size()

# Align indexes so both series match
domestic_calls = domestic_calls.reindex(total_calls.index, fill_value=0)
print(domestic_calls)

# Non-domestic calls (for stacking)
non_domestic = total_calls - domestic_calls

# Plot stacked bar chart
plt.figure(figsize=(10,6))

plt.bar(total_calls.index, non_domestic, label="Other Calls")
plt.bar(total_calls.index, domestic_calls, bottom=non_domestic, label="Domestic Calls")

plt.xlabel("Year")
plt.ylabel("Number of Calls")
plt.title("Police Calls per Year (Domestic vs Other)")
plt.legend()

plt.xticks(total_calls.index)
plt.tight_layout()

print("done")
plt.show()




