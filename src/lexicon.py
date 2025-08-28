from dataclasses import dataclass, field
from typing import Optional, Mapping
from types import MappingProxyType

from .utils.id import id_field, ToolID, LocationID, ContainerID, CanonicalIngredientID, CanonicalTechniqueID
from .units import StandardUnit


@dataclass(frozen=True, slots=True)
class Tool:
    uid: ToolID = id_field(ToolID)

    name:     str
    material: Optional[str] = None
    # ...


@dataclass(frozen=True, slots=True)
class Location:
    uid: LocationID = id_field(LocationID)

    name:     str
    # ...


@dataclass(frozen=True, slots=True)
class Container:
    uid: ContainerID = id_field(ContainerID)

    name:     str
    material: Optional[str] = None
    volume:   Optional[float] = None
    # ...


@dataclass(frozen=True, slots=True)
class CanonicalIngredient:
    uid: CanonicalIngredientID = id_field(CanonicalIngredientID)

    name: str
    # ...


@dataclass(frozen=True, slots=True)
class ParamSpec:
    default: Optional[any] = None
    unit:    Optional[StandardUnit] = None
    bounds:  Optional[tuple] = None


@dataclass(frozen=True, slots=True)
class CanonicalTechnique:
    uid: CanonicalTechniqueID = id_field(CanonicalTechniqueID)

    name:       str
    static:     tuple[str]
    parameters: Mapping[str, ParamSpec] = field(default_factory=lambda: MappingProxyType({}))
    # ...
