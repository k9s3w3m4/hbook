import requests
from bs4 import BeautifulSoup
import re
from requests.exceptions import RequestException

baseurl = 'http://www.xxshubao.com/'
subbookurl = 'book/52894.html'
def get_charpter_url(bookurl):
  try:
    responde = requests.get(bookurl)
    if responde.status_code == 200:
        # print(responde.text)
        return responde.text
    return None
  except RequestException:
      print('error')
      return None

def parse_charpter_url(html):
    soup = BeautifulSoup(html,'lxml')
    # print(soup)
    for content in soup.select('#m > div.infoleft > div.mulu > ul > li > a'):
        href = content.attrs['href']
        title = content.attrs['title']
        yield href,title


def get_page_content(pageurl):
    try:
        responde = requests.get(pageurl)
        if responde.status_code == 200:
            # print(responde.text)
            responde.encoding = 'gbk'
            return responde.text
        return None
    except RequestException:
        print('error')
        return None
def get_good_content(content2):
    content = re.sub('Kou','口',content2)
    content = re.sub('Xing', '性', content)
    content = re.sub('Jian', '奸', content)
    content = re.sub('Bao', '暴', content)
    content = re.sub('Yin', '淫', content)
    content = re.sub('Jing', '精', content)
    content = re.sub('Cao', '操', content)
    content = re.sub('Qi', '妻', content)
    content = re.sub('Di', '蒂', content)
    content = re.sub('Gui', '龟', content)
    content = re.sub('Ru', '乳', content)
    content = re.sub('��', '你', content)
    content = re.sub('Rou', '肉', content)
    content = re.sub('Zuo', '做', content)
    content = re.sub('Cha', '插', content)
    content = re.sub('Chu', '处', content)
    content = re.sub('She', '射', content)
    goodcontent = content
    return goodcontent





def parse_page_content(pagehtml):
    parsetext = re.compile('"mc">.*?<h1>(.*?)</h1>.*?"mcc">(.*?)<a',re.S) #.*?<h1>(.*?)</h1>.*?"mcc">(.*?).*?<a
    result = re.findall(parsetext,pagehtml)
    for i in  result:
        title,content = i
        content = re.sub('<br />','',content)
        content2 = re.sub('<script|type="text/javascript">|read_text_c|</script>|\(|\)|\;|\||丨','',content)
        good_content = get_good_content(content2)
        print(title+'\n'+good_content)
        yield title,good_content

def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(content)
        f.close()

def main():
    bookurl = baseurl+subbookurl
    html = get_charpter_url(bookurl)
    for href,title in parse_charpter_url(html):
        pageurl = baseurl+href
        pagehtml = get_page_content(pageurl)
        for title2,content in parse_page_content(pagehtml):
            content = title2+'\n'+content
            write_to_file(content)
            print(title2+'写入成功')




if __name__ == '__main__':
    main()

