import requests
from bs4 import BeautifulSoup
import re

def get_news():
    url = "https://www.usatoday.com"
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    lists = bs.select("div.gnt_m_th > a")
    for li in lists:
        href = url + li["href"]
        print(href)

        r = requests.get(href)
        bs = BeautifulSoup(r.text, "lxml")
        texts = bs.select("div.gnt_ar_b > p.gnt_ar_b_p")
        contents = [p.text for p in texts]
        # 리스트 컴프리헨션
        # contents = []
        # for p in texts:
        #     contents.append(p.text)
        contents = " ".join(contents)
        # 이렇게 하면 for문을 안 돈다는 데 이거 이해 안가네
        return contents.lower()
    return None

def make_quiz(news):
    # 정규식 이용하기
    match_pattern = re.findall(r'\b[a-z]{4,15}\b', news)
    # print(match_pattern)

    frequency = {}
    quiz_list = []

    for word in match_pattern:
        count = frequency.get(word, 0)
        # 이 부분 쫌 어렵네 일단 pass
        frequency[word] = count + 1

    for word, count in frequency.items():
        print(word, count)
        if count > 1:
            kor = ""
            quiz_list.append({kor: word})

    return quiz

news = get_news()
quiz = make_quiz(news)