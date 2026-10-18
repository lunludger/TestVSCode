# Dropping columns in a dataframe

school_data.drop(["math_score", "english_score", "science_score"], axis=1, inplace=True)

# Replacing values
my_data.Nationality.fillna('Other', inplace=True)

# To perform general replacements for example to replace 'UK' with 'United Kingdom' use
my_data.Nationality.replace('UK', 'United Kingdom', inplace=True)