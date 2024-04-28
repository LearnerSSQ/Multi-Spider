import requests


send_nbr = '15387744202'

test_url = 'https://dqd30.jxdxxt.com/chnl-web/chnl/jx/mkt/workSheetExec/nbrValidata'
headers = {
    'Cookie': 'CHNL_SESSION=MmM4MDQzYmMtOTlhNi00M2U2LTk0ZWItM2JjNjYxYjQ3YmRh',
    'Referer': 'https://dqd30.jxdxxt.com/chnl-web/frame?p=chnl/modules/jx/mkt/views/TaskMapView&staffCode=jhy578146'
               '&staffPosId=502163014&menuId=1122',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 '
                  'Safari/537.36 Edg/123.0.0.0'
}
data = {
    'send_nbr': send_nbr
}
response = requests.post(url=test_url, headers=headers, json=data)

print(response)
print(response.json())

if response.status_code == 500:
    print('zero')
