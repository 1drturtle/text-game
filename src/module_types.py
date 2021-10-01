from enum import Enum
from typing import List

from pydantic import BaseModel


class ModuleTypes(str, Enum):
    advance = 'advance'
    choice = 'choice'
    outcome = 'outcome'


class Module(BaseModel):
    id: int
    type: ModuleTypes
    intro: str = ''


class AdvanceModule(Module):
    next: int


class Choice(BaseModel):
    desc: str
    outcome: int  # module ID


class ChoiceModule(Module):
    choices: List[Choice]


class OutcomeModule(AdvanceModule):
    hp_change: int = 0
    inv_gain: List[str] = []
    inv_loss: List[str] = []
