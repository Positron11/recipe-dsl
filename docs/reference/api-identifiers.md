# Identifiers and ID Helpers

Module: `dsl.identifiers`

## Types

```python
ActionID              = NewType("ActionID", str)
CanonicalToolID       = NewType("CanonicalToolID", str)
CanonicalLocationID   = NewType("CanonicalLocationID", str)
CanonicalContainerID  = NewType("CanonicalContainerID", str)
CanonicalIngredientID = NewType("CanonicalIngredientID", str)
CanonicalTechniqueID  = NewType("CanonicalTechniqueID", str)
```

These are strong typedefs over `str` to make intent explicit across the API.

## `id_field`

```python
def id_field(factory: Callable[[str], T]) -> Field[T]
```

Helper for dataclasses to auto-generate a unique ID using `nanoid.generate(size=12)`. It stores the generated value in a field with `init=False`.

Usage pattern inside a dataclass:

```python
@dataclass(frozen=True, slots=True)
class CanonicalTool:
    _uid: CanonicalToolID = id_field(CanonicalToolID)
    # ...
```

## Dependency

- Requires `nanoid` at runtime. Install with: `python -m pip install nanoid`.

## Notes

- IDs are ephemeral unless persisted. Store `_uid` externally if deterministic cross-process linking is required.
- The `_uid` naming indicates intended internal use; reference IDs rather than names between entities.

