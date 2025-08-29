# Ingredients

Module: `dsl.ingredient`

```python
@dataclass(frozen=True, slots=True)
class Ingredient:
    ingredient: CanonicalIngredientID
    quantity:   float
    unit:       StandardUnit
    form:       Optional[str] = None
    modifiers:  tuple[str, ...] = field(default_factory=tuple)
```

## Fields

- `ingredient`: ID referencing a canonical ingredient from the lexicon.
- `quantity`: Numeric value in the base unit of `unit` (see `StandardUnit`).
- `unit`: Category enum; interpret `quantity` accordingly.
- `form`: Optional specialization (e.g. “minced”, “whole”, “room temp”).
- `modifiers`: Free-form annotations. Use to capture details not yet formalized.

## Usage

```python
from dsl.lexicon import CanonicalIngredient
from dsl.units import StandardUnit
from dsl.ingredient import Ingredient

salt_c = CanonicalIngredient(name="salt")
salt = Ingredient(
    ingredient=salt_c._uid,
    quantity=0.002,            # 2 grams
    unit=StandardUnit.WEIGHT,
    form=None,
    modifiers=("kosher",),
)
```

Pass `Ingredient` instances directly as inputs to actions (see `api-action.md`).

