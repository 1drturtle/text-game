import json
import os

from devtools import debug

from game import Game
from module_types import *


MODULE_REFERENCE = {
    ModuleTypes.choice: ChoiceModule,
    ModuleTypes.advance: AdvanceModule,
    ModuleTypes.outcome: OutcomeModule
}


def load_modules():
    # all json files in modules

    files = list(filter(lambda x: x.endswith('.json'), os.listdir('modules')))
    modules: List[Module] = []
    for file in files:
        with open(f'modules/{file}', 'r') as fp:
            data = json.load(fp)
            if isinstance(data, list):
                for x in data:
                    module = MODULE_REFERENCE[x.get('type')](**x)
                    modules.append(module)
            elif isinstance(data, dict):
                module = MODULE_REFERENCE[data.get('type')](**data)
                modules.append(module)

    return modules


if __name__ == '__main__':

    game = Game()

    game.load_modules(load_modules())

    game.begin()
    debug(game.player)
