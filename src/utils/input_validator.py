import re


class InputValidator:
    # 正则表达式模式
    NUMBER_PATTERN = re.compile(r'^\d+$')

    @staticmethod
    def get_valid_input(prompt: str, min_val: int, max_val: int, exclude: int = None) -> int:
        while True:
            user_input = input(prompt)

            if InputValidator.NUMBER_PATTERN.match(user_input):
                user_input = int(user_input)

                if min_val <= user_input <= max_val and (exclude is None or user_input != exclude):
                    return user_input

            print("请输入有效且不重复的编号")
