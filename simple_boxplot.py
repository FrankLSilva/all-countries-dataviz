from pandas import read_csv
from seaborn import boxplot
from matplotlib.pyplot import xticks, xlabel, ylabel, title, tight_layout, show, figure

# Data
df = read_csv("dataset/AllCountries.csv")

# Boxplot format
figure(figsize=(10, 6))
boxplot(data=df, x='continent', y='life_expectancy', palette="crest")

# Format details
xticks(rotation=45)
xlabel('Continente')
ylabel('Expectativa de Vida')
title('Boxplot de Expectativa de Vida por Continente')

# Plot
tight_layout()
show()




