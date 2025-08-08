from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

app = Dash()
df = pd.read_csv('./valuable-data.csv')

fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales Over Time", labels={"date": "Date", "sales": "Sales in USD ($)"})
app.layout = html.Div(
    [html.H1('Pink Morsel Sales Visualizer'),

    html.P(
        ['A dashboard to visualize the trend in sales of Pink Morsel over time. ',
        'Use this chart to assess whether sales were higher before or after the price change.']
           ),
    dcc.Graph(
        id='sales-graph',
        figure=fig
    )]

)
if __name__ == '__main__':
    app.run(debug=True)