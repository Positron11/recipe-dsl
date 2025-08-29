# Timing

Module: `dsl.timing`

```python
@dataclass(frozen=True, slots=True)
class Timing:
    unit: StandardUnit = field(default=StandardUnit.TIME, init=False)
    value: float  # <1 => relative; >=1 => seconds
    relative_to: Optional[ActionID] = None
    blocking:    bool = False
    repeating:   bool = False
```

## Semantics

- `value < 1`: Interpret as a fraction of a reference duration (relative timing).
- `value >= 1`: Interpret as an absolute time in seconds.
- `relative_to`: When set, anchors relative timing to a specific `ActionID` (e.g. “halfway through sautéing onions”).
- `blocking`: When true, an executor should not advance beyond this step until the timing completes.
- `repeating`: Indicates recurrence (e.g. “stir every 10s”).

## Usage

```python
from dsl.timing import Timing

absolute = Timing(value=60)            # 60 seconds
relative = Timing(value=0.5)           # 50% of a reference
periodic = Timing(value=10, repeating=True)  # every 10s
```

Combine with actions (see `api-action.md`) to encode schedule constraints.

