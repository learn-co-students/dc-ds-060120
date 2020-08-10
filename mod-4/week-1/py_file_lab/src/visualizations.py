import matplotlib.pyplot as plt

def plot_highest_from_col(df, col, num):
    num_highest = df.sort_values(col, ascending=False).iloc[:num]

    fig, ax = plt.subplots(figsize=(num, 8))
    plt.xticks(rotation=45)
    ax.bar(num_highest["school"], num_highest[col])
    ax.set_title(f"{num} School Fight Songs with Highest {col}")
    ax.set_ylabel(col)
    plt.show()