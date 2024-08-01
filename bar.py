import pandas as pd
import lightningchart as lc

# Read the license key for LightningChart
lc.set_license(my_license_key)

# Load the dataset
data = pd.read_excel(file_path)

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
