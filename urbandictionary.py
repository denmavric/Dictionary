import requests

# authorization headers, this is needed.
headers = {"x-rapidapi-key": "{you need to get this from rapidapi which is free}", "x-rapidapi-host": "mashape-community-urban-dictionary.p.rapidapi.com"}

word = input("Word: ") # taking input

# we're getting the information, we can use data=payload but since this doesn't really need that we're just using params.
# payload = {"term", word}

term = requests.get("https://mashape-community-urban-dictionary.p.rapidapi.com/define", headers=headers, params={"term": word})
print(term.text) # this gives the response from the rapidapi/api
