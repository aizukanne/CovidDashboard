import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import covid

countries = covid.getCountries()

df = covid.getNewData()
#print(df)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

	html.H1("International COVID-19 Dashboard", style={'text-align': 'center'}),

    dcc.Dropdown(
        id='select-country',
        options=[
            {'label': c, 'value': c} for c in countries
        ],
        #multi=True,
        placeholder="Select a country",
        style={'width': "30%"}
    ),
    html.Div(id='dd-output-container', children=[]),
    html.Br(),

    dcc.Graph(id='world_map', figure={})
])

@app.callback(
    [Output(component_id='dd-output-container', component_property='children'),
    Output(component_id='world_map', component_property='figure')],
    [Input(component_id='select-country', component_property='value')]
)
def update_output_div(input_value):
	container = "The map shows information for: {}".format(input_value)
	df.reset_index(drop=True)
	
	# Plotly Express
	fig = px.choropleth(
    	data_frame=df,
        labels={'cases.new':'New', 'cases.active':'Active', 'deaths.total':'Deaths', 'cases.total':'Cases','tests.total':'Tests'},
        locations='country',
        locationmode='country names',
        title="Covid Map",
        color='cases.active',
        range_color=[10,100000],
        hover_data=['cases.new', 'cases.active', 'deaths.total', 'cases.total', 'tests.total'],
        hover_name='country',
        custom_data=['continent'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        height=960,
        projection='natural earth',
        template='plotly'
    )
	return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)
