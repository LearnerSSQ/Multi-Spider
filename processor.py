from src.network.spider0 import Spider0
from src.network.spider1 import Spider1
from src.utils.csv_reader import CSVReader
from src.utils.excel_helper import ExcelHelper
from src.utils.input_validator import InputValidator


class Processor:
    def __init__(self):
        self.excel_helper = ExcelHelper()
        self.csv_reader = CSVReader()
        self.input_validator = InputValidator()
        self.spider0 = Spider0()
        self.spider1 = Spider1()

    def main_processor(self):
        getActWorkSheetListUrl = 'https://dqd30.jxdxxt.com/chnl-web/chnl/jx/mkt/workSheetExec/getActWorkSheetList'
        qryInfDownDataBasicCpcUrl = 'https://dqd30.jxdxxt.com/chnl-web/chnl/jx/mkt/workSheetExec/qryInfDownDataBasicCpc'

        headers = self.csv_reader.read_headers()
        main_data = self.csv_reader.read_spider0_main_data()
        deputy_data = self.csv_reader.read_spider0_deputy_data()

        selected_excel_file = self.excel_helper.select_excel_file()
        self.excel_helper.check_and_close_excel_file(selected_excel_file)
        read_column, write_column = self.excel_helper.select_excel_columns(selected_excel_file)
        mixed = self.excel_helper.read_excel_columns(selected_excel_file, read_column, read_column)

        customer_name = []
        for mix in mixed:
            customer_name.append(mix[0])

        customer_number = self.spider0.crawler(customer_name, getActWorkSheetListUrl, qryInfDownDataBasicCpcUrl,
                                               main_data, deputy_data, headers)

        self.excel_helper.write_to_excel(selected_excel_file, 2, write_column, customer_number)

    def deputy_processor(self):
        nbrValidataUrl = 'https://dqd30.jxdxxt.com/chnl-web/chnl/jx/mkt/workSheetExec/nbrValidata'
        batchSendSmsUrl = 'https://dqd30.jxdxxt.com/chnl-web/chnl/jx/mkt/workSheetExec/batchSendSms'

        headers = self.csv_reader.read_headers()
        main_data = self.csv_reader.read_spider1_main_data()
        deputy_data = self.csv_reader.read_spider1_deputy_data()

        selected_excel_file = self.excel_helper.select_excel_file()
        self.excel_helper.check_and_close_excel_file(selected_excel_file)
        read_column, write_column = self.excel_helper.select_excel_columns(selected_excel_file)
        mixed = self.excel_helper.read_excel_columns(selected_excel_file, read_column, read_column + 1)

        send_nbr, sum_content = [], []
        for mix in mixed:
            send_nbr.append(mix[0])
            sum_content.append(mix[1])

        result = self.spider1.crawler(send_nbr, sum_content, nbrValidataUrl, batchSendSmsUrl,
                                      main_data, deputy_data, headers)

        self.excel_helper.write_to_excel(selected_excel_file, 2, write_column, result)
