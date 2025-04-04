def calculate_mean(df):
    return df.groupby("Produto")["Preço"].mean()

def calculate_price_range(df):
    return df.groupby("Produto")["Preço"].agg(["min", 'max'])

def calculate_std_deviation(df):
    return df.groupby("Produto")["Preço"].std()