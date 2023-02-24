import random
import string

from locust import HttpUser, between, task

popular_keywords_input = open("data/popular_keywords","r")
popular_keywords = popular_keywords_input.read().splitlines()

spesific_keywords_input = open("data/spesific_keywords","r")
spesific_keywords = spesific_keywords_input.read().splitlines()

general_keywords_input = open("data/general_keywords","r")
general_keywords = general_keywords_input.read().splitlines()

def get_header():
    header = {
        'User-Agent' : 'temp'
    }
    return header

class CustomerUser(HttpUser):

    @task(25)
    def get_products_with_popular(self):
        keyword = random.choice(popular_keywords)
        print(self.host + "arama?q="+keyword)
        with self.client.get(
                'arama?q='+keyword,headers=get_header(), name='get_products_with_popular', catch_response=True) as get_products_with_popular_response:
            get_products_with_popular_response = get_products_with_popular_response

    @task(15)
    def get_products_with_spesific(self):
        keyword = random.choice(spesific_keywords)
        print(self.host + "arama?q=" + keyword)
        with self.client.get(
                'arama?q=' + keyword,headers=get_header(), name='get_products_with_spesific',
                catch_response=True) as get_products_with_spesific_response:
            get_products_with_spesific_response = get_products_with_spesific_response

    @task(60)
    def get_products_with_general(self):
        keyword = random.choice(general_keywords)
        print(self.host + "arama?q=" + keyword)
        with self.client.get(
                'arama?q=' + keyword,headers=get_header(), name='get_products_with_general',
                catch_response=True) as get_products_with_general_response:
            get_products_with_general_response = get_products_with_general_response

    host = "https://www.n11.com/"
    wait_time = between(0.1, 0.2)