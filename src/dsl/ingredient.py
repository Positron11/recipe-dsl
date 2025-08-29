from dataclasses import dataclass, field
from typing import Optional

from .identifiers import id_field, CanonicalIngredientID
from .units import StandardUnit


@dataclass(frozen=True, slots=True)
class Ingredient:	
	ingredient:CanonicalIngredientID
	quantity:  float
	unit:      StandardUnit
	form:      Optional[str] = None
	
	modifiers:tuple[str, ...]=field(default_factory=tuple)
