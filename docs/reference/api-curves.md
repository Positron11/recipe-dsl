# Curves

Module: `dsl.curves`

```python
def linear(start: float, end: float, frac: float) -> float
def exp_increase(start: float, end: float, frac: float) -> float
```

## Semantics

- `linear`: Straight interpolation `start + (end - start) * frac`.
- `exp_increase`: Ease-in curve that accelerates as `frac → 1`. The implementation clamps `frac` to `[0, 1]` and normalizes an exponential profile.

## Custom Curves

A curve is any callable `(start: float, end: float, frac: float) -> float`.

Guidelines:

- Clamp or handle out-of-range `frac` (`<0` or `>1`) to avoid surprising values.
- Ensure monotonicity when modeling strictly increasing or decreasing profiles.
- Consider numerical stability at boundaries (`frac=0` and `frac=1`).

## Usage

```python
from dsl.temperature import RampTemperature

def quad(start, end, frac):
    f = max(0.0, min(1.0, frac))
    return start + (end - start) * (f * f)

temp = RampTemperature(start=100.0, end=160.0, curve=quad)
``` 

