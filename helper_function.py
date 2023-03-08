
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


def get_parameters(eps_range, min_samples_range, X):
    Gene.X = X
    data = [eps_range, min_samples_range]
    population = Population(data)

    for _ in range(50):
        
        population.elite_populatio()
        population.cross_over()
        population.nex_iter()

    return max(population.old_population)



def get_indicator(indicator_val=0):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = indicator_val,
        title = {'text': "Silhouette Score"},
        domain = {'x': [0, 1], 'y': [0, 1]}
    ))

    return fig

def get_graph(title, original_data, kargs):
    graph1 = go.Figure(data=[go.Scatter(x=original_data[:, 0], y=original_data[:, 1],
                                                mode='markers',
                                                marker=kargs 
                                            )
                                ]
                            )

    graph1.update_layout(
        xaxis_title='first PCA component',
        yaxis_title='second PCA component',
        title=title
    )

    return graph1