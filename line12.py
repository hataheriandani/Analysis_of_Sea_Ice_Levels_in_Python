import pandas as pd
import lightningchart as lc

# Read the license key for LightningChart
lc.set_license(my_license_key)

# Load the dataset
data = pd.read_csv(file_path)

# Extract year and month from the 'Date' column
data['Year'] = data['Date'].astype(str).str[:4].astype(int)
data['Month'] = data['Date'].astype(str).str[4:].astype(int)

# Create a dictionary to store charts for each month
charts = {}

# Define colors for each chart
colors = [
    lc.Color(0, 0, 255),  # Blue
    lc.Color(255, 0, 0),  # Red
    lc.Color(0, 255, 0),  # Green
    lc.Color(255, 255, 0),  # Yellow
    lc.Color(255, 165, 0),  # Orange
    lc.Color(0, 255, 255),  # Cyan
    lc.Color(255, 0, 255),  # Magenta
    lc.Color(128, 0, 128),  # Purple
    lc.Color(0, 128, 128),  # Teal
    lc.Color(128, 128, 0),  # Olive
    lc.Color(128, 0, 0),    # Maroon
    lc.Color(0, 128, 0)     # Dark Green
]

# Create a chart for each month
for month in range(1, 13):
    # Filter data for the current month
    monthly_data = data[data['Month'] == month]
    
    # Create the chart
    chart = lc.ChartXY(
        theme=lc.Themes.White,
        title=f'Sea Ice Extent for {month} Over the Years '
    )
    
    # Create a line series for the current month
    line_series = chart.add_line_series()
    line_series.set_name(f'Month {month}')
    line_series.set_line_color(colors[month - 1])
    line_series.set_line_thickness(2)
    
    # Customize x-axis
    x_axis = chart.get_default_x_axis()
    x_axis.set_title('Year')
    x_axis.set_decimal_precision(0)
    
    # Customize y-axis
    y_axis = chart.get_default_y_axis()
    y_axis.set_title('Extent (million km)')
    
    # Add a legend to the chart
    chart.add_legend(
        horizontal=False,
        title='Legend',
        x=12, y=42,
        data=chart
    )
    
    # Add data points to the chart
    for _, row in monthly_data.iterrows():
        year = row['Year']
        volume = row['Value']
        line_series.add(year, volume)
    
    # Open the chart
    chart.open(live=True)
    
    # Store the chart in the dictionary
    charts[month] = chart