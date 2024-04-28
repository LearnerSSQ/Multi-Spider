import re

from rich.console import Console


class InputValidator:
    NUMBER_PATTERN = re.compile(r'^\d+$')
    console = Console()

    @staticmethod
    def get_valid_input(prompt: str, min_val: int, max_val: int, exclude: int = None) -> int:
        while True:
            user_input = input(prompt)

            if user_input.strip() and InputValidator.NUMBER_PATTERN.match(user_input):
                user_input = int(user_input)

                if min_val <= user_input <= max_val and (exclude is None or user_input != exclude):
                    return user_input

            InputValidator.console.print("[bold red]请输入有效且不重复的编号[/bold red]")
