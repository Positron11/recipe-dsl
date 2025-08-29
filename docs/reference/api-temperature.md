# Temperature Profiles

Module: `dsl.temperature`

```python
@dataclass(frozen=True, slots=True)
class Temperature:
    unit: StandardUnit = field(default=StandardUnit.TEMPERATURE, init=False)

@dataclass(frozen=True, slots=True)
class RampTemperature(Temperature):
    start: float
    end:   float
    curve: Optional[Callable] = linear

    def value(self, completed: float) -> float:
        return self.curve(self.start, self.end, completed)

@dataclass(frozen=True, slots=True)
class StaticTemperature(Temperature):
    value: float
```

## Semantics

- All temperatures are expressed in degrees Celsius (`StandardUnit.TEMPERATURE`).
- `RampTemperature` uses a progress fraction `completed` in `[0, 1]` to compute an instantaneous temperature.
- Default curve is `dsl.curves.linear`. Any callable `(start: float, end: float, frac: float) -> float` is valid.

## Curves

See `dsl.curves` and `docs/reference/api-curves.md` for available functions and how to write custom ones.

## Usage

```python
from dsl.temperature import StaticTemperature, RampTemperature
from dsl.curves import exp_increase

static = StaticTemperature(160.0)  # °C
ramp = RampTemperature(start=120.0, end=180.0, curve=exp_increase)
snapshot = ramp.value(0.5)  # temperature at 50% progress
```

