import pandas as pd
from lightningchart import ChartXY, set_license

# Set the license
set_license('')

# Load the data
data = pd.read_csv(file_path)

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