import json

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

from clsReview import Review

lstReviews = []


def get_reviews(page_url):
    page_number = '1'
    if str(page_url).__contains__("&page="):
        page_number = page_url.split("&page=")[1]

    print('Page ' + str(page_number) + ': ' + page_url)
    req_data = requests.get(page_url)
    review_soup = BeautifulSoup(req_data.content, 'html.parser')
    all_reviews = review_soup.find_all('div', {'class': 'col _390CkK _1gY8H-'})
    for review in all_reviews:
        likes = ''
        dislikes = ''

        try:
            rating = review.find('div', {'class': 'hGSR34 E_uFuv'}).text
            review_header = review.find('p', {'class': '_2xg6Ul'}).text
            detailed_review = review.find('div', {'class': 'qwjRop'}).div.div.text
            user = review.find('p', {'class': '_3LYOAd _3sxSiS'}).text
            likes_dislikes = review.find_all('span', {'class': '_1_BQL8'})

            print(rating, review_header, detailed_review, user, likes_dislikes)
            if len(likes_dislikes) > 0:
                likes = likes_dislikes[0].text
                dislikes = likes_dislikes[1].text

            # Create an object of type Review
            rev = Review(review_header, detailed_review, rating, likes, dislikes, user)
            lstReviews.append(rev)

        #       print('Rating :' + str(rev.rating))
        #       print('Header : ' + rev.reviewHeader)
        #       print("Review : " + rev.detailedReview)
        #       print('User :' + rev.user)
        #       print('Likes : ' + str(rev.likes))
        #       print('Dislikes : ' + str(rev.dislikes))
        #       print('--------------------------------------------------------------------------------------------------')

        except:
            print('Error on ' + str(page_number) + ': ' + page_url)


def insertDataInDB(data, dbName, collectionName):
    client = MongoClient()
    db = client[dbName]
    collections = db.collectionName
    result = collections.insert_one(data)
    return result


def getDataByuserId(dbName, collectionName):
    client = MongoClient()
    db = client[dbName]
    result = db[collectionName].find_one({'user': 'Moumita Dey'})
    return result


# Create an object into JSON
def json_default_format(reviewObj):
    if isinstance(reviewObj, Review):
        return {
            'rating': reviewObj.rating,
            'reviewHeader': reviewObj.reviewHeader,
            'detailedReview': reviewObj.detailedReview,
            'user': reviewObj.user,
            'likes': reviewObj.likes,
            'dislikes': reviewObj.dislikes
        }


# websiteUrl = "https://www.flipkart.com"
# URL = "https://www.flipkart.com/realme-xt-pearl-blue-64-gb/p/itm731360fdbd273?pid=MOBFJYBE9FHXFEFJ&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_0_4_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_0_4_na_na_pr&lid=LSTMOBFJYBE9FHXFEFJVA0XQF&fm=SEARCH&iid=a611c9af-350b-423d-87d8-df9bcc1987c7.MOBFJYBE9FHXFEFJ.SEARCH&ppt=sp&ppn=sp&ssid=n57aimhb7k0000001573581114720&qH=23f6a0071022557e"
# URL = "https://www.flipkart.com/realme-xt-pearl-blue-64-gb/p/itm731360fdbd273?pid=MOBFJYBE9FHXFEFJ&srno=s_1_1" \
#       "&otracker=AS_QueryStore_OrganicAutoSuggest_0_4_na_na_pr&otracker1" \
#       "=AS_QueryStore_OrganicAutoSuggest_0_4_na_na_pr&lid=LSTMOBFJYBE9FHXFEFJVA0XQF&fm=SEARCH&iid=a611c9af-350b-423d" \
#       "-87d8-df9bcc1987c7.MOBFJYBE9FHXFEFJ.SEARCH&ppt=sp&ppn=sp&ssid=n57aimhb7k0000001573581114720&qH=23f6a0071022557e "

def getReviewsFromURL(websiteUrl, url):
    r = requests.get(url)
    global lstReviews
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())

    # all_Reviews = soup.find_all('div', {'class': 'col _390CkK'})

    productPage_soup = soup.find('div', {'class': 'swINJg _3nrCtb'})
    # productPage_soup = soup.find_all('a')
    nextpageUrl = websiteUrl + productPage_soup.find_parent('a', {'href': True})['href']

    # databaseObj = DataAcccess('ReviewDB', 'ScrapperCollection')

    # try:
    #     while nextpageUrl != '':
    try:
        print('Current page  : ' + nextpageUrl)
        get_reviews(nextpageUrl)
        # req = requests.get(nextpageUrl)
        # nxt_soup = BeautifulSoup(req.content, 'html.parser')
        #
        # u = nxt_soup.find_all('a', {'class': '_3fVaIS'})
        # if len(u) == 1:
        #     if str.lower(u[0].text) == 'next':
        #         nextpageUrl = websiteUrl + u[0]['href']
        #     else:
        #         nextpageUrl = ''
        # else:
        #     nextpageUrl = websiteUrl + u[1]['href']
        #
        # print('Next Page : ' + nextpageUrl)
        # # print( u)
    except:
        print('Error Occured or last page ')
        # break
    # except:
    #     print('Error Occurred')

    dict_list = []

    for r in lstReviews:
        # insertDataInDB(json_default_format(r), 'ReviewScraperDB', 'scraperCollection')
        dict_list.append(json_default_format(r))

    # print('*' * 100)
    # print('Get Review by is')

    jsonObj = json.dumps(dict_list)
    return jsonObj
    # print(jsonObj)