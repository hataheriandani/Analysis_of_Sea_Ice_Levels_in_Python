import pandas as pd
import lightningchart as lc

# Read the license key for LightningChart
lc.set_license(my_license_key)

# Load the dataset
data = pd.read_csv(file_path)

# Define the year and month columns for plotting
years = data['Year']
months = ['Jan_Value', 'Feb_Value', 'Mar_Value', 'Apr_Value', 'May_Value', 
          'Jun_Value', 'Jul_Value', 'Aug_Value', 'Sep_Value', 'Oct_Value', 
          'Nov_Value', 'Dec_Value']

# Remove rows with NaN values for plotting columns
data = data.dropna(subset=months)

# Create a LightningChart window
chart = lc.ChartXY(
    lc.Themes.White,
    title='Sea Ice Extent Over the Years'
)

# Add a line series for each month
for month in months:
    if month in data.columns:
        line_series = chart.add_line_series()
        line_series.set_name(month)  # Set the name of the series
        
        # Ensure that x and y values are lists of the same length
        x_values = years.tolist()
        y_values = data[month].tolist()
        
        # Check for any missing or invalid data
        if len(x_values) != len(y_values):
            print(f"Data length mismatch for {month}: x_values ({len(x_values)}) vs y_values ({len(y_values)})")
            continue
        
        # Add data to the series
        try:
            line_series.add(x_values, y_values)  # Add data to the series
        except Exception as e:
            print(f"Error adding data for {month}: {e}")
    else:
        print(f"Column {month} not found in data.")

# Customize the chart (titles, labels, etc.)
x_axis = chart.get_default_x_axis()
y_axis = chart.get_default_y_axis()

x_axis.set_title("Year")
x_axis.set_decimal_precision(0)
y_axis.set_title("Extent (million km)")

# Add a legend to the chart
chart.add_legend(
    horizontal=False,
    title='Legend',
    x=12, y=42,
    data=chart
    )

# Display the chart
chart.open()
