# Dynamic Graph based on User Input

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import  Input,Output
import pandas_datareader.data as web
import datetime


app=dash.Dash()


#Layout


app.layout=html.Div([
    html.H1('Symbol to Graph!'),
    dcc.Input(id='input',value='',type='text'),
    html.Div(id='output-graph')

])


# Function
# get the data based on input and return a graph

@app.callback(
    Output('output-graph','children'),
    [Input('input','value')]
)
def update_value(input):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(input, 'morningstar', start, end)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    df = df.drop("Symbol", axis=1)

    return dcc.Graph(
        id='example-graph',
        figure ={
            'data':[
                {'x':df.index,'y':df.Close,'type':'line','name':input}
            ],
            'layout':{'title':input}

        }

    )


# Main Function

if __name__ == '__main__':
    app.run_server(debug=True)