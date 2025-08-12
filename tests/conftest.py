# tests/conftest.py
import pytest
from dash.testing.composite import DashComposite
from dash.testing.application_runners import ThreadedRunner
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def dash_duo(tmp_path):
    server = ThreadedRunner()
    options = Options()
    options.add_argument("--headless=new")

    dc = DashComposite(
        server=server,
        browser="chrome",                 # let Selenium Manager resolve driver
        headless=True,
        options=options,
        download_path=str(tmp_path / "download"),
    )
    with dc:
        yield dc
