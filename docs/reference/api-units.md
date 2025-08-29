# Units

Module: `dsl.units`

```python
class StandardUnit(Enum):
    TEMPERATURE = "C"
    VOLUME      = "l"
    WEIGHT      = "kg"
    LENGTH      = "m"
    TIME        = "s"
```

## Semantics

- Each enumeration member represents a category and its canonical SI-like base unit:
  - TEMPERATURE: degrees Celsius
  - VOLUME: liters
  - WEIGHT: kilograms
  - LENGTH: meters
  - TIME: seconds

Values should be provided in the base unit for the category, using fractional values for sub-units (e.g. 0.25 liters = 250 mL, 0.001 kg = 1 g).

## Conversions

No built-in conversion helpers are provided. Keep quantities normalized at instantiation.

