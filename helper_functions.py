import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def class_distr(class_col: str, df: pd.DataFrame):
    total_samples = df.count()
    print("Total number of samples:")
    print(total_samples)

    class_distr = df.groupby(class_col)[class_col].count()
    print("\nclass distribution:")
    print(class_distr)

    percentage_distr = class_distr.div(class_distr.sum()).round(2)
    print("\n class distribution in %:")
    print(percentage_distr)

    percentage_distr.plot(kind="bar", title="Class distribution", xlabel="class", ylabel="percentage")

def words_per_sample(list_of_texts: list):
    
    num_words = [len(s.split()) for s in list_of_texts]
    return np.median(num_words)

def plot_sample_length_distr(sample_texts):
    """Plots the sample length distribution.
    """
    plt.hist([len(s) for s in sample_texts], 50)
    plt.xlabel('Length of a sample')
    plt.ylabel('Number of samples')
    plt.title('Sample length distribution')
    plt.show()