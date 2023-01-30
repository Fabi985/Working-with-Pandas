import pandas as pd
import matplotlib.pyplot as plt

#This extracts all of the data from the CSV file
extracted_data = pd.read_csv("Task4a_data.csv")

#Pints it as string
print(extracted_data.to_string())

#Groups the "month" column together
most_popular_by_month = extracted_data.groupby(extracted_data["Month"]).mean()
print(extracted_data["Month"])
print(most_popular_by_month)

#/This part is for ordering the months in the correct format\#
new_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

most_popular_by_month = most_popular_by_month.reindex(new_order, axis=0)
#-----------------------------------------------------------------------------------------------------------------------------------------#

#This creates a plot for the data "most_popular_by_month" and drops the "Commission (%)" column
plt.plot(most_popular_by_month.drop(['Commission (%)'], axis=1))

#Displays the "meaning" of the colour on gaph
plt.legend(["Mean Price"])

#The labels and title
plt.ylabel("Price")
plt.xlabel("Months")
plt.title("Mean price from months")
#----------------------------------#

#Displays the graph
plt.show()