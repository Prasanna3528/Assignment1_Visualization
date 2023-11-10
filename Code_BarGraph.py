import pandas as pd
import matplotlib.pyplot as plt


def Build_bar_chart(csv_to_read):
    """
    Generates a bar chart of CO2 emissions in the year 2020
    based on data from a CSV file.

    Parameters:
    - csv_to_read (str): The path to the CSV file 
    containing CO2 emissions data.

    Returns:
    returns no values but the Bar chart is generated
    """
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(csv_to_read)

    # Extract country names and CO2 emissions for the year 2020
    countries = data.iloc[:, 0]
    co2_emissions_2020 = data.iloc[:, -1]

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(countries, co2_emissions_2020)
    
    # Adding labels to the Bar graph
    plt.xlabel('Countries')
    plt.ylabel('CO2 Emissions in 2020 (in metric kilotons)')
    plt.title('CO2 Emissions in 2020 by Country')
   
    # Show the bar chart
    plt.show()


# Pass CSV file to function
csv_to_read = r'C:\Users\prasanna_chowdary_0\OneDrive\Desktop\AD1 Assignment\Co2_Emission.csv'
Build_bar_chart(csv_to_read)
