import os
import sys

from openpyxl.reader.excel import load_workbook
from rich import print
from rich.console import Console

from input_validator import InputValidator


class ExcelHelper:
    def __init__(self):
        self.console = Console()
        self.input_validator = InputValidator()

    def select_excel_file(self) -> str:
        excel_files = [file for file in os.listdir('.') if file.endswith('.xlsx')]

        if not excel_files:
            print("[bold red]当前目录下没有找到任何 .xlsx 文件[/bold red]")
            input('按任意键退出...')
            sys.exit(1)

        print('[bold]找到了以下 .xlsx 文件[/bold]')
        self.console.print("-" * 50)

        for idx, excel_file in enumerate(excel_files, start=1):
            self.console.print(f'{idx}. {excel_file}')

        self.console.print("-" * 50)

        select_idx = self.input_validator.get_valid_input("请输入要读取的 Excel 文件序号: ", 1, len(excel_files))

        return excel_files[select_idx - 1]

    def select_excel_columns(self, file_path: str) -> tuple:
        wb = load_workbook(filename=file_path)
        sheet = wb.active

        self.console.print("[bold]展示Excel文件标题行如下[/bold]")
        self.console.print("-" * 50)

        for idx, cell in enumerate(sheet[1], start=1):
            self.console.print(f"{idx}. {cell.value}")

        self.console.print("-" * 50)

        read_col_num = self.input_validator.get_valid_input("请输入需要读取数据的列编号: ", 1, sheet.max_column)
        self.console.print('覆写的内容为N行3列,内容为"新增用户名, 新增联系号码1, 新增联系号码2",只需要选取最左侧的列即可'
                           '\n举例: 如果选取了第4列，那么数据将会覆盖到第4, 5, 6列')
        write_col_num = self.input_validator.get_valid_input("请输入需要进行覆写的列编号: ", 1, sheet.max_column,
                                                             exclude=read_col_num)

        return read_col_num, write_col_num

    @staticmethod
    def read_excel_columns(read_excel_file: str, read_col_num: int) -> list:
        result = []

        wb = load_workbook(read_excel_file)
        sheet = wb.active

        for row in sheet.iter_rows(min_row=2, min_col=read_col_num, max_col=read_col_num, values_only=True):
            if row[0] is not None:
                result.append(row[0])
            else:
                break

        return result

    @staticmethod
    def write_to_excel(selected_excel_file: str, start_row: int, start_column: int, data_to_write: list) -> None:
        wb = load_workbook(filename=selected_excel_file)
        sheet = wb.active

        for row_index, row_data in enumerate(data_to_write, start=start_row):
            for column_index, cell_value in enumerate(row_data, start=start_column):
                sheet.cell(row=row_index, column=column_index, value=cell_value)

        wb.save(selected_excel_file)

    @staticmethod
    def check_and_close_excel_file(file_path: str) -> None:
        try:
            wb = load_workbook(filename=file_path)
            wb.close()
            print(f"[green]文件 {file_path} 未被打开,或已成功关闭,\n可以进行下一步操作[/green]")
            print("-" * 50)

        except PermissionError:
            print(f"[bold red]文件 {file_path} 当前被打开,请关闭它后再试[/bold red]")
            input('按任意键退出...')
            sys.exit(1)

        except Exception as e:
            print(f"[bold red]检查文件时出现未知错误: {e}[/bold red]")
            input('按任意键退出...')
            sys.exit(1)
