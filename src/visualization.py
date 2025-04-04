import matplotlib.pyplot as plt

def plot_price_evolution(df):
    df = df.sort_values("Data")

    for product in df["Produto"].unique():
        product_data = df[df["Produto"] == product]
        plt.plot(product_data["Data"], product_data["Preço"], label=product)

    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Price Evolution per Product")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_mean_prices(mean_series):
    mean_series.plot(kind="bar", title="Average Price per Product")
    plt.ylabel("Average Price")
    plt.tight_layout()
    plt.show()