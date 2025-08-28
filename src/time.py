from dataclasses import dataclass, field
from typing import Optional

from .units import StandardUnit
from .utils.id import ActionID


@dataclass(frozen=True, slots=True)
class Timing:
	unit: StandardUnit=field(default=StandardUnit.TIME, init=False)
	value:float # values < 1 interpreted as fractionally relative, >= 1 interpreted in std. time units

	relative_to:Optional[ActionID]=None
	blocking:   bool=False
	repeating:  bool=False
