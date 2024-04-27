import requests

send_nbr = '13387927637'
sms_content = ('尊敬周先生/女士您好！使用的电信产品2671091付款账号6720041706已欠费，请您在三天内九江电信各大营业厅凭付费编码缴清欠费，以免欠费给你生活带来不必要的麻烦！谢谢您的合作('
               '如已交清欠费请忽略）有疑问可致电咨询电话07928199373')

part_url = 'https://dqd30.jxdxxt.com/chnl-web/chnl/jx/mkt/workSheetExec/batchSendSms'
headers = {
    'Cookie': 'CHNL_SESSION=MzUxZjRlYTUtZTE3My00YjMwLTkwOWYtMDA4MTgzZDg1YjE1',
    'Referer': 'https://dqd30.jxdxxt.com/chnl-web/frame?p=chnl/modules/jx/mkt/views/TaskMapView&staffCode=jhy578146'
               '&staffPosId=502163014&menuId=1122',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 '
                  'Safari/537.36 Edg/123.0.0.0'
}
data = {
    'if_record_sheet': 1,
    'if_sign': 0,
    'is_sec': 'false',
    'mkt_exec_id': 640580294,
    'send_nbr': send_nbr,
    'sms_args': '',
    'sms_content': sms_content
}
response = requests.post(url=part_url, headers=headers, json=data)
print(response)
print(response.json())

result = response.json()
remark = result['topCont']['remark']
print(remark)
