import pandas as pd
import matplotlib.pyplot as plt


def Build_line_plot(CSV_to_Read):
    """
    Create a line plot with multiple lines based on data from a CSV file.

    Parameters:
    - CSV_to_Read (str): The file path to the CSV file containing the data.

    Returns:
    returns no values but the line plot will be generated.
    """
    # Load the dataset from the CSV file
    data = pd.read_csv(CSV_to_Read)

    # Getting the data of country codes and years
    # Fetched the country codes from the CSV
    countries = data['Country Name']
    # data of years initiates from column 2
    years = data.columns[1:]

    # generate a line plot with multiple lines
    plt.figure(figsize=(10, 6))
    for idx in range(len(countries)):
        # referring to the data from column 2 till end
        plt.plot(years, data.iloc[idx, 1:], label=countries[idx])

    # Adding plot title and axis labels to append to the graphs.
    plt.title('Comparing Nations: CO2 Emission Profiles of Leading Nations')
    plt.xlabel('Years')
    plt.ylabel('CO2 Emitted')

    # Adding legend
    plt.legend()

    # Displaying the plot to save
    plt.show()


# Calling the function to create the Line plot
CSV_to_Read = r'C:\Users\Avinash Reddy\Videos\ADS1Assgn\Prasanna\Co2_Emission.csv'
Build_line_plot(CSV_to_Read)
