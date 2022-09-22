import json
import logging
import collections
from typing import final

import awpy


@final
class Kast:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.rounds: list = []

    @classmethod
    def get_kast(cls, file_path: str) -> dict:
        try:
            self = cls()
            self._parse_demofile(file_path)
            player_rounds = self._get_player_rounds()
            return self._calculate_kast(player_rounds)
        except Exception as e:
            cls().logger.info(f'KAST MODULE ERROR: {e.__class__.__name__}:{e}')

    def _parse_demofile(self, file_path: str) -> None:
        parser = awpy.DemoParser(
            demofile=file_path,
            log=True,
        )
        game_data: dict = parser.parse()
        self.rounds = game_data['gameRounds']

    def _get_player_rounds(self) -> list:
        player_rounds = []

        for round_ in self.rounds:
            kills = round_['kills']
            players = round_['ctSide']['players'] + round_['tSide']['players']
            deaths = []
            involved_players = set()

            for kill in kills:
                involved_players.add(kill['attackerName'])
                deaths.append(kill['victimName'])

                if assister := kill['assisterName']:
                    involved_players.add(assister)

                if trade := kill['playerTradedName']:
                    involved_players.add(trade)

            for player in players:
                if player['playerName'] not in deaths:
                    involved_players.add(player['playerName'])

            player_rounds.extend(list(involved_players))

        return player_rounds

    def _calculate_kast(self, player_rounds: list) -> dict:
        kast = dict(collections.Counter(player_rounds))

        for player, value in kast.items():
            kast[player] = round(value / len(self.rounds) * 100, 1)

        return kast
