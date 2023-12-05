import requests

USERNAME='grandma'
TOKEN='gjgjjjjjj'
GRAPHID='azasdasd'


pixela_API='https://pixe.la/v1/users'

user_param= {
    'token':TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes',
}

#response=requests.post(pixela_API,json=user_param)
#print(response.text)


graph_param={
    'id':GRAPHID,
    'name':'running graph',
    'unit':'kilometer',
    'type':'float',
    'color':'sora',


}

graph_header={
'X-USER-TOKEN': TOKEN
}

graph_endpoint =f'{pixela_API}/{USERNAME}/graphs'

#response=requests.post(url=graph_endpoint,json=graph_param,headers=graph_header)
#print(response.text)

pixel_params={
    'date':'20231109',
    'quantity':'123.1',
}

pixel_endpoint=f'{graph_endpoint}/{GRAPHID}'

response=requests.post(url=pixel_endpoint,json=pixel_params,headers=graph_header)
print(response.text)





