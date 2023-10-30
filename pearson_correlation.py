from seaborn import lmplot
from numpy import array, corrcoef
from pandas import read_csv, DataFrame
from matplotlib.pyplot import title, xlabel, ylabel, tight_layout, show, subplots

# Data
df = read_csv("dataset/AllCountries.csv")
x_column = 'birth_rate'
y_column = 'fertility_rate'

# Creates lists of X and Y for correlation:
x_array = array((df[x_column].fillna(0)).tolist())
y_array = array((df[y_column].fillna(0)).tolist())

# Pearson correlation for two datasets/columns
p_corr = corrcoef(x_array, y_array)
print(p_corr)

# Graph edit
corr_df = DataFrame({'X': x_array, 'Y': y_array})
lmplot(x='X', y='Y', data=corr_df, aspect=1.35)
title('Correlação de Pearson')
xlabel('Taxa de Fertilidade')
ylabel('Taxa de Natalidade')

# Plot
tight_layout()
show()