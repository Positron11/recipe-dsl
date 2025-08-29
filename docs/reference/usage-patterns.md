# Usage Patterns and Examples

This guide shows common ways to compose the DSL building blocks to model realistic recipe steps.

## Recipe Graph Basics

1. Define canonical entities (tools, ingredients, techniques) to obtain stable IDs.
2. Instantiate `Ingredient`s with quantities and units.
3. Use `Transfer` to place items into environments (vessels and locations).
4. Use `Process` to apply a technique, optionally with temperature and time.
5. Thread action outputs by passing prior action `_uid`s as inputs to later actions.

```python
from dsl.lexicon import CanonicalIngredient, CanonicalTechnique, CanonicalTool
from dsl.ingredient import Ingredient
from dsl.action import Transfer, Process, Plate
from dsl.environment import Environment
from dsl.temperature import StaticTemperature
from dsl.timing import Timing
from dsl.units import StandardUnit

# Canonical
salt_c = CanonicalIngredient(name="salt")
water_c = CanonicalIngredient(name="water")
pot_c = CanonicalTool(name="saucepan", material="steel")
boil = CanonicalTechnique(name="boil", static=("simmer",))

# Inputs
salt = Ingredient(ingredient=salt_c._uid, quantity=0.01, unit=StandardUnit.WEIGHT)
water = Ingredient(ingredient=water_c._uid, quantity=1.0, unit=StandardUnit.VOLUME)

# Environment
pot_env = Environment(container=pot_c._uid, modifiers=("filled",))
t0 = Transfer(inputs=(water, salt), destination=pot_env)

# Process
p0 = Process(
  inputs=(t0._uid,),
  technique=boil._uid,
  tool=pot_c._uid,
  temperature=StaticTemperature(100.0),
  time=Timing(value=600),   # 10 minutes
)

plate = Plate(inputs=(p0._uid,), description="Boiled water with salt")
```

## Modeling Reuse of an Environment

Use an `ActionID` as a destination to refer to an environment established earlier:

```python
# Establish environment via a transfer
t_pan = Transfer(inputs=(), destination=Environment(container=pot_c._uid))

# Later, pour into that same pan by referencing the earlier action ID
t_again = Transfer(inputs=(water,), destination=t_pan._uid)
```

## Relative Interjections

Schedule additions relative to progress of a long-running process:

```python
saute = CanonicalTechnique(name="sauté", static=("stir",))
p_onions = Process(inputs=(onions,), technique=saute._uid, time=Timing(value=300))

# Add garlic halfway through
t_garlic = Transfer(
  inputs=(garlic,),
  destination=p_onions._uid,               # implicit current environment of onions
  time=Timing(value=0.5, relative_to=p_onions._uid)
)
```

## Periodic Tasks

Express recurring actions like stirring:

```python
stir = CanonicalTechnique(name="stir", static=())
stir_every_10s = Process(
  inputs=(p_onions._uid,),
  technique=stir._uid,
  time=Timing(value=10, repeating=True),
)
```

## Tips

- Keep canonical entries centralized if you need stable references across runs.
- Use `modifiers` to capture qualitative details until schema evolves.
- Consider wrapping graph creation in your own builder functions if you plan to execute/simulate steps.

