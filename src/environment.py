from dataclasses import dataclass, field
from typing import Optional

from .utils.id import id_field, CanonicalContainerID, CanonicalLocationID


@dataclass(frozen=True, slots=True)
class Environment:
	location: Optional[CanonicalLocationID]=None
	container:Optional[CanonicalContainerID]=None
	
	modifiers:tuple[str, ...]=field(default_factory=tuple)
