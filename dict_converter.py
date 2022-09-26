import re
from typing import Union

import dacite

from data_structures import GameRound


class DictConverter:
    @classmethod
    def rounds_to_dataclasses(cls, rounds: dict) -> list[GameRound]:
        cls._fields_to_snake_case(rounds)
        return [
            dacite.from_dict(
                data_class=GameRound,
                data=round_,
            ) for round_ in rounds
        ]

    @classmethod
    def _fields_to_snake_case(cls, data: Union[dict, list]) -> None:
        if isinstance(data, dict):
            for key, value in list(data.items()):
                if isinstance(value, (dict, list)):
                    cls._fields_to_snake_case(value)
                data[cls._camel_case_to_snake_case(key)] = data.pop(key)
        elif isinstance(data, list):
            for item in data:
                cls._fields_to_snake_case(item)

    @staticmethod
    def _camel_case_to_snake_case(word: str) -> str:
        word = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', word)
        word = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', word)
        word = word.replace('-', '_')
        return word.lower()
