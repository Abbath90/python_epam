from pathlib import Path

import pandas as pd
import pytest
import requests_mock
from aioresponses import aioresponses
from bs4 import BeautifulSoup

from homework10.task1.sp500 import *


def test_get_dollar_rate():
    with requests_mock.Mocker() as m:
        with open("homework10/tests/test_stuff/dollar.xml") as file:
            m.get("http://test.com", text=file.read())
            assert get_dollar_rate("http://test.com") == 73.5264


def test_create_page_list():
    pass


def test_get_p_e():
    with requests_mock.Mocker() as m:
        with open("homework10/tests/test_stuff/html2") as file:
            m.get("http://test.com", text=file.read())
            response = requests.get("http://test.com")
            soup = BeautifulSoup(response.content, "lxml")
            assert get_p_e(soup) == 21.43


def test_get_potential_profit():
    with requests_mock.Mocker() as m:
        with open("homework10/tests/test_stuff/html2") as file:
            m.get("http://test.com", text=file.read())
            response = requests.get("http://test.com")
            soup = BeautifulSoup(response.content, "lxml")
            assert get_potential_profit(soup) == 42.45


async def test_get_info_from_company_page():
    with aioresponses() as m:
        with open("homework10/tests/test_stuff/html2") as file:
            m.get("http://test.com", body=file.read())
            session = aiohttp.ClientSession()
            dollar_rate = 1
            link = "http://test.com"
            company = dict()
            await get_info_from_company_page(session, link, company, dollar_rate)
            assert company["p_e"] == 21.43


def test_create_jsons():
    dict_for_dataframe = {
        "MKC": {
            "Name": "McCormick &",
            "price": 6855.89,
            "p_e": 31.59,
            "growth": "9.80",
            "profit %": 2.49,
        },
        "RJF": {
            "Name": "Raymond James Financial",
            "price": 7581.78,
            "p_e": 11.8,
            "growth": "9.69",
            "profit %": 1.85,
        },
        "DLR": {
            "Name": "Digital Realty Trust",
            "price": 10014.66,
            "p_e": 50.76,
            "growth": "9.54",
            "profit %": 2.5,
        },
    }

    df = (
        pd.DataFrame(dict_for_dataframe)
        .transpose()
        .reset_index()
        .rename({"index": "code"}, axis=1)
    )
    create_jsons(df)
    assert len(sorted(Path(".").glob("*.json"))) == 4
