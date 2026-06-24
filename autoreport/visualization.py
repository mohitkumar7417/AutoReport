import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


def create_bar_chart(df, category_column, value_column):
    plt.figure(figsize=(6, 4))
    plt.bar(df[category_column], df[value_column])

    plt.title("Sales Analysis Report")
    plt.xlabel(category_column)
    plt.ylabel(value_column)

    plt.tight_layout()
    plt.savefig("reports/sales_chart.png")
    plt.close()

def create_line_chart(df, x_column, y_column, output_file):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 4))
    plt.plot(df[x_column], df[y_column], marker="o")

    plt.title(f"{y_column} by {x_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)

    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

def create_pie_chart(df, label_column, value_column, output_file):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 6))
    
    plt.pie(
        df[value_column],
        labels=df[label_column],
        autopct="%1.1f%%"
    )

    plt.title(f"{value_column} Distribution")

    plt.savefig(output_file)
    plt.close()

def create_scatter_plot(df, x_column, y_column, output_file):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 4))

    plt.scatter(df[x_column], df[y_column])

    plt.title(f"{y_column} vs {x_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)

    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()