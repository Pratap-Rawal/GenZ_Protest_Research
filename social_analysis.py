import pandas as pd

df = pd.read_csv("social_media_data.csv")

print("SOCIAL MEDIA DATA".center(50, '-'))
print(df)

print("\nTONE COUNT".center(50, '-'))
print(df['tone'].value_counts())

print("\nFRAME COUNT".center(50, '-'))
print(df['frame'].value_counts())

print("\nEMOTION LEVEL".center(50, '-'))
print(df['emotion'].value_counts())