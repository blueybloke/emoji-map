# -*- coding: utf-8 -*-

import json
import asyncio
import aiohttp

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

df = pd.DataFrame()
url = 'https://stream.emojitracker.com/subscribe/eps'
# Start the dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


async def update_df():
    async with aiohttp.request('get',url) as r:
        for line in r.content:
            line = json.loads(line[0])
            for (k, v) in line:
                df[k] += v


# Define the bar chart
@app.callback(Output('live-update-graph', 'children'),
                [Input('interval-component', 'n_intervals')])
def update_bar_chart(n):
    return go.bar(data)

app.layout = html.Div(
    dcc.Graph(id='live-update-graph'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,
        n_intervals=0
    )
)

app.run_server(debug=True)