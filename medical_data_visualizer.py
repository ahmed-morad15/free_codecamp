import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('medical_examination.csv')

# Add overweight column based on BMI
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# Normalize cholesterol and gluc columns
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Create a DataFrame for the categorical plot
df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
df_cat = df_cat.rename(columns={'variable': 'feature', 'value': 'value'})

# Draw the Categorical Plot
def draw_cat_plot():
    fig = sns.catplot(x="feature", hue="value", col="cardio", data=df_cat, kind="count")
    fig.fig.tight_layout()  # Adjust layout to avoid overlap
    return fig

# Clean the data for the heatmap
df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
]

# Calculate the correlation matrix
corr = df_heat.corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Plot the Heatmap
def draw_heat_map():
    fig = sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap="coolwarm", cbar_kws={'label': 'Correlation Coefficient'})
    return fig
