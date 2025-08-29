# Environments

Module: `dsl.environment`

```python
@dataclass(frozen=True, slots=True)
class Environment:
    location:  Optional[CanonicalLocationID] = None
    container: Optional[CanonicalContainerID] = None
    modifiers: tuple[str, ...] = field(default_factory=tuple)
```

## Semantics

- An environment describes where and in what vessel an item resides (e.g. a pan on a stovetop, a bowl on a counter).
- Items are associated to environments via `Transfer` actions. The association persists for subsequent processes until changed by another transfer.
- `modifiers` can annotate environment state (e.g. “preheated”, “lined with parchment”).

## Usage

```python
from dsl.environment import Environment
from dsl.lexicon import CanonicalContainer, CanonicalLocation

pan = CanonicalContainer(name="frying pan", material="steel")
stove = CanonicalLocation(name="stovetop")

hot_pan = Environment(location=stove._uid, container=pan._uid, modifiers=("preheated",))
```

Use the environment as a `Transfer.destination` or reference it indirectly via an `ActionID` produced earlier (see `api-action.md`).

