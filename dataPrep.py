#!/usr/bin/env python3


# imports
import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv("Kinematics_Data.csv")
# Drop unnecessary columns
df.drop(columns=["date", "username", "wrist", "time"], inplace=True)
print(df.info())
df.head()

# Check for imbalance
df['activity'].value_counts()
df['activity'].hist(bins=10);
