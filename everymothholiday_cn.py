#!/usr/bin/env python3
"""Fetch holidays from gov.cn  """
import log

import argparse
import json
import re
from datetime import date, timedelta
from itertools import chain
from typing import Iterator, List, Optional, Tuple
import datetime
import bs4
import requests

SEARCH_URL = 'http://sousuo.gov.cn/s.htm'
PAPER_EXCLUDE = [
    'http://www.gov.cn/zhengce/content/2014-09/29/content_9102.htm',
    'http://www.gov.cn/zhengce/content/2015-02/09/content_9466.htm',
]


def get_paper_urls(year: int) -> List[str]:
    """Find year related paper urls.

    Args:
        year (int): eg. 2018

    Returns:
        List[str]: Urls， newlest first.
    """

    body = requests.get(SEARCH_URL, params={
        't': 'paper',
        'advance': 'true',
        'title': year,
        'q': '假期',
        'pcodeJiguan': '国办发明电',
        'puborg': '国务院办公厅'
    }).text
    ret = re.findall(
        r'<li class="res-list".*?<a href="(.+?)".*?</li>', body, flags=re.S)
    ret = [i for i in ret if i not in PAPER_EXCLUDE]
    ret.sort()
    # print(ret)
    return ret






def get_paper(url: str) -> str:
    """Extract paper text from url.

    Args:
        url (str): Paper url.

    Returns:
        str: Extracted paper text.
    """

    assert re.match(r'http://www.gov.cn/zhengce/content/\d{4}-\d{2}/\d{2}/content_\d+.htm',
                    url), 'Site changed, need human verify'

    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(response.text, features='html.parser')
    container = soup.find('td', class_='b12c')
    assert container, f'Can not get paper container from url: {url}'
    ret = container.get_text().replace('\u3000\u3000', '\n')
    assert ret, f'Can not get paper context from url: {url}'
    # print(ret)
    return ret


if __name__ == '__main__':
    # get_paper('http://www.gov.cn/zhengce/content/2020-11/25/content_5564127.htm')


    year = datetime.datetime.today().year
    # print(year)
    # url=get_paper_urls(year)
    for i in get_paper_urls(year):
        s=i
        txt = get_paper(s)
        print(txt)

        url = 'http://wxpusher.zjiecode.com/api/send/message'
        HEADERS = {'Content-Type': 'application/json'}
        # dt = datetime.now()
        # time = dt.strftime('%Y-%m-%d')
        # 'application/x-www-form-urlencoded'
        # 'application/json;charset=utf-8'
        FormData = {
                    "appToken": "AT_iaPxpUE0FLNUECu1zFnKhFR7R9NU5K8e",
                    "content": txt,
                    "summary": f"国务院办公厅关于{year}年部分节假日安排的通知",
                    "contentType": 1,

        "topicIds": [

        ],
        "uids": [
        "UID_noWsar4x3r0zd4WqjCaoD5CIX9Xi"
        ],
        "url": ""
        }

        res = requests.post(url=url, json=FormData)
        # content = requests.post(url=url, data=FormData).text

        print(res.text)
        log.info(res.text)









#
# if __name__ == '__main__':
#     a=get_paper('http://www.gov.cn/zhengce/content/2020-11/25/content_5564127.htm')
#     get_rules(a)


