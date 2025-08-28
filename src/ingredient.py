from dataclasses import dataclass, field
from typing import Optional

from .utils.id import id_field, IngredientID, CanonicalIngredientID
from .units import StandardUnit


@dataclass(frozen=True, slots=True)
class Ingredient:
	uid: IngredientID = id_field(IngredientID)
	
	ingredient:	CanonicalIngredientID
	quantity: 	float
	unit: 		StandardUnit
	form: 		Optional[str] = None
	
	modifiers:  tuple[str, ...] = field(default_factory=tuple)
