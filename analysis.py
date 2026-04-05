import pandas as pd

# Load the dataset
df = pd.read_csv("data/protest_media_data.csv")

# Show full data 
print('DATASET'.center(50, '-'))
print(df) 

# Basic Info
print('\nBASIC INFO'.center(50, '-'))
print(df.info())

# Frame distribution
print('\nFRAME DISTRIBUTION'.center(50, '-'))
print(df['frame'].value_counts())

# Tone distribution
print('\nTONE DISTRIBUTION'.center(50, '-'))
print(df['tone'].value_counts())

# Focus distribution
print('\nFOCUS DISTRIBUTION'.center(50, '-'))
print(df['focus'].value_counts())

# Violence distribution
print('\nVIOLENCE DISTRIBUTION'.center(50, '-'))
print(df['violence'].value_counts())

# Cross analysis 
# Framing is directly linked to who is portrayed as responsible for violence
print('\nCROSS ANALYSIS: FRAME vs VIOLENCE'.center(50, '-'))
print(pd.crosstab(df['frame'], df['violence']))

