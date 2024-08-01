import pandas as pd
import lightningchart as lc
import time

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

# Create the chart
chart = lc.ChartXY(
    theme=lc.Themes.Dark,
    title='Sea Ice Extent Over the Years'
)

# Define colors for each month
colors = [
    lc.Color(0, 0, 255),     # Blue for January
    lc.Color(0, 255, 255),   # Cyan for February
    lc.Color(0, 128, 0),     # Green for March
    lc.Color(128, 128, 0),   # Olive for April
    lc.Color(255, 255, 0),   # Yellow for May
    lc.Color(255, 165, 0),   # Orange for June
    lc.Color(255, 0, 0),     # Red for July
    lc.Color(139, 69, 19),   # Brown for August
    lc.Color(128, 0, 128),   # Purple for September
    lc.Color(238, 130, 238), # Violet for October
    lc.Color(128, 128, 128), # Grey for November
    lc.Color(0, 0, 0)        # Black for December
]

# Create a line series for each month
line_series_dict = {}
for i, month in enumerate(months):
    line_series = chart.add_line_series()
    line_series.set_name(month)
    line_series.set_line_color(colors[i])
    line_series.set_line_thickness(2)
    line_series_dict[month] = line_series

# Customize x-axis
x_axis = chart.get_default_x_axis()
x_axis.set_title('Year')
x_axis.set_decimal_precision(0)

# Customize y-axis
y_axis = chart.get_default_y_axis()
y_axis.set_title('Ice Extent (million square km)')

# Add a legend to the chart
chart.add_legend(
horizontal=False,
title='Months',
x=12, y=42,
data=chart
)

# Open the chart
chart.open(live=True)

# Add data points with a delay to simulate real-time drawing
for index, row in data.iterrows():
    year = row['Year']
    for month in months:
        volume = row[month]
        if pd.notna(year) and pd.notna(volume):
            print(f"Adding data for {month}: Year={year}, Volume={volume}")
            line_series_dict[month].add(year, volume)
            time.sleep(0.01)  # 0.01 second delay between each data point

chart.close()
