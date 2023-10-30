from pandas import read_csv
from math import pi
from matplotlib.pyplot import subplot, margins, title, legend, yticks, xticks, ylim, show

# Read data
df = read_csv("dataset/AllCountries.csv").nlargest(5, columns=['gdp'])

# Define columns and labels
df_column1 = "co2_emissions"
df_column2 = "methane_emissions"
df_label1 = "CO2"
df_label2 = "Methane"  # Label for the new column

# Normalize data for the first column
max_val1 = df[df_column1].max()
min_val1 = df[df_column1].min()
df['normalized_data1'] = ((df[df_column1] - min_val1) / (max_val1 - min_val1)) * 100

# Normalize data for the second column
max_val2 = df[df_column2].max()
min_val2 = df[df_column2].min()
df['normalized_data2'] = ((df[df_column2] - min_val2) / (max_val2 - min_val2)) * 100

# Define categories and number of categories
categories = list(df['country'])
N = len(categories)

# Define angles for radar chart
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]



# Define values for the radar chart
values1 = df['normalized_data1'].tolist()
values1 += values1[:1]
values2 = df['normalized_data2'].tolist()
values2 += values2[:1]

# Create a polar plot
ax = subplot(111, polar=True)
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
ax.set_rlabel_position(0)

# Plot data outline and fill / 1st column
ax.plot(angles, values1, color='#FF6969', linewidth=0.5, label=df_label1)
ax.fill(angles, values1, '#FF6969', alpha=0.1)

# Plot data outline and fill / 2nd column
ax.plot(angles, values2, color='#004225', linewidth=0.5, label=df_label2)
ax.fill(angles, values2, '#004225', alpha=0.1)

# Plot formatting
margins(1, 1)
title('Top países por emissão de CO2 e Methane')
legend(loc='upper right', bbox_to_anchor=(-0.03, 0.1))
yticks([10, 30, 50, 70, 100], ["10", "30", "50", "70", "100"], color="k", size=7)
xticks(angles[:-1], categories, color='grey', size=10)
ylim(0, 100)

# Show the plot
show()