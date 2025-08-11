from dash import Dash, dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px

def create_app(df):
    app = Dash()

    app.layout = html.Div(
        [html.H1('Pink Morsel Sales Visualizer', style={
            'textAlign': 'center',
            'color': '#2E86C1',
            'font-family': 'Arial'
        }),

        html.P(
            ['A dashboard to visualize the trend in sales of Pink Morsel over time. ',
            'Use this chart to assess whether sales were higher before or after the price change.']
            , style={
                'textAlign': 'center',
                'fontSize': '18px',
                'marginBottom': '20px'
            }),
        dcc.Graph(
            id='sales-graph',
            style={
                'border': '2px solid #ccc',
                'padding': '10px',
                'backgroundColor': '#f9f9f9'
            }
        ),
        dcc.RadioItems(
            id='regions',
            options=[
                'north', 'east', 'south', 'west', 'all'
            ],
            value='all',
            inline=True,
            style={
                'display': 'flex',
                'justifyContent': 'center',
                'gap': '15px',
                'marginBottom': '30px'
            }
        )],
    style={'maxWidth': '800px', 'margin': '0 auto'}
    )

    @callback(
        Output('sales-graph', 'figure'),
        Input('regions', 'value')
    )
    def update_graph(regions):
        updated_df = df[df['region'] == regions]
        if regions != 'all':
            fig = px.line(updated_df, x="date", y="sales", title="Pink Morsel Sales Over Time", labels={"date": "Date", "sales": "Sales in USD ($)"})
        else:
            fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales Over Time", labels={"date": "Date", "sales": "Sales in USD ($)"})
        return fig
    return app

if __name__ == '__main__':
    df = pd.read_csv('./valuable-data.csv')
    create_app(df).run(debug=True)