import pandas as pd
import lightningchart as lc

# Set the license
lc.set_license('')
# Load the data
data = pd.read_csv(file_path)
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