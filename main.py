from rich.console import Console

from processor import Processor

console = Console()
processor = Processor()


def select_processor():
    console.print('[green]请选择处理器: \n1. 获取客户号码\n2. 发送短信[/green]')

    while True:
        choice = input('请输入选择的编号: ')
        if choice in ['1', '2']:
            return choice
        else:
            print('请输入有效的选项编号')


def main():
    processor_choice = select_processor()
    if processor_choice == '1':
        console.print('[green]选择了处理器: 1. 获取客户号码[/green]')
        processor.main_processor()

    elif processor_choice == '2':
        console.print('[green]选择了处理器: 2. 发送短信[/green]')
        processor.deputy_processor()


if __name__ == '__main__':
    main()
