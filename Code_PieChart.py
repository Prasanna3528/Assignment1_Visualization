import pandas as pd
import matplotlib.pyplot as plt


def Build_pie_chart(CSV_to_Read):
    """
    Generate a pie chart to visualize the distribution of Earth

    Parameters:
    - CSV_to_Read (str): The file path to the CSV file containing the data.

    Returns:
    returns no values but pie chart will be generated
    """
    # Load the dataset from the CSV file
    data = pd.read_csv(CSV_to_Read)

    # Get the data of Percentages
    percent = data.iloc[:, 1]  # Percentages are in the 1st column.

    # Get the data of Types
    types = data['Covered by']

    # Creating a pie chart using the data.
    plt.figure(figsize=(8, 6))
    plt.pie(percent, labels=types)
    plt.title('Surface Area of Earth')

    # Display the plot
    plt.show()


# Pass CSV File to generate data
CSV_to_Read = r'C:\Users\Avinash Reddy\Videos\ADS1Assgn\Prasanna\Earth_Coverage.csv'
Build_pie_chart(CSV_to_Read)
