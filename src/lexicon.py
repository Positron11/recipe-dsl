from dataclasses import dataclass, field
from typing import Optional, NewType, Mapping

from .utils.uid import uid_field
from .units import StandardUnit


ToolID                = NewType("ToolID", str)
LocationID            = NewType("LocationID", str)
ContainerID           = NewType("ContainerID", str)
CanonicalIngredientID = NewType("CanonicalIngredientID", str)
CanonicalTechniqueID  = NewType("CanonicalTechniqueID", str)


@dataclass(frozen=True, slots=True)
class Tool:
    uid: ToolID = uid_field(ToolID)

    name:     str
    material: Optional[str] = None
    # ...


@dataclass(frozen=True, slots=True)
class Location:
    uid: LocationID = uid_field(LocationID)

    name:     str
    # ...


@dataclass(frozen=True, slots=True)
class Container:
    uid: ContainerID = uid_field(ContainerID)

    name:     str
    material: Optional[str] = None
    volume:   Optional[float] = None
    # ...


@dataclass(frozen=True, slots=True)
class CanonicalIngredient:
    uid: CanonicalIngredientID = uid_field(CanonicalIngredientID)

    name: str
    # ...


@dataclass(frozen=True, slots=True)
class ParamSpec:
    default: Optional[any] = None
    unit:    Optional[StandardUnit] = None
    bounds:  Optional[tuple] = None


@dataclass(frozen=True, slots=True)
class CanonicalTechnique:
    uid: CanonicalTechniqueID = uid_field(CanonicalTechniqueID)

    name:       str
    static:     tuple[str]
    parameters: Mapping[str, ParamSpec] = field(default_factory=lambda: MappingProxyType({}))
    # ...