from dataclasses import dataclass, field
from typing import Optional

from .utils.id import id_field, ActionID, ToolID, CanonicalTechniqueID, IngredientID
from .temperature import Temperature
from .time import Timing


@dataclass(frozen=True, slots=True)
class Action:
	uid: ActionID = id_field(ActionID)
	  
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
