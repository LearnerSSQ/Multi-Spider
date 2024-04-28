import csv
import os
import sys

from rich.console import Console


class CSVReader:

    def __init__(self):
        self.console = Console()

    def read_csv(self, file_path: str) -> dict:
        try:
            with open(file_path, 'r', encoding='utf-8', newline='') as f:
                reader = csv.reader(f)
                next(reader)
                data = {row[0]: row[1] for row in reader}

        except FileNotFoundError:
            self.console.print(f'[bold red]错误: 文件 {file_path} 不存在[/bold red]')
            input('按任意键退出...')
            sys.exit(1)

        return data

    def read_file_data(self, file_name: str) -> dict:
        cwd = os.getcwd()
        file_path = os.path.join(cwd, 'data', f'{file_name}.csv')
        return self.read_csv(file_path)

    def read_headers(self) -> dict:
        return self.read_file_data('headers')

    def read_spider0_main_data(self) -> dict:
        return self.read_file_data('get_act_work_sheet_list_data')

    def read_spider0_deputy_data(self) -> dict:
        return self.read_file_data('qry_inf_down_data_basic_cpc_data')

    def read_spider1_main_data(self) -> dict:
        return self.read_file_data('nbr_validata_data')

    def read_spider1_deputy_data(self) -> dict:
        return self.read_file_data('batch_send_sms_data')
