from app import create_app
import pandas as pd

df = pd.DataFrame({
        'date': ['2018-02-08', '2018-02-10'],
        'sales': [120, 350],
        'region': ['all', 'north']
    })
app = create_app(df)

def test_header_shows(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1")

def test_graph_shows(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#regions")

def test_radio_works(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-graph")