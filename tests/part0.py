import requests


send_nbr = ''

test_url = 'https://dqd30.jxdxxt.com/chnl-web/chnl/jx/mkt/workSheetExec/nbrValidata'
headers = {
    'Cookie': 'CHNL_SESSION=MzUxZjRlYTUtZTE3My00YjMwLTkwOWYtMDA4MTgzZDg1YjE1',
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

result = response.json()
error_nums = result['svcCont']['data']['errorList']
print(error_nums)
for error_num in error_nums:
    if error_num == send_nbr:
        print(False)
    else:
        print(True)
