from dataclasses import dataclass, field
from typing import Optional, NewType

from .utils.uid import uid_field
from .lexicon import ContainerID, LocationID


EnvironmentID = NewType("EnvironmentID", str)


@dataclass(frozen=True, slots=True)
class Environment:
	uid: EnvironmentID = uid_field(EnvironmentID)

	location:  LocationID
	container: Optional[ContainerID] = None
	
	modifiers:  tuple[str, ...] = field(default_factory=tuple)