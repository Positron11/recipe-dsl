from dataclasses import dataclass, field
from typing import Optional, Mapping
from types import MappingProxyType

from .utils.id import id_field, CanonicalToolID, CanonicalLocationID, CanonicalContainerID, CanonicalIngredientID, CanonicalTechniqueID
from .units import StandardUnit


@dataclass(frozen=True, slots=True)
class CanonicalTool:
    _uid:CanonicalToolID=id_field(CanonicalToolID)

    name:    str
    material:Optional[str]=None
    # ...


@dataclass(frozen=True, slots=True)
class CanonicalLocation:
    _uid:CanonicalLocationID=id_field(CanonicalLocationID)
    
    name:str
    # ...


@dataclass(frozen=True, slots=True)
class CanonicalContainer:
    _uid:CanonicalContainerID=id_field(CanonicalContainerID)

    name:    str
    material:Optional[str]=None
    volume:  Optional[float]=None
    # ...


@dataclass(frozen=True, slots=True)
class CanonicalIngredient:
    _uid:CanonicalIngredientID=id_field(CanonicalIngredientID)

    name: str
    # ...


@dataclass(frozen=True, slots=True)
class ParamSpec:
    default:Optional[any]=None
    unit:   Optional[StandardUnit]=None
    bounds: Optional[tuple]=None


@dataclass(frozen=True, slots=True)
class CanonicalTechnique:
    _uid:CanonicalTechniqueID=id_field(CanonicalTechniqueID)

    name:      str
    static:    tuple[str]
    parameters:Mapping[str, ParamSpec]=field(default_factory=lambda: MappingProxyType({}))
    # ...
