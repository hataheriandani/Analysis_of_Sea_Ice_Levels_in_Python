import lightningchart as lc

# Set the license key for LightningChart
lc.set_license('')

# Data for sea ice extent in July 2024
data = [
    {'name': 'Arctic', 'value': 10.9},
    {'name': 'Antarctic', 'value': 11.76}, # Arctic v Antarctic
]

# Create the pie chart
chart = lc.PieChart(
    labels_inside_slices=False,
    title='Sea Ice Extent in June 2024 (Million km²)',
    theme=lc.Themes.White
)

# Add the data slices to the chart
chart.add_slices(data)

# Set the inner radius (optional)
chart.set_inner_radius(50)

# Open the chart in the browser
chart.open()
