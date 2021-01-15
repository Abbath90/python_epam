import pytest
from pathlib import Path
from homework10.task1.sp500 import *

from bs4 import BeautifulSoup
import pandas as pd

def test_get_dollar_rate():
    with open(Path('./test_stuff/dollar.xml')) as file:
        assert get_dollar_rate(file.read()) == 73.5264