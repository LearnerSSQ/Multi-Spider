from network.spider0 import Spider0
from utils.csv_reader import CSVReader
from utils.excel_helper import ExcelHelper
from utils.input_validator import InputValidator


class Processor:
    def __init__(self):
        self.excel_helper = ExcelHelper()
        self.csv_reader = CSVReader()
        self.input_validator = InputValidator()
        self.spider = Spider0()

    def main_processor(self):
        getActWorkSheetListUrl = 'https://dqd30.jxdxxt.com/chnl-web/chnl/jx/mkt/workSheetExec/getActWorkSheetList'
        qryInfDownDataBasicCpcUrl = 'https://dqd30.jxdxxt.com/chnl-web/chnl/jx/mkt/workSheetExec/qryInfDownDataBasicCpc'

        headers = self.csv_reader.read_headers()
        main_data = self.csv_reader.read_main_data()
        deputy_data = self.csv_reader.read_deputy_data()

        selected_excel_file = self.excel_helper.select_excel_file()
        self.excel_helper.check_and_close_excel_file(selected_excel_file)
        read_column, write_column = self.excel_helper.select_excel_columns(selected_excel_file)
        customer_name = self.excel_helper.read_excel_columns(selected_excel_file, read_column)

        customer_number = self.spider.crawler(customer_name, getActWorkSheetListUrl, qryInfDownDataBasicCpcUrl,
                                              main_data, deputy_data, headers)

        self.excel_helper.write_to_excel(selected_excel_file, 2, write_column, customer_number)

    def deputy_processor(self):
        pass


def main():
    processor = Processor()
    processor.main_processor()


if __name__ == '__main__':
    main()
