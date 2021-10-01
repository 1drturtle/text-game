from typing import Callable

from module_types import *
from player import *


class Game:
    def __init__(self):
        self.modules: Dict[int, Module] = dict()
        self.player = Player(hp=100)

    def load_modules(self, modules: List[Module]):
        for module in modules:
            self.modules[module.id] = module

    def begin(self):
        first_module = self.modules[min(self.modules.keys())]  # will always start with the smallest key.
        self.run_module(first_module.id)

    def run_module(self, module_id: int):
        module = self.modules[module_id]

        if module.intro:
            print(module.intro)

        types: Dict[ModuleTypes, Callable] = {
            ModuleTypes.advance: self.run_advance,
            ModuleTypes.choice: self.run_choice
        }
        func = types.get(module.type, None)
        if func:
            func(module_id)

    def run_advance(self, module_id: int):
        module = self.modules[module_id]
        if not isinstance(module, AdvanceModule):
            raise ValueError('Invalid Module, must be an instance of AdvanceModule')

        next_module = self.modules.get(module.next, None)
        if not next_module:
            raise IndexError(f'Could not find a next module with id {module.next}.')

        self.run_module(next_module.id)

    def run_choice(self, module_id: int):
        module = self.modules[module_id]
        if not isinstance(module, ChoiceModule):
            raise ValueError('Invalid Module, must be an instance of ChoiceModule')

        for i, choice in enumerate(module.choices):
            print(f'{i+1}) {choice.desc}')
