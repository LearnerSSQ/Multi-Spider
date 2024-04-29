import sys
import time

import requests
from rich.console import Console
from rich.progress import Progress
from rich.traceback import install

# from tqdm import tqdm

console = Console()
install(show_locals=True)


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
                console.print(f"警告: 请求于 [red]{url}[/red] 出现错误\n错误详情: {str(e)}", style="bold red")

                if attempt < max_attempts - 1:
                    console.print(f"等待5秒后重试...", style="bold yellow")
                    time.sleep(5)
                else:
                    console.print(f"错误: 请求失败超过 {max_attempts} 次", style="bold red")
                    input('按任意键退出...')
                    sys.exit(1)

    @staticmethod
    def crawler(data_acc_nbr: list, request_main_url: str, request_deputy_url: str,
                request_main_data: dict, request_deputy_data: dict, request_headers: dict) -> list:
        values = []
        empty_value = ['', '', '']

        with Progress(console=console, refresh_per_second=1) as progress:
            task = progress.add_task("[bold cyan]Crawling datas...", total=len(data_acc_nbr))

            for idx, acc_nbr in enumerate(data_acc_nbr, start=2):
                progress.update(task, advance=1)
                request_main_data.update({'acc_nbr': str(acc_nbr)})
                main_response = Spider0.send_request(request_main_url, request_main_data, request_headers)

                if main_response.status_code != 200:
                    console.print(f"\n[bold red]错误:[/bold red] 没有响应于 {request_main_url}")
                    values.append(empty_value)
                    continue

                main_json = main_response.json()
                if ('svcCont' not in main_json or 'data' not in main_json['svcCont']
                        or not main_json['svcCont']['data']):
                    console.print(f"\n[bold red]错误:[/bold red] 响应无效于: {request_main_url}"
                                  f"\n行数: {idx} 号码: {acc_nbr}")
                    values.append(empty_value)
                    continue

                mkt_exec_id = main_json['svcCont']['data'][0]['mkt_exec_id']
                request_deputy_data.update({'mkt_exec_id': mkt_exec_id})
                deputy_response = Spider0.send_request(request_deputy_url, request_deputy_data, request_headers)

                if not deputy_response:
                    console.print(f"\n[bold red]错误:[/bold red] 没有响应于 {request_deputy_url}")
                    values.append(empty_value)
                    continue

                deputy_json = deputy_response.json()
                if ('svcCont' not in deputy_json or 'data' not in deputy_json['svcCont']
                        or not deputy_json['svcCont']['data']):
                    console.print(f"\n[bold red]错误:[/bold red] 响应无效于 {request_deputy_url}"
                                  f"\n行数: {idx} 号码: {acc_nbr}")
                    values.append(empty_value)
                    continue

                value = [item['value'] for item in deputy_json['svcCont']['data']
                         if item['col_value'] in ['客户姓名', '联系电话', '本网联系人（发短信专用）']]

                values.append(value)

        return values
