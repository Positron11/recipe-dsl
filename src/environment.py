from dataclasses import dataclass, field
from typing import Optional

from .utils.id import id_field, EnvironmentID, ContainerID, LocationID


@dataclass(frozen=True, slots=True)
class Environment:
	uid: EnvironmentID = id_field(EnvironmentID)

	location:  LocationID
	container: Optional[ContainerID] = None
	
	modifiers:  tuple[str, ...] = field(default_factory=tuple)
