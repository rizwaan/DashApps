## Demoes UI interactivity

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import  Input,Output

app=dash.Dash()

#Layout


app.layout=html.Div([
    dcc.Input(id="inputTxtBox",value="Enter stuff here!",type="text"),
    html.Div(id="outputlabel")
])

# Function

@app.callback(
    Output(component_id='outputlabel',component_property='children'),
    [Input(component_id='inputTxtBox',component_property='value')]
)
def update_value(input_data):
    return 'Input: {}'.format(input_data)

# Main Function

if __name__ == '__main__':
    app.run_server(debug=True)