import logging
import traceback
import collections
from typing import final

import awpy

from dict_converter import DictConverter
from data_structures import GameRound


@final
class Kast:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.rounds: list = []

    @classmethod
    def get_kast(cls, file_path: str) -> dict:
        self = cls()
        try:
            self._parse_demofile(file_path)
            player_rounds = self._get_player_rounds()
            return self._calculate_kast(player_rounds)
        except Exception as e:
            self.logger.info(
                f'KAST MODULE ERROR: {e.__class__.__name__}:{e}, '
                f'TRACEBACK:{traceback.extract_tb(e.__traceback__)}'
            )

    def _parse_demofile(self, file_path: str) -> None:
        parser = awpy.DemoParser(
            demofile=file_path,
            log=True,
        )
        game_data: dict = parser.parse()
        self.rounds: list[GameRound] = DictConverter.rounds_to_dataclasses(
            game_data['gameRounds'],
        )

    def _get_player_rounds(self) -> list:
        player_rounds = []

        for round_ in self.rounds:
            kills = round_.kills
            players = round_.ct_side.players + round_.t_side.players
            deaths = []
            involved_players = set()

            for kill in kills:
                involved_players.add(kill.attacker_name)
                deaths.append(kill.victim_name)

                if assister := kill.assister_name:
                    involved_players.add(assister)

                if trade := kill.player_traded_name:
                    involved_players.add(trade)

            for player in players:
                if player.player_name not in deaths:
                    involved_players.add(player.player_name)

            player_rounds.extend(list(involved_players))

        return player_rounds

    def _calculate_kast(self, player_rounds: list) -> dict:
        kast = dict(collections.Counter(player_rounds))

        for player, value in kast.items():
            kast[player] = round(value / len(self.rounds) * 100, 1)

        return kast
