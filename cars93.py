import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Inline indicates graphs should be presented as a cell output
plt.show()

# Load data
car_data = pd.read_csv('Cars93.csv', index_col = 0, keep_default_na=False)
# Note the additional keep_default_na parameter which is set to False. This ensures
# that pandas does not intepret the None string in the AirBag column as NaN

# Explore the data
# Get column names
car_data.columns

# Get a random sample of data
car_data.sample(5)

# Get numbers of row and column
car_data.shape

# Get the number of unique manufactures
car_data['Manufacturer'].nunique()

# Select features for scatterplot
scatter_features = pd.DataFrame({'Horsepower': car_data['Horsepower'], 
                                 'Price': car_data['Price']})

# Plot a bar chart showing the number of models in each airbag category
scatter_features.plot.scatter(x='Horsepower', y='Price',
                              legend=False, title="Horsepower vs Price",
                              ylabel="Average price of model", xlabel="Horsepower (max)",
                              color='green')

# Select rows from the dataframe for plotting
x = car_data['Horsepower'].values
y = car_data['Price'].values

# Create a scatterplot
plt.scatter(x, y, color = 'g')
plt.title('Horsepower vs Price')
plt.xlabel('Horsepower (max)')
plt.ylabel('Average Price of model')
plt.show()

# Group data by 'Type'
group_by_type = car_data.groupby(by=['Type'])

# Get the mean (average) for each type across all columns
# Note the mean can only be calculated for numeric values
car_data_avg = round(group_by_type.mean(numeric_only=True), 0)
car_data_avg.sample(5)

# Create a DataFrame of only the relevant features to plot
features_to_plot = pd.DataFrame({'MPG.highway': car_data_avg['MPG.highway'],
                                 'MPG.city': car_data_avg['MPG.city']})

# Plot the average miles per gallon (MPG) for highway
# driving and city driving for each type of car
features_to_plot.plot(kind='bar', ylabel="Average MPG")

car_data['AirBag'].unique()

# Group by 'Airbag' and count models in each airbag category
car_AirBagscount = car_data.groupby('Airbag').count()

# View grouped data
car_AirBagscount

# Create a DataFrame with the first column and all rows
car_AirBagscount = pd.DataFrame(car_AirBagscount.iloc[:, 0])

# Rename the first column to 'Count'
car_AirBagscount.rename(colums={'Manufacturer': 'Count'}, inplace=True)

car_AirBagscount.plot.bar(figsize=(3, 3), legend=False, title="Airbag Count",
                          ylabel="Number of Models", xlabel="Airbag categories",
                          color='purple')



