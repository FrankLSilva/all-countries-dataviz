import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
df = pd.read_csv("dataset/AllCountries.csv")
y_column = 'life_expectancy'
x_column = 'continent'

# Order boxplot values
group = df.groupby(x_column)[y_column].median()
order = group.sort_values(ascending=True).index

# Set figure
f, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x=y_column, y=x_column, width=.5, order=order, palette="deep")
sns.stripplot(data=df, x=y_column, y=x_column, size=4, linewidth=0,order=order, color=".2")
ax.set(title="Expectativa de Vida por Continente (com observações)",
       xlabel="Expectativa de vida", ylabel="")
# Show
plt.show()


