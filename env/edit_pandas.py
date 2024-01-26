import pandas as pd
import numpy as np

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
ranking = pd.Series([3,1,2,4])

df = pd.DataFrame({
    "Languages": languages,
    "Ranking": ranking
})

# df.loc[4] = ["php", 11]
# print(df)

# df.loc[3.5] = ["KESL", 20]
# print(df)

# df =df.sort_index()
# print(df)

# df=df.reset_index(drop=True)
# print(df)

new_data = pd.DataFrame({"Languages": ["PHP"], "Ranking": [11]})
df = pd.concat([df, new_data], ignore_index=True)

df.loc[5] = ["Java", 7]
df.loc[6] = ["TypeScript", 5]

df["Ranking 2022"] = [4,1,2,3,10,6,5]
# df["Ranking 2021"] = [3,1,2,4,11,5,7]
df["Ranking 2020"] = [4,1,2,3,8,5,9]
df["Ranking 2019"] = [4,1,2,3,8,5,10]

df.insert(3, "Ranking 2021",  [3,1,2,4,11,5,7])

# new_column_to_add = pd.DataFrame({"Ranking 2022" = [4,1,2,3,10,6,5]})
# df = pd.concat([df, new_column_to_add])

print(df.columns.get_loc("Ranking 2022"))

df.rename(columns={"Ranking": "Ranking 2023"})

# df = df.set_index("Languages")

print(df)