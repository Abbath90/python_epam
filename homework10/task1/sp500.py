import asyncio
import re
import time
from typing import Any, List

import aiohttp
import pandas as pd
import requests
from bs4 import BeautifulSoup


def timeit(func):
    """
    Decorator for measuring function's running time.
    """

    def measure_time(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print(
            "Processing time of %s(): %.2f seconds."
            % (func.__qualname__, time.time() - start_time)
        )
        return result

    return measure_time


def get_dollar_rate(link: str) -> float:
    response = requests.get(link)
    soup = (
        BeautifulSoup(response.content, "lxml").find("valute", id="R01235").value.string
    )
    dollar_rate = float(soup.replace(",", "."))
    return dollar_rate


def create_page_list(urlbase: str) -> List[str]:
    return [urlbase + "/index/components/s&p_500?p=" + str(i) for i in range(1, 3)]


def get_p_e(soup: BeautifulSoup) -> float:
    try:
        numbs = soup.findAll("div", attrs={"class": "snapshot__data-item"})
        p_e = re.findall("\d+\.\d+", str(numbs))[4]
        return float(p_e.replace(",", ""))
    except AttributeError:
        return 0


def get_potential_profit(soup: BeautifulSoup) -> float:
    js_text = soup.find("div", id="snapshot").find("script")
    js_text_numbs = re.findall("\d+\.\d+", str(js_text.get_text))
    high52 = float(js_text_numbs[0].replace(",", ""))
    low52 = float(js_text_numbs[1].replace(",", ""))
    profit = round((1 - (low52 / high52)) * 100, 2)
    return profit


async def get_info_from_company_page(
    client: aiohttp.ClientSession, link: str, company: dict, dollar_rate: float
) -> None:
    async with client.get(link) as response:
        soup = BeautifulSoup(await response.text(), "lxml")
        company["code"] = soup.find(
            "span", class_="price-section__category"
        ).text.split()[-1]
        price = float(
            soup.find_all("span", class_="price-section__current-value")[
                -1
            ].text.replace(",", "")
        )
        company["price"] = round(price * dollar_rate, 2)
        company["p_e"] = get_p_e(soup)
        company["profit %"] = get_potential_profit(soup)


async def get_table(
    client: aiohttp.ClientSession, url: str, dollar_rate: float, urlbase: str
) -> pd.DataFrame:
    async with client.get(url) as response:
        tasks = []
        company_list = []
        soup = BeautifulSoup(await response.text(), "lxml")
        table = soup.find_all("table")
        stock_links = [line.get("href") for line in table[1].find_all("a")]
        for link in stock_links:
            company = dict()
            company_list.append(company)
            stock_url = urlbase + link
            tasks.append(
                asyncio.create_task(
                    get_info_from_company_page(client, stock_url, company, dollar_rate)
                )
            )
        await asyncio.gather(*tasks)
        df = pd.read_html(str(table))[1]
        df["Link"] = stock_links
        df2 = pd.DataFrame(company_list)
        df = pd.concat([df, df2], axis=1)
        return df


async def get_all_tables(urls: List[str], dollar_rate: float, urlbase: str) -> Any:
    async with aiohttp.ClientSession() as client:
        futures = [get_table(client, url, dollar_rate, urlbase) for url in urls]
        return await asyncio.gather(*futures)


def create_jsons(sp500_df: pd.DataFrame) -> None:
    sp500_df.set_index("code").sort_values(["price"], ascending=False).head(10).to_json(
        "top10_price", orient="index"
    )
    sp500_df.set_index("code").sort_values(["p_e"], ascending=True).head(10).to_json(
        "top10_pe", orient="index"
    )
    sp500_df.set_index("code").sort_values(["growth"], ascending=False).head(
        10
    ).to_json("top10_growth", orient="index")
    sp500_df.set_index("code").sort_values(["profit %"], ascending=False).head(
        10
    ).to_json("top10_profit", orient="index")


@timeit
def sp500_main() -> None:
    urlbase = "https://markets.businessinsider.com"
    urls = create_page_list(urlbase)
    dollar_rate = get_dollar_rate("http://www.cbr.ru/scripts/XML_daily.asp")
    tables = asyncio.get_event_loop().run_until_complete(
        get_all_tables(urls, dollar_rate, urlbase)
    )
    # tables = asyncio.run(get_all_tables(urls, dollar_rate, urlbase))
    sp500_df = pd.concat(tables, ignore_index=True)
    sp500_df["growth"] = sp500_df["1 Year +/- %"].str.split(" ", 1, expand=True)[0]
    sp500_df = sp500_df[["code", "Name", "price", "p_e", "growth", "profit %"]]
    create_jsons(sp500_df)


sp500_main()
