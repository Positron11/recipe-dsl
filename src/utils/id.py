from dataclasses import field, Field
from typing import TypeVar, Callable, NewType
from nanoid import generate


# central ID types
ActionID             = NewType("ActionID", str)
IngredientID         = NewType("IngredientID", str)
EnvironmentID        = NewType("EnvironmentID", str)
ToolID               = NewType("ToolID", str)
LocationID           = NewType("LocationID", str)
ContainerID          = NewType("ContainerID", str)
CanonicalIngredientID= NewType("CanonicalIngredientID", str)
CanonicalTechniqueID = NewType("CanonicalTechniqueID", str)


# generic ID type
T = TypeVar("T", bound=str)

def id_field(factory: Callable[[str], T]) -> Field[T]:
    return field(default_factory=lambda: factory(generate(size=12)), init=False)
