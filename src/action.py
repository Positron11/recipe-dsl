from dataclasses import dataclass, field
from typing import Optional, NewType
from nanoid import generate

from .utils.uid import uid_field
from .lexicon import ToolID, CanonicalTechniqueID
from .ingredient import IngredientID
from .temperature import Temperature
from .time import Timing


ActionID = NewType("ActionID", str)


@dataclass(frozen=True, slots=True)
class Action:
	uid: ActionID = uid_field(ActionID)
	  
	inputs: tuple[IngredientID|ActionID]


@dataclass(frozen=True, slots=True)
class Process(Action):
	technique:   CanonicalTechniqueID         # applied to input, using...
	tool:        Optional[ToolID] = None      # at...
	temperature: Optional[Temperature] = None # until...
	time:        Optional[Timing] = None      # or...
	condition:   Optional[str] = None         # is satisfied
	
	modifiers:   Optional[str] = None


@dataclass(frozen=True, slots=True)
class Transfer(Action):
	modifiers: Optional[str] = None
	# ...
	

@dataclass(frozen=True, slots=True)
class Plate(Action):
	description: str
	# ...