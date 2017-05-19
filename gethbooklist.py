from getHbook import main as getbookcontent
import requests
import re
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from Config import *

def get_all_h_book(sublisturl):
    booklisturl = BASEURL+sublisturl
    try:
        responde = requests.get(booklisturl)
        if responde.status_code == 200 :
            return responde.text
        print("状态异常")
        return None
    except RequestException:
        print('Error')
def parse_all_h_book_list():
    soup = BeautifulSoup




def main():
    recommend = [0,1,2,3,4,5,6,7,8,9,10,11,12,13] #0-3 日周月总排行榜 4-7推荐榜 8-11收藏榜 12－13字数和更新榜
    sort = [0,1,2,3,4,5,6,7,8,9,10,11,12] #12为h小说
    page = 20   #页数
    listnubmer = '{0}_{1}_{2}'.format(recommend[11],sort[12],page)
    sublisturl =  '/top/'+listnubmer+'.html' #'/top/11_12_2.html'
    get_all_h_book(sublisturl)

    # subbookurl = 'book/52894.html'
    # getbookcontent(subbookurl)
if __name__ == '__main__':
    main()
