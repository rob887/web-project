import pandas as pd
import numpy as np

df = pd.read_csv("spotify_songs.csv")

# print(df.shape)

# print(df.columns)

# print(df["playlist_genre"].value_counts())
# print(df["playlist_name"].value_counts())

# print(df["track_artist"].mode()[0])

# data = {"categories" : ["A", "B", "C"]}
# df = pd.DataFrame()

# print(df["duration_ms"].median())
# print(df["duration_ms"].mean())


# max_ms=df["duration_ms"].max()
# min_ms=df["duration_ms"].min()
# print(max_ms-min_ms)

# print(df["duration_ms"].sum())

# print(df.sort_values(by=["duration_ms"]))
# print(df.sort_values(by=["duration_ms"], ascending=False))

# print(df.sort_values(by=["track_artist"]))

# df = df.sort_values(by=["track_artist"])
# print(df,iloc[0])

# print(df.query("track_artist=='Ricky martin'"))

# mean_val = df["duration_ms"].mean()
# print(mean_val)
# print(df.query("duration_ms > @mean_val"))

print(df.query("track_artist=='mullin rap'"))