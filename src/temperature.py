from dataclasses import dataclass, field
from typing import Optional, Callable

from .units import StandardUnit
from .curves import linear


@dataclass(frozen=True, slots=True)
class Temperature:
	unit:StandardUnit=field(default=StandardUnit.TEMPERATURE, init=False)


@dataclass(frozen=True, slots=True)
class RampTemperature(Temperature):
	start:float
	end:  float
	curve:Optional[Callable] = linear

	def value(self, completed:float) -> float:
		return self.curve(self.start, self.end, completed)


@dataclass(frozen=True, slots=True)
class StaticTemperature(Temperature):
	value:float
