import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/AllCountries.csv")

top_10_df = df.nlargest(10, columns=['land_area'])
top_10_df = top_10_df.sort_values(by='land_area', ascending=False)

x_values = top_10_df['country']
y_agricultural = top_10_df['agricultural_land']
y_forest = top_10_df['forest_area']
y_rural = top_10_df['rural_land']
y_urban = top_10_df['urban_land']

plt.figure(figsize=(10, 6))
plt.title('Top 15 por Área de Agricultura')
plt.xlabel('País')
plt.ylabel('Área')
plt.xticks(rotation=45)

plt.bar(x_values, y_urban, label="Urbano", color="#3D5656")
plt.bar(x_values, y_agricultural, bottom=y_urban, label="Agricultura", color="#61876E")
plt.bar(x_values, y_forest, bottom=y_agricultural, label="Floresta", color="#A6BB8D")
plt.bar(x_values, y_rural, bottom=y_forest, label="Rural", color="#EAE7B1")

plt.legend(loc=1)
plt.tight_layout()
plt.show()