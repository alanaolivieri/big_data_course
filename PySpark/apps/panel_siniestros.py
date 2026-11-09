"""Datos y figura compartidos por el notebook, Streamlit y Dash."""

from pathlib import Path

import pandas as pd

ARCHIVO = 'resumen_siniestros_panel.csv'
TODOS = 'Todos los distritos'
DIAS = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
MESES = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']


def cargar_datos():
    inicio = Path.cwd()
    carpetas = [inicio, inicio / 'data', inicio.parent / 'data',
                inicio / 'PySpark' / 'data', Path(__file__).resolve().parent.parent / 'data']
    ruta = next((p / ARCHIVO for p in carpetas if (p / ARCHIVO).is_file()), None)
    if ruta is None:
        raise FileNotFoundError(f'No encuentro {ARCHIVO}. Ejecuta la exportación del notebook 16.')
    return pd.read_csv(ruta, parse_dates=['fecha'])


def distritos(datos):
    return [TODOS, *sorted(datos['distrito'].unique())]


def resumir(datos, distrito, periodo):
    inicio, fin = periodo
    if not 1 <= inicio <= fin <= 12:
        raise ValueError('El periodo debe estar entre enero y diciembre.')
    seleccion = datos[datos['fecha'].dt.month.between(inicio, fin)]
    zona = 'distrito' if distrito == TODOS else 'barrio'
    if distrito != TODOS:
        seleccion = seleccion[seleccion['distrito'].eq(distrito)]

    mensual = (seleccion.groupby(seleccion['fecha'].dt.month)['expedientes'].sum()
               .reindex(range(inicio, fin + 1), fill_value=0))
    zonas = seleccion.groupby(zona)['expedientes'].sum().sort_values()
    dia_semana = seleccion['fecha'].dt.dayofweek.map(dict(enumerate(DIAS)))
    calor = (seleccion.groupby([dia_semana, 'hora'])['expedientes'].sum().unstack(fill_value=0)
             .reindex(index=DIAS, columns=range(24), fill_value=0))
    total = int(seleccion['expedientes'].sum())
    assert total == mensual.sum() == zonas.sum() == calor.to_numpy().sum()
    return total, mensual, zonas, calor, zona


def figura_panel(datos, distrito=TODOS, periodo=(1, 12)):
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    total, mensual, zonas, calor, zona = resumir(datos, distrito, periodo)
    fig = make_subplots(
        rows=3, cols=2,
        specs=[[{'type': 'indicator', 'colspan': 2}, None],
               [{}, {}],
               [{'colspan': 2}, None]],
        row_heights=[0.16, 0.38, 0.46],
        vertical_spacing=0.10,
        subplot_titles=('', 'Evolución mensual', f'Recuento por {zona}', 'Día y hora'),
    )
    fig.add_trace(go.Indicator(mode='number', value=total, title={'text': 'Expedientes registrados'}), row=1, col=1)
    fig.add_trace(go.Scatter(x=[MESES[m - 1][:3] for m in mensual.index], y=mensual.values,
                             mode='lines+markers', line={'color': '#067276'}), row=2, col=1)
    fig.add_trace(go.Bar(x=zonas.values, y=zonas.index, orientation='h',
                         marker_color='#613A89'), row=2, col=2)
    fig.add_trace(go.Heatmap(x=list(calor.columns), y=list(calor.index), z=calor.to_numpy(),
                             colorscale='Blues', zmin=0, colorbar={'title': 'Expedientes', 'len': 0.4, 'y': 0.20}), row=3, col=1)
    fig.update_xaxes(title_text='Mes', row=2, col=1)
    fig.update_yaxes(title_text='Expedientes', rangemode='tozero', row=2, col=1)
    fig.update_xaxes(title_text='Expedientes', row=2, col=2)
    fig.update_xaxes(title_text='Hora del día', dtick=1, row=3, col=1)
    fig.update_yaxes(autorange='reversed', row=3, col=1)
    inicio, fin = periodo
    alcance = MESES[inicio - 1] if inicio == fin else f'{MESES[inicio - 1]} a {MESES[fin - 1]}'
    fig.update_layout(title=f'{distrito} · {alcance} de 2023', showlegend=False,
                      height=780, template='plotly_white', margin={'l': 110, 'r': 95, 't': 75, 'b': 55})
    return fig
