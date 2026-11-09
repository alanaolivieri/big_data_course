"""Ejecutar con python apps/app_dash.py desde PySpark."""

from dash import Dash, Input, Output, dcc, html

from panel_siniestros import MESES, TODOS, cargar_datos, distritos, figura_panel


def crear_app(datos):
    app = Dash(__name__)
    app.title = 'Panel de siniestros'
    app.layout = html.Main([
        html.H1('Siniestros de tráfico en Barcelona'),
        html.Label('Distrito'),
        dcc.Dropdown(distritos(datos), TODOS, id='distrito', clearable=False),
        html.Label('Periodo'),
        dcc.RangeSlider(1, 12, 1, value=[1, 12], id='periodo',
                        marks={m: MESES[m - 1][:3] for m in range(1, 13)}),
        dcc.Graph(id='panel'),
        html.P('Para comparar riesgo entre zonas hace falta medir la exposición al tráfico.'),
    ], style={'maxWidth': '1100px', 'margin': 'auto', 'padding': '1rem', 'fontFamily': 'sans-serif'})

    @app.callback(Output('panel', 'figure'), Input('distrito', 'value'), Input('periodo', 'value'))
    def actualizar(distrito, periodo):
        return figura_panel(datos, distrito, periodo)

    return app


if __name__ == '__main__':
    crear_app(cargar_datos()).run(host='127.0.0.1', debug=False)
