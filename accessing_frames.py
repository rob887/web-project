import pandas as pd
import numpy as np

df = pd.read_excel("dev_rankings.xlsx")
df = df.set_index("Languages")
print(df)

print(df["Ranking 2019"])

print(df[["Ranking 2023", "Ranking 2022"]])

print(df.loc["Python"])

# df.loc["Python", "JavaScript", "HTML"]
# print(df[["Ranking 2023", "Ranking 2021", "Ranking 2019"]])

print(df.loc[:"HTML":, :"Ranking 2019": 2])

print(df.iloc[3])

print(df.at["HTML", "Ranking 2023"])

print(df.head(2))