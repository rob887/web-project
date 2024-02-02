import pandas as pd 

df = pd.read_excel("results2024-1-19-1249.xlsx")
# print(df.columns)

print(df["Download (Mb/s)"].median())
print(df["Download (Mb/s)"].mean())

print(df["Upload (Mb/s)"].median())
print(df["Upload (Mb/s)"].mean())

# print(df.query(f"duration_ms > {mean_val}"))

# down_median_val = (df["Download (Mb/s)"].median())
