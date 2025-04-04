from data_loader import load_data
from statistical_analysis import calculate_mean
from visualization import plot_price_evolution, plot_mean_prices

df = load_data()
mean = calculate_mean(df)

plot_price_evolution(df)
plot_mean_prices(mean)
