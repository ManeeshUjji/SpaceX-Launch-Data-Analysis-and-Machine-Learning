import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

#load data
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

#create dash app
app = dash.Dash(__name__)

#dropdown options for launch site
dropdown_options = [{'label': 'All Sites', 'value': 'ALL'}]
dropdown_options += [{'label': site, 'value': site} for site in spacex_df['Launch Site'].unique()]


#app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

    #dropdown for Launch Site
    dcc.Dropdown(id='site-dropdown',
                 options=dropdown_options,
                 value='ALL',
                 placeholder='Select a Launch Site',
                 searchable=True),
    html.Br(),

    #pie chart for success count
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    #payload range slider
    html.P("Payload range (Kg):"),
    dcc.RangeSlider(id='payload-slider',
                    min=min_payload,
                    max=max_payload,
                    step=1000,
                    marks={int(min_payload): str(int(min_payload)),
                           int(max_payload): str(int(max_payload))},
                    value=[min_payload, max_payload]),
    html.Br(),

    #scatter plot - payload vs success
    html.Div(dcc.Graph(id='success-payload-scatter-chart'))
])

#pie chart callback
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        fig = px.pie(spacex_df,
                     names='Launch Site',
                     values='class',
                     title='Total Success Launches by Site')
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        counts = filtered_df['class'].value_counts().reset_index()
        counts.columns = ['Outcome', 'Count']
        counts['Outcome'] = counts['Outcome'].replace({1: 'Success', 0: 'Failure'})
        fig = px.pie(counts,
                     names='Outcome',
                     values='Count',
                     title=f'Total Success vs Failure for site {selected_site}')
    return fig

#scatter chart callback
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def update_scatter_chart(selected_site, payload_range):
    low, high = payload_range
    mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    filtered_df = spacex_df[mask]

    if selected_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]

    fig = px.scatter(filtered_df,
                     x='Payload Mass (kg)',
                     y='class',
                     color='Booster Version Category',
                     title='Correlation between Payload and Success for ' +
                     ('All Sites' if selected_site == 'ALL' else selected_site))
    return fig

#run app
if __name__ == '__main__':
    app.run()