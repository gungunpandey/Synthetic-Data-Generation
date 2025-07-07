import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure output directories exist
os.makedirs('outputs/plots', exist_ok=True)
os.makedirs('results', exist_ok=True)

datasets = [
    ('Dataset 1.csv', 'Dataset 1'),
    ('Dataset 2.csv', 'Dataset 2'),
    ('Dataset 3.csv', 'Dataset 3'),
]

for file, name in datasets:
    results = []
    results.append(f'===== {name} =====\n')
    df = pd.read_csv(file)

    # Basic info
    results.append(f'Shape: {df.shape}\n')
    results.append(f'Columns: {df.columns.tolist()}\n')
    results.append('Data types:\n')
    results.append(f'{df.dtypes}\n')

    # Missing values
    results.append('Missing values:\n')
    results.append(f'{df.isnull().sum()}\n')

    # Descriptive statistics
    results.append('Descriptive statistics:\n')
    results.append(f'{df.describe()}\n')

    # Save results to text file
    with open(f'results/{name}_eda.txt', 'w') as f:
        for line in results:
            f.write(str(line) + '\n')

    # Save descriptive stats to CSV
    df.describe().to_csv(f'outputs/plots/{name}_describe.csv')

    # Histograms
    df.hist(bins=30, figsize=(15, 10))
    plt.suptitle(f'{name} - Histograms')
    plt.tight_layout(rect=(0, 0, 1, 0.97))
    plt.savefig(f'outputs/plots/{name}_histograms.png')
    plt.close()

    # KDE plots
    for col in df.columns:
        plt.figure()
        data_1d = df[col].dropna().to_numpy().ravel()
        sns.kdeplot(data_1d, fill=True)
        plt.title(f'{name} - KDE of {col}')
        plt.savefig(f'outputs/plots/{name}_kde_{col}.png')
        plt.close()

    # Correlation matrix
    corr = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title(f'{name} - Correlation Matrix')
    plt.tight_layout()
    plt.savefig(f'outputs/plots/{name}_correlation.png')
    plt.close()

    # Pairplot (sampled for speed)
    if len(df) > 1000:
        sample_df = df.sample(1000, random_state=42)
    else:
        sample_df = df
    sns.pairplot(sample_df)
    plt.suptitle(f'{name} - Pairplot', y=1.02)
    plt.savefig(f'outputs/plots/{name}_pairplot.png')
    plt.close()

print('\nEDA complete. Plots and stats saved in outputs/plots/ and results/') 