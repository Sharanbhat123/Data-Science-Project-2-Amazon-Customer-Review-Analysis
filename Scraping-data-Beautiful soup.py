import pandas as pd
import requests
from bs4 import BeautifulSoup

reviews_ratings = []
for j in range(1, 201):
    link = 'https://www.amazon.in/Canon-1500D-Digital-Camera-S18-55/product-reviews/B07BS4TJ43/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber='
    page = requests.get(link + str(j))
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('div', class_='a-section review aok-relative')

    for i in lists:
        review = i.find('span', class_='a-size-base review-text review-text-content').text.replace('\n','')
        rating = i.find('span', class_='a-icon-alt').text.replace('\n','')
        info = {'ratings': rating, 'reviews': review}
        reviews_ratings.append(info)

df_info=pd.DataFrame(reviews_ratings)
to_csv=df_info.to_csv('D:/Data Science/Data science project - 2/amazon_reviews.csv')