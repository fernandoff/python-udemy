import dash
from dash import dcc, html
from datetime import datetime

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.Img(src="https://github.com/fernandoff.png", style={
            'width':'100px',
            'border-radius':'175px',
            'display':'block',
        }),
        html.Hr(),
        html.H1("Testando Dash com HTML"),
        html.Span(
            children= [
                f'Hoje é {datetime.now().date()}',
                html.Br(),
                'Desenvolvido por ', html.B('Rodrigo Macedo'),
                html.Br(),
                html.I('Instrutor Cursos Tecnologia')
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)