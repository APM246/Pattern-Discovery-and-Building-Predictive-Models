import pandas as pd

df = pd.read_csv('data/cleaned_mobile_price.csv', sep=',', dtype=str)
output = pd.DataFrame()
class_labels = ['Yes', 'No']

# REDUCE NUMBER OF INSTANCES BY HALF
FINAL_NUM_ROWS = int(0.5 * len(df))

for label in class_labels:
    number_of_class_labels = (df['price_category'] == label).sum()
    proportion = number_of_class_labels/len(df)

    # number of rows in final data frame to maintain proportion
    num_rows = int(proportion * FINAL_NUM_ROWS)
    random_sample = df[df['price_category'] == label].sample(num_rows)
    output = output.append(random_sample)

output.to_csv("files for tasks/task 5/stratified_data.csv", index=False)
