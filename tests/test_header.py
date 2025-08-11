import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pandas as pd
from app import create_app

def test_header(dash_duo):
    df = pd.DataFrame({
        'date': ['2018-02-08', '2018-02-10'],
        'sales': [120, 350],
        'region': ['all', 'north']
    })

    app = create_app(df)
    dash_duo.start_server(app)

    
    h1 = dash_duo.find_element("h1")
    assert h1 is not None
    assert h1.text.strip() == 'Pink Morsel Sales Visualizer'