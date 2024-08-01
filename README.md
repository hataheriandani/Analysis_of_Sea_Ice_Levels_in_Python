## Analysis of Sea Ice Levels in Python

#### Introduction
Climate change is a global phenomenon significantly impacting the earth’s weather patterns. One of the most critical consequences of climate change is the alteration in sea ice levels. The Arctic region, in particular, is experiencing drastic temperature variations leading to changes in sea ice extent. This phenomenon is known as polar amplification, where the Arctic warms at a faster rate compared to the rest of the world. Monitoring and visualizing sea ice levels is crucial for understanding these changes and their global implications.

#### LightningChart Python
LightningChart for Python is a powerful data visualization library that offers various features for creating complex and high-performance charts. It supports different chart types, including bar charts, line charts, pie charts, and more, making it an ideal choice for visualizing sea ice levels. Its performance characteristics ensure smooth and responsive visualizations even with large datasets.

#### Setting Up Python Environment
To set up the Python environment for sea ice level visualization, you need to install Python and the necessary libraries. The primary libraries used in this project are:
- **Pandas**: For data manipulation.
- **LightningChart**: For creating high-performance charts.
You can install these libraries using pip:

```bash
pip install numpy pandas lightningchart pycountry
```
Setting up the development environment involves creating a virtual environment, installing the libraries, and setting up the license for LightningChart.

#### Loading and Processing Data
Loading data files into your Python environment is the first step in the analysis process. You can use Pandas to read data from various file formats like CSV and Excel. Here's an example of loading and processing data from an Excel file:

```bash
import pandas as pd
import lightningchart as lc

# Read the license key for LightningChart
my_license_key = 'Your license_key  '
lc.set_license(my_license_key)

# Load the dataset
file_path = 'The_maximum_ice extent_in_the_Baltic_Sea.xlsx'
data = pd.read_excel(file_path)
```
Handling and preprocessing the data involves cleaning the data, handling missing values, and preparing it for visualization.

#### Visualizing Data with LightningChart
In this section, we delve into how LightningChart can be used to visualize sea ice extent data. Visualization is a crucial part of data analysis as it helps in understanding trends, patterns, and anomalies that might not be obvious from raw data.

#### Bar Chart: Maximum Ice Extent in the Baltic Sea

A bar chart is used to visualize the maximum ice extent in the Baltic Sea from 1991 to 2024. The following code demonstrates how to create a bar chart with LightningChart:

```bash

# Convert data to JSON serializable format
data_list = [{'category': str(row['year']), 'value': int(row['extent']) } for index, row in data.iterrows()]

# Create bar chart
bar_chart = lc.BarChart(
    theme=lc.Themes.Dark,
    title='The maximum ice extent in the Baltic Sea (1991-2024)'
)

# Set sorting and data
bar_chart.set_sorting('disabled')
bar_chart.set_data(data_list)

# Open the chart in the browser
bar_chart.open()

```

![barchart](/images/bar.png)

The bar chart visualizes the maximum ice extent in the Baltic Sea from 1991 to 2024. From the data, it is evident that there is significant variability in the ice extent over the years. Notably, there are peaks in 1995, 2011, and 2006, indicating years with higher ice extents. Conversely, years like 2007 and 2014 show much lower ice extents. This variability can be attributed to various climatic factors influencing the Baltic Sea's ice coverage annually.


#### Line Chart: Monthly Sea Ice Extent

A line chart is used to visualize the average sea ice extent for different months over the years. Here is the code to create such a chart:

```bash


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
```

![line chart](/images/line.png)

The single month line chart shows the sea ice extent for a specific month over the years. This focused view helps in identifying the trends and anomalies for that particular month. The data highlights how the ice extent fluctuates year by year, with some years experiencing higher extents and others significantly lower, reflecting short-term climatic variations.


#### Line Chart
We also created individual line charts for each month to provide a clearer view of sea ice extent trends throughout the years. Here’s the Python code used:

```bash
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

```
![line chart](/images/line12.gif)

These individual monthly charts help to drill down into specific seasonal trends and identify any anomalies or significant changes over the years.

#### Real-Time Line Chart
To visualize sea ice extent data in real-time, we used a real-time line chart. This type of chart is useful for monitoring current data and observing live trends.

```bash

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

```

![live](/images/live.gif)

This real-time line chart dynamically displays data as it is added, providing an up-to-date view of sea ice extent changes.

#### Multi-line Chart
A multi-line chart can display data from different seasons or months in one chart. The code below demonstrates how to create a multi-line chart:

```bash

# Prepare the data for the selected months (first month of each season)
months = ['Jan', 'Apr', 'Jul', 'Oct']
month_columns = [f'{month}_Value' for month in months]

# Extract data for the selected months
data_selected_months = data[['Year'] + month_columns]

# Create the chart
chart = ChartXY(
    title= 'Sea Ice Extent Over the Years '
)

# Dispose the default y-axis
chart.get_default_y_axis().dispose()

# Customize axes
axis_x = chart.get_default_x_axis()
axis_x.set_title('Year')
axis_x.set_decimal_precision(0)

# Add y-axes and line series for each selected month
for i, month in enumerate(months):
    axis_y = chart.add_y_axis(stack_index=i)  # increasing stack_index will create stacked axes
    axis_y.set_margins(15 if i > 0 else 0, 15 if i < 3 else 0)  # optional margin space
    axis_y.set_title(title=month)
    
    
    series = chart.add_line_series(y_axis=axis_y, data_pattern='ProgressiveX')
    series.add(
        x=data_selected_months['Year'].tolist(),
        y=data_selected_months[f'{month}_Value'].tolist()
    )

# Open the chart
chart.open()
```

![line](/images/lines.png)

This multi-line chart displays the average sea ice extent for each month over several years. The data illustrates the seasonal patterns in sea ice extent, with the highest extents typically occurring during winter months (December to February) and the lowest during summer months (June to August). The overall trend also indicates a slight decline in sea ice extent over the years, which aligns with global warming and climate change patterns.

#### Dashboard
In this chart, you can observe the sea ice extent for different seasons over the years.

```bash
# Prepare the data for the selected months for each season
seasons = {
    'Winter': ['Dec', 'Jan', 'Feb'],
    'Spring': ['Mar', 'Apr', 'May'],
    'Summer': ['Jun', 'Jul', 'Aug'],
    'Autumn': ['Sep', 'Oct', 'Nov']
}

# Create the dashboard
dashboard = lc.Dashboard(
    rows=2,
    columns=2,
    theme=lc.Themes.Dark
)

# Function to plot each season's data
def plot_season_data(dashboard, season, months, column_index, row_index):
    chart = dashboard.ChartXY(
        title=f'Values for {season}',
        column_index=column_index,
        row_index=row_index
    )
    
    # Customize axes
    axis_x = chart.get_default_x_axis()
    axis_x.set_title('Year')
    axis_x.set_decimal_precision(0)
    
    colors = [lc.Color(0, 0, 255), lc.Color(255, 255, 0), lc.Color(0, 255, 0)]
    
    for i, month in enumerate(months):
        series = chart.add_line_series()
        series.set_name(month)
        series.set_line_color(colors[i])
        series.add(
            x=data['Year'].tolist(),
            y=data[f'{month}_Value'].tolist()
        )
    
    legend=chart.add_legend(
        horizontal=False,
        title='Legend',
        data=chart
    )

# Plot data for each season
plot_season_data(dashboard, 'Winter', seasons['Winter'], 0, 0)
plot_season_data(dashboard, 'Spring', seasons['Spring'], 1, 0)
plot_season_data(dashboard, 'Summer', seasons['Summer'], 0, 1)
plot_season_data(dashboard, 'Autumn', seasons['Autumn'], 1, 1)

# Open the dashboard
dashboard.open()

```
![dashbord](/images/dashbord.png)

The dashboard comprises four line charts, each representing one of the four seasons. The charts provide a detailed view of how sea ice extent changes throughout the different times of the year:
- Winter (Dec, Jan, Feb): Shows the highest ice extents, with a gradual decrease over the years.
- Spring (Mar, Apr, May): Displays a transition from high to lower extents as the season progresses.
- Summer (Jun, Jul, Aug): Exhibits the lowest ice extents, reflecting the melting period.
- Autumn (Sep, Oct, Nov): Indicates the reformation of sea ice, with extents increasing towards the end of the season.
The seasonal charts collectively illustrate the cyclical nature of sea ice coverage and the impact of warming temperatures on the extent and duration of sea ice.

#### Pie Chart
In this chart, you can easily compare the sea ice extent in the Northern and Southern Hemispheres.

```bash
# Convert data to JSON serializable format
data_list = [{'category': str(row['year']), 'value': int(row['extent'])} for index, row in data.iterrows()]

# Create bar chart
bar_chart = lc.BarChart(
    theme=lc.Themes.Dark,
    title='The maximum ice extent in the Baltic Sea (1991-2024)'
)

# Set sorting and data
bar_chart.set_sorting('disabled')
bar_chart.set_data(data_list)

# Open the chart in the browser
bar_chart.open()

```
![pie](/images/pie.png)

The pie chart compares the sea ice extent between the Arctic and Antarctic regions in June 2024. The data shows that the Antarctic region has a slightly larger ice extent compared to the Arctic. 

## Conclusion
#### Recap of Creating the Application and Its Usefulness
- **Bar Chart**: This visualization helps compare sea ice extent across different categories or time periods. It provides a clear, straightforward way to view and compare the magnitude of sea ice extent immediately.
- **Monthly Line Chart**: This chart displays sea ice extent over time, showing trends and patterns month by month. It is useful for observing how sea ice extent changes within each year and tracking long-term trends.
- **Multi-Line Chart**: This type of chart enables comparison between multiple datasets or categories over the same time period. For instance, it can be used to compare sea ice extent across different seasons or years, highlighting variations and trends between them.
- **Real-Time Timeline Chart**: This chart provides a dynamic view of sea ice extent data as it evolves over time. It is particularly useful for monitoring and analyzing real-time data, allowing users to track changes and trends as they occur.
- **Dashboard**: The dashboard integrates multiple charts into a single interface, allowing for a comprehensive view of the data. It includes seasonal charts (Winter, Spring, Summer, Autumn) that facilitate an easy comparison of sea ice extent across different seasons and years.
- **Pie Chart**: This visualization is used to compare sea ice extent between the Northern and Southern Hemispheres for a specific month. It offers an intuitive way to visualize proportions and differences between these regions.
Benefits of Using LightningChart Python for Visualizing Data
#### Using LightningChart Python for data visualization comes with several advantages:
- **Ease of Use:** LightningChart's Python library simplifies the creation of various charts and visualizations with minimal code. The intuitive API and comprehensive documentation make it accessible even for those with basic programming knowledge. For instance, creating a complex dashboard or a detailed pie chart requires only a few lines of code, allowing users to focus more on data analysis rather than the intricacies of visualization design.
- **High Performance:** LightningChart is known for its high performance and ability to handle large datasets smoothly. This ensures that even with extensive data, the visualizations remain responsive and quick, providing a seamless user experience.
- **Customizability:** The library offers extensive customization options for charts, axes, legends, and other components. Users can tailor the appearance and behavior of their visualizations to meet specific requirements, ensuring that the final output is both informative and aesthetically pleasing.
- **Interactivity:** Charts created with LightningChart are interactive by default. Users can zoom, pan, and hover over data points to get more details. This interactivity makes the data exploration process more engaging and insightful.
- **Cross-Platform Compatibility:** Visualizations created using LightningChart can be easily embedded in web applications, desktop applications, or presented as standalone charts. This versatility makes it suitable for a wide range of applications, from academic research to business analytics.

In conclusion, LightningChart Python is an excellent tool for creating high-quality, interactive data visualizations with ease. Its combination of performance, customizability, and ease of use makes it an ideal choice for both developers and data scientists looking to visualize complex datasets effectively.


### Sources

- [LightningChart](https://lightningchart.com/python-charts/docs/charts/)
- [Finnish Meteorological Institute](https://en.ilmatieteenlaitos.fi/icestatistics)
- [NOAA National Centers for Environmental Information](https://www.ncei.noaa.gov/access/monitoring/snow-and-ice-extent/sea-ice/G/0)
- [Our World in Data](https://ourworldindata.org/grapher/arctic-sea-ice?time=earliest..2024)
