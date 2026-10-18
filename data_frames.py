import pandas as pd
import numpy as np
import seaborn as sns

# Generates dates for 6 different days
dates = pd.date_range('20130101', periods=6)

# Creates DataFrame with dates at the index column
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    

print(df)

# Or create a DataFrame with a dictionary of objects
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4,dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

# Get the data types for each column
print(df2.dtypes)

# Check data types and null values
print(df2.info())

iris_df = sns.load_dataset('iris')
print(iris_df.columns)

# Select only the species column
just_the_species = iris_df['species']
print(just_the_species.sample(5))

# Filter for specific values in a column
small_sepal_length = iris_df[iris_df['sepal_length'] < 4.8]
print(small_sepal_length.sample(5))


# Accessing specific records
# Check if all entries in "Identifier" column are unique
df['Identifier'].is_unique

# Set "Identifier" column as the index
df = df.set_index('Identifier')

# Access a specific row
df.loc[76244]

# grouping in pandas
# If you want the insurance charges of all people between the ages of 30 and 35
# Get people in the 30-35 age group
between_30_and_35 = insurance_df[(insurance_df['age'] > 30) & 
                                 (insurance_df['age'] < 35)]

# Print mean charges for all people in the 30-35 age group
print(between_30_and35['charges'].mean())

# Alternatively you can use the query method to get people in the 30-35 age group
between_30_and_35 = insurance_df.query("age > 30 and age < 35")

# Print mean charges for all people in the 35-35 age group
print(between_30_and_35['charges'].mean())

# Get the mean charges for each age
print(insurance_df.groupby('age')['charges'].mean())