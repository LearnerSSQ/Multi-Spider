import sys
import time

import requests
from tqdm import tqdm

class Spider0:
    session = requests.Session()

    @staticmethod
    def send_request(url: str, data: dict, headers: dict) -> requests.Response:
        max_attempts = 5
        for attempt in range(max_attempts):
            try:
                response = Spider0.session.post(url, json=data, headers=headers, timeout=5)
                return response

            except requests.exceptions.RequestException as e:
                print(f"警告: 请求于 {url} 出现错误\n错误详情: {str(e)}")

                if attempt < max_attempts - 1:
                    print(f"等待5秒后重试...")
                    time.sleep(5)
                else:
                    print(f"错误: 请求失败超过 {max_attempts} 次")
                    input('按任意键退出...')
                    sys.exit(1)

    @staticmethod
    def crawler(data_acc_nbr: list, request_main_url: str, request_deputy_url: str,
                request_main_data: dict, request_deputy_data: dict, request_headers: dict) -> list:
        values = []
        empty_value = ['', '', '']

        for idx, acc_nbr in tqdm(enumerate(data_acc_nbr, start=2),
                                 total=len(data_acc_nbr), desc='Crawling headers', unit='headers'):
            request_main_data.update({'acc_nbr': str(acc_nbr)})
            main_response = Spider0.send_request(request_main_url, request_main_data, request_headers)

            if not main_response:
                print('\n错误: 没有响应于', request_main_url)
                values.append(empty_value)
                continue

            main_text = main_response.json()
            if ('svcCont' not in main_text or 'headers' not in main_text['svcCont']
                    or not main_text['svcCont']['headers']):
                print('\n错误: 响应无效于:', request_main_url, '行数:', idx, '号码:', acc_nbr)
                values.append(empty_value)
                continue

            mkt_exec_id = main_text['svcCont']['headers'][0]['mkt_exec_id']
            request_deputy_data.update({'mkt_exec_id': mkt_exec_id})

            deputy_response = Spider0.send_request(request_deputy_url, request_deputy_data, request_headers)
            if not deputy_response:
                print('\n错误: 没有响应于', request_deputy_url)
                values.append(empty_value)
                continue

            deputy_text = deputy_response.json()
            if ('svcCont' not in deputy_text or 'headers' not in deputy_text['svcCont']
                    or not deputy_text['svcCont']['headers']):
                print('\n错误: 响应无效于', request_deputy_url, '行数:', idx, '号码:', acc_nbr)
                values.append(empty_value)
                continue

            value = [item['value'] for item in deputy_text['svcCont']['headers']
                     if item['col_value'] in ['客户姓名', '联系电话', '本网联系人（发短信专用）']]

            values.append(value)

        return values
