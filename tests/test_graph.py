import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pandas as pd
from app import create_app
import plotly.express as px

def test_graph(dash_duo):
    df = pd.DataFrame({
        'date': ['2018-02-08', '2018-02-10'],
        'sales': [120, 350],
        'region': ['all', 'north']
    })
    def update_graph(regions):
        updated_df = df[df['region'] == regions]
        if regions != 'all':
            fig = px.line(updated_df, x="date", y="sales", title="Pink Morsel Sales Over Time", labels={"date": "Date", "sales": "Sales in USD ($)"})
        else:
            fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales Over Time", labels={"date": "Date", "sales": "Sales in USD ($)"})
        return fig
    fig = update_graph('north')
    app = create_app(df)
    dash_duo.start_server(app)

    assert fig is not None
    assert len(fig.data) > 0
