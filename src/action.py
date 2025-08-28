from dataclasses import dataclass, field
from typing import Optional

from .utils.id import id_field, ActionID, CanonicalToolID, CanonicalTechniqueID
from .environment import Environment
from .ingredient import Ingredient
from .temperature import Temperature
from .time import Timing


@dataclass(frozen=True, slots=True)
class Action:
	_uid:ActionID=id_field(ActionID)
	  
	inputs:tuple[Ingredient|ActionID] # equivalent to "source" for Transfer


@dataclass(frozen=True, slots=True)
class Process(Action):
	technique:  CanonicalTechniqueID            # applied to input, using...
	tool:       Optional[CanonicalToolID]= None # at...
	temperature:Optional[Temperature]    = None # until...
	time:       Optional[Timing]         = None # or...
	condition:  Optional[str]            = None # is satisfied
	
	modifiers:Optional[str]=None


@dataclass(frozen=True, slots=True)
class Transfer(Action):
	destination:Environment|ActionID
	
	modifiers:Optional[str]=None
	

@dataclass(frozen=True, slots=True)
class Plate(Action):
	description:str
	# ...
