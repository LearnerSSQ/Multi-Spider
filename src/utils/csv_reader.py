import csv
import os
import sys


class CSVReader:
    @staticmethod
    def read_csv(file_path: str) -> dict:
        data = {}
        try:
            with open(file_path, 'r', encoding='utf-8', newline='') as f:
                reader = csv.reader(f)
                next(reader)

                for row in reader:
                    param_name, param_value = row[:2]
                    data[param_name] = param_value

        except FileNotFoundError:
            print(f'错误: 文件 {file_path} 不存在')
            input('按任意键退出...')
            sys.exit(1)

        return data

    def read_headers(self) -> dict:
        cwd = os.getcwd()
        file_path = os.path.join(cwd, 'headers', 'headers.csv')
        return self.read_csv(file_path)

    def read_main_data(self) -> dict:
        cwd = os.getcwd()
        file_path = os.path.join(cwd, 'headers', 'main_data.csv')
        return self.read_csv(file_path)

    def read_deputy_data(self) -> dict:
        cwd = os.getcwd()
        file_path = os.path.join(cwd, 'headers', 'deputy_data.csv')
        return self.read_csv(file_path)
