import requests

data=requests.get(url='https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean')
data=data.json()['results']
question_data = data


