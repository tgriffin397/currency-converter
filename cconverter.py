import requests

currency_code_pre = input().lower()

usd_price = requests.get('http://www.floatrates.com/daily/' + 'usd' + '.json').json()
eur_price = requests.get('http://www.floatrates.com/daily/' + 'eur' + '.json').json()
cache = {'usd': usd_price, 'eur': eur_price}

while True:
    currency_code_post = input().lower()
    if currency_code_post == "":
        break
    currency_amount = float(input())


    def retrieval_print(num, text):
        print("You received " + str(round(num, 2)) + " " + text + ".")


    print("Checking the cache...")
    if currency_code_post in cache:
        print("Oh! It is in the cache!")
        retrieval_print(currency_amount * cache[currency_code_post][currency_code_pre]['inverseRate'], currency_code_post.upper())
    else:
        print("Sorry, but it is not in the cache!")
        url = requests.get('http://www.floatrates.com/daily/' + currency_code_post + '.json').json()
        cache.update({currency_code_post: url})
        retrieval_print(currency_amount * cache[currency_code_post][currency_code_pre]['inverseRate'], currency_code_post.upper())