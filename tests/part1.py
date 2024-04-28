import requests

send_nbr = '15387726042'
sms_content = '短信测试'

part_url = 'https://dqd30.jxdxxt.com/chnl-web/chnl/jx/mkt/workSheetExec/batchSendSms'
headers = {
    'Cookie': 'CHNL_SESSION=ZTZhYmU1YjUtMDdiZS00ZTk5LWEyOWItMzA0YWE4ODVmY2E4',
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
