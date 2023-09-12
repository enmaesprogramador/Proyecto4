import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


data = pd.read_csv("epa-sea-level.csv")


plt.figure(figsize=(12, 6))
plt.scatter(data["Year"], data["CSIRO Adjusted Sea Level"], label="Data", alpha=0.6)


slope, intercept, r_value, p_value, std_err = linregress(data["Year"], data["CSIRO Adjusted Sea Level"])


year_range = range(1880, 2051)
line_fit = [(slope * year + intercept) for year in year_range]
plt.plot(year_range, line_fit, color="red", label="Best Fit Line")

recent_data = data[data["Year"] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data["Year"], recent_data["CSIRO Adjusted Sea Level"])
line_fit_recent = [(slope_recent * year + intercept_recent) for year in year_range]
plt.plot(year_range, line_fit_recent, color="green", label="Best Fit Line (2000-Present)")


plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.legend()


plt.savefig("sea_level_rise.png")


plt.show()