import dash
import dash_core_components as dcc
import dash_html_components as html

app=dash.Dash()

app.layout=html.Div([

    html.H1("Hello Dash"),
    html.Div('Dash: A Web Application for Interactive Dashboards'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                {'x':[1,2,3,4,5],'y':[120,90,200,250,98],'type':'line','name':'Series 1'},
                {'x':[1,2,3,4,5],'y':[135,451,859,322,566],'type':'bar','name':'Series 2'}
            ],

            'layout':{
                'title':'First Graph'
            }
        }
    )

])


app.css.append_css({"external_url": "https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css"})

if __name__=='__main__':

    app.run_server(debug=True)