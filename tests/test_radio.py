# tests/test_radio.py
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pandas as pd
from app import create_app
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def _first_trace_len(dash_duo):
    return dash_duo.driver.execute_script("""
        const el = document.querySelector('#sales-graph .js-plotly-plot');
        if (!el || !el.data || !el.data.length) return -1;
        const t = el.data[0];
        return (t.x && t.x.length !== undefined) ? t.x.length : -1;
    """)

def _wait_until(dash_duo, predicate, timeout=10):
    WebDriverWait(dash_duo.driver, timeout).until(lambda d: predicate())

def test_radio(dash_duo):
    df = pd.DataFrame({
        'date':   ['2018-02-08', '2018-02-10'],
        'sales':  [120, 350],
        'region': ['all', 'north'],
    })
    app = create_app(df)
    dash_duo.start_server(app)

    # Wait for both the graph and the radios to be present
    dash_duo.wait_for_element('#sales-graph .js-plotly-plot')
    dash_duo.wait_for_element('#regions')

    # default 'all' -> both points
    _wait_until(dash_duo, lambda: _first_trace_len(dash_duo) == 2, timeout=10)

    # Click the "north" option by its label text (more robust than input[value=...])
    label_north = WebDriverWait(dash_duo.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="regions"]//label[normalize-space()="north"]'))
    )
    dash_duo.driver.execute_script("arguments[0].scrollIntoView(true);", label_north)
    label_north.click()

    # Now only 1 point should remain
    _wait_until(dash_duo, lambda: _first_trace_len(dash_duo) == 1, timeout=10)
