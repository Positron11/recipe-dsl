# DSL Code Dev. Notes

Documentation for implementation design choices.

## Classes

- Using `dataclass`-es for immutable DSL entities, will use regular classes for orchestration.

- Prefer `frozen=True, slots=True` on dataclasses for immutability + memory savings.

### Units

- Define standardized units so we have a better translation target when parsing with LLMs

### Recipe DSL Entities

- Define `uid` field for all entities that will be explicitly extracted into the graph

- Use `modifiers` field or "..." comment as a cop-out for representation we haven't strictly figured out yet

## To-Do

- Data validation