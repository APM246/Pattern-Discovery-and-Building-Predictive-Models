import pandas as pd
from collections import defaultdict

#load into data frame
df = pd.read_csv("data/mobile_price.csv", sep=',')

# check if any null or missing values in entire CSV file
if df.isnull().values.any():
    print('Data has missing values')

else:
    # file has no null values thus set default data type as str
    df = pd.read_csv("data/mobile_price.csv", sep=',', dtype=str)

    categorical_columns = ["blue", "dual_sim", "four_g", "three_g", "touch_screen", "wifi", "price_category"]

    # map 'has' and 1 to 'yes' and any other value to 'no'
    replacements_dict = defaultdict(lambda: "no")
    replacements_dict.update({"has": "yes", "1": "yes", "yes": "yes"})

    for column in categorical_columns:
        df[column] = df[column].str.lower()
        df[column] = df[column].map(replacements_dict)

    df.to_csv("data/cleaned_mobile_price.csv", index = False)