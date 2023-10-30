import pandas as pd
import matplotlib.pyplot as plt

# Data
df = pd.read_csv("dataset/AllCountries.csv")

# Top 15 PIB + X e Y
top_15_df = df.nlargest(10, columns=['gdp'])
x_values = top_15_df['country']
y_values = top_15_df['gdp']

# Format
plt.figure(figsize=(10, 6))
plt.bar(x_values, y_values)
plt.title('Top 10 PIB por País')
plt.xlabel('País')
plt.ylabel('PIB (em trilhões de dólares)')
plt.xticks(rotation=45)

# Format (valores decimais e adicionar rótulos)
def format_value(value):
    value_str = f'{value:.0f}'
    if len(value_str) >= 4:
        return f'{value_str[:2]}.{value_str[2:4]}'
    else:
        return value_str

for x, y in zip(x_values, y_values): # rótulos
    plt.text(x, y, format_value(y), ha='center', va='bottom')

# Plot
plt.tight_layout()
plt.show()





