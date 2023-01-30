import pandas as pd
import matplotlib.pyplot as plt
import math

extracted_data = pd.read_csv("Task4a_data.csv")

print(extracted_data.to_string())

most_popular_by_month = extracted_data.groupby(extracted_data["Month"]).mean()
print(extracted_data["Month"])
print(most_popular_by_month)

new_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

most_popular_by_month = most_popular_by_month.reindex(new_order, axis=0)

plt.plot(most_popular_by_month.drop(['Commission (%)'], axis=1))
plt.legend(["Mean Price"])
plt.ylabel("Price")
plt.xlabel("Months")
plt.title("Mean price from months")
plt.show()