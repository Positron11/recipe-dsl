# Actions

Module: `dsl.action`

```python
@dataclass(frozen=True, slots=True)
class Action:
    _uid: ActionID = id_field(ActionID)
    inputs: tuple[Ingredient | ActionID]

@dataclass(frozen=True, slots=True)
class Process(Action):
    technique:   CanonicalTechniqueID
    tool:        Optional[CanonicalToolID] = None
    temperature: Optional[Temperature] = None
    time:        Optional[Timing] = None
    condition:   Optional[str] = None
    modifiers:   Optional[str] = None

@dataclass(frozen=True, slots=True)
class Transfer(Action):
    destination: Environment | ActionID
    time:        Optional[Timing] = None
    modifiers:   Optional[str] = None

@dataclass(frozen=True, slots=True)
class Plate(Action):
    description: str
```

## Semantics

- `Action.inputs` consumes either base `Ingredient` instances or outputs from prior actions referred to by `ActionID`.
- Each action implicitly produces a partially processed component (PPC) identified by its `_uid`.
- `Process` transforms state; `Transfer` relocates and associates an environment; `Plate` denotes presentation.
- `Process.condition` can describe non-time stop criteria (e.g. “until translucent”).
- `Transfer.destination` may be an `Environment` or an `ActionID` resolving to a previously established environment.

## Usage: Building a Simple Flow

```python
from dsl.lexicon import CanonicalIngredient, CanonicalTechnique, CanonicalTool
from dsl.ingredient import Ingredient
from dsl.action import Process, Transfer, Plate
from dsl.environment import Environment
from dsl.temperature import StaticTemperature, RampTemperature
from dsl.timing import Timing
from dsl.units import StandardUnit
from dsl.curves import linear

# Canonical definitions
egg_c = CanonicalIngredient(name="egg")
butter_c = CanonicalIngredient(name="butter")
pan_c = CanonicalTool(name="pan", material="steel")
fry = CanonicalTechnique(name="fry", static=("tilt",))

# Ingredients
egg = Ingredient(ingredient=egg_c._uid, quantity=2.0, unit=StandardUnit.WEIGHT, form="whole")
butter = Ingredient(ingredient=butter_c._uid, quantity=0.02, unit=StandardUnit.WEIGHT)

# Create environment and transfer butter to preheated pan
pan_env = Environment(container=pan_c._uid, modifiers=("preheated",))
t_butter = Transfer(inputs=(butter,), destination=pan_env)

# Fry egg with temperature ramp for 90 seconds
temp = RampTemperature(start=140.0, end=160.0, curve=linear)
p_fry = Process(
    inputs=(egg, t_butter._uid),
    technique=fry._uid,
    tool=pan_c._uid,
    temperature=temp,
    time=Timing(value=90),
)

plate = Plate(inputs=(p_fry._uid,), description="Sunny side up")
```

## Concurrency Patterns

- Parallel actions: create independent branches that both take the same predecessor `_uid` and rejoin later by passing their IDs forward to a common action.
- Interjections: create a secondary `Process` or `Transfer` with `Timing(relative_to=<primary_id>, value=<fraction>)` to schedule relative to progress of another step (e.g. add salt at `value=0.5`).
- Repeating tasks: set `Timing.repeating=True` for periodic actions such as stirring.

