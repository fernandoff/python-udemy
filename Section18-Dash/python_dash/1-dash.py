from plotly_bar import bar_fig
import dash
from dash import dcc, html

app = dash.Dash()

# app.layout = dcc.Graph(
#     id = 'example-graph',
#     figure = bar_fig
# )

app.layout = html.Div(
    children = [
        html.H1('Sales by Country'),
        dcc.Graph(id='example-graph', figure=bar_fig)
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)