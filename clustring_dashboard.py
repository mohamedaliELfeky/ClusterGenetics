# importing modules
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from flask import Flask

import plotly.express as px
import plotly.graph_objects as go
from plotly.data import iris

from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

from Genatics_hyperprameter_tuning import Population, Gene
import helper_function as hf

# read data
X = iris().drop(['species', 'species_id'], axis=1)

# intiate app

server = Flask(__name__)

app = Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

# read files

original_data1 = PCA(n_components=2).fit_transform(X)


# Build Components

header_component = html.H1('Clustring visualization DBscan', style={'display': 'flex',
  'justify-content': 'center',
  'align-items': 'center',
  'color':'#9191FF'
})

# graph

graph1 = hf.get_graph('Data before clustring', original_data1, None)

# indicator

fig = hf.get_indicator(0)

# Design app layout

app.layout = html.Div(
    [
        dbc.Row(
            [
                header_component
            ]
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col([dbc.Label("Enter eps range: ",  style={'font-size':'25px',
                                                                 'color':'#9191F1',
                                                                 'padding-left': 10})]),
                dbc.Col([dbc.Input(id='eps1', placeholder="from", type="number", value=0.1)], style={'padding-right': 100}),
                dbc.Col([dbc.Input(id='eps2', placeholder="to", type="number", value=2)], style={'padding-right': 300})
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col([dbc.Label("Enter min_samples range: ",  style={'font-size':'25px',
                                                                 'color':'#9191F1',
                                                                 'padding-left': 10})]),
                dbc.Col([dbc.Input(id='min_samples1', placeholder="from", type="number", value=2)], style={'padding-right': 100}),
                dbc.Col([dbc.Input(id='min_samples2', placeholder="to", type="number", value=20)], style={'padding-right': 300}),
                
            ]
        ),
        html.Br(),
        html.Div([dbc.Button(
                    "Submit",
                    id="submit_btn",
                    n_clicks=0,
                    style={
                        'width':'10%'
                    }
                    
                )], style={'justify-content': 'right',

                            'display': 'flex'}
            ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col([dcc.Graph(id='original_data', figure=graph1)]),

                dbc.Col([
                            dcc.Graph(id='clustered_data'),
                            dcc.Graph(id='accuracy', figure=fig)
                        ]
                    )
            ]
        )
    
    ]
)



@app.callback(
    Output('clustered_data', 'figure'),
    Output('accuracy', 'figure'),
    Input('submit_btn', 'n_clicks'),
    State('eps1', 'value'),
    State('eps2', 'value'),
    State('min_samples1', 'value'),
    State('min_samples2', 'value')
)
def submit_values(n_clicks, eps1, eps2, min_samples1, min_samples2):
    print(eps1, eps2, min_samples1, min_samples2)

    if eps1 and eps2 and min_samples1 and  min_samples2:
        # print('here1')
        eps, min_sample = hf.get_parameters([eps1, eps2], [min_samples1, min_samples2], X)
        # print('here2', eps, min_sample)
        dbscan = DBSCAN(eps=eps.gene, min_samples=min_sample.gene)
        labels = dbscan.fit_predict(X)
        silhouette = 0

        try:
            print('here3')
            silhouette = silhouette_score(X, labels)
        except:
            print('wrong')
            return None , fig


        out_fig = hf.get_graph("Clustred Data", original_data1, dict(
                                                                color=labels,
                                                                colorscale='Viridis',
                                                                showscale=True
                                                                )
                                )


        
        out_indicator = hf.get_indicator(silhouette)

        print('here5')
        return out_fig , out_indicator

    print('here6')
    return None , fig

if __name__ == '__main__':
    # run app
    app.run_server(debug=True)