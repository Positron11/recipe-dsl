from dataclasses import dataclass, field
from typing import Optional, NewType

from .utils.uid import uid_field
from .units import StandardUnit
from .lexicon import CanonicalIngredientID


IngredientID = NewType("IngredientID", str)


@dataclass(frozen=True, slots=True)
class Ingredient:
	uid: IngredientID = uid_field(IngredientID)
	
	ingredient:	CanonicalIngredientID
	quantity: 	float
	unit: 		StandardUnit
	form: 		Optional[str] = None
	
	modifiers:  tuple[str, ...] = field(default_factory=tuple)