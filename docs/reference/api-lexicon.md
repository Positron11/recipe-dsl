# Canonical Lexicon

Module: `dsl.lexicon`

Canonical entities provide stable IDs and optional metadata for tools, locations, containers, ingredients, and techniques. Use these `_uid`s throughout the DSL to reference domain concepts consistently.

```python
@dataclass(frozen=True, slots=True)
class CanonicalTool:
    _uid: CanonicalToolID = id_field(CanonicalToolID)
    name: str
    material: Optional[str] = None

@dataclass(frozen=True, slots=True)
class CanonicalLocation:
    _uid: CanonicalLocationID = id_field(CanonicalLocationID)
    name: str

@dataclass(frozen=True, slots=True)
class CanonicalContainer:
    _uid: CanonicalContainerID = id_field(CanonicalContainerID)
    name: str
    material: Optional[str] = None
    volume:   Optional[float] = None

@dataclass(frozen=True, slots=True)
class CanonicalIngredient:
    _uid: CanonicalIngredientID = id_field(CanonicalIngredientID)
    name: str

@dataclass(frozen=True, slots=True)
class ParamSpec:
    default: Optional[any] = None
    unit:    Optional[StandardUnit] = None
    bounds:  Optional[tuple] = None

@dataclass(frozen=True, slots=True)
class CanonicalTechnique:
    _uid: CanonicalTechniqueID = id_field(CanonicalTechniqueID)
    name:      str
    static:    tuple[str]
    parameters: Mapping[str, ParamSpec] = field(default_factory=lambda: MappingProxyType({}))
```

## Semantics

- Canonical entities represent normalized domain vocabulary. Their `_uid` should be used for cross-references.
- `CanonicalTechnique.static`: immutable list of qualitative tags (e.g. movements or fixed attributes like "stir").
- `ParamSpec`: optional schema for technique parameters; include `unit` and `bounds` where applicable.

## Usage

```python
from dsl.lexicon import (
  CanonicalTool, CanonicalLocation, CanonicalContainer,
  CanonicalIngredient, CanonicalTechnique, ParamSpec
)
from dsl.units import StandardUnit
from types import MappingProxyType

knife = CanonicalTool(name="chef's knife", material="steel")
board = CanonicalLocation(name="cutting board")
pan   = CanonicalContainer(name="frying pan", material="steel", volume=0.002)
onion = CanonicalIngredient(name="onion")

chop = CanonicalTechnique(
  name="chop",
  static=("dice",),
  parameters=MappingProxyType({
    "size": ParamSpec(default=0.01, unit=StandardUnit.LENGTH, bounds=(0.0, 0.05))
  })
)
```

