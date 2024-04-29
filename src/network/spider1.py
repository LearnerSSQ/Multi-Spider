import sys
import time

import requests
from rich.console import Console
from rich.progress import Progress
from rich.traceback import install

# from tqdm import tqdm

install()
console = Console()


class Spider1:
    session = requests.Session()

    @staticmethod
    def send_request(url: str, data: dict, headers: dict) -> requests.Response:
        max_attempts = 5
        for attempt in range(max_attempts):
            try:
                response = Spider1.session.post(url=url, json=data, headers=headers, timeout=5)
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
    def crawler(data_send_nbr: list, data_sum_content: list, request_main_url: str, request_deputy_url: str,
                request_main_data: dict, request_deputy_data: dict, request_headers: dict) -> list:
        values = []
        empty_value = ['']
        number_error = ['错误号码']
        connect_error = ['响应无效']

        with Progress(console=console, refresh_per_second=1) as progress:
            task = progress.add_task("[bold cyan]Crawling datas...", total=len(data_send_nbr))

            for idx, (send_nbr, sum_content) in enumerate(zip(data_send_nbr, data_sum_content), start=2):
                progress.update(task, advance=1)
                request_main_data.update({'send_nbr': str(send_nbr)})
                main_response = Spider1.send_request(request_main_url, request_main_data, request_headers)

                if main_response.status_code == 200:
                    console.print(f"\n[bold red]错误:[/bold red] 号码无效于 {request_main_url}"
                                  f"\n行数: {idx} 号码: {send_nbr}")
                    values.append(number_error)
                    continue

                request_deputy_data.update({'send_nbr': send_nbr, 'sum_content': sum_content})
                deputy_response = Spider1.send_request(request_deputy_url, request_deputy_data, request_headers)

                if deputy_response.status_code == 200:
                    values.append(empty_value)

                else:
                    console.print(f"\n[bold red]错误:[/bold red] 响应无效于 {request_deputy_url}"
                                  f"\n行数: {idx} 号码: {send_nbr}")
                    values.append(connect_error)
                    continue

        return values
