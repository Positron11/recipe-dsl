# DSL Code Dev. Notes

Documentation for implementation design choices.

## Classes

- Using `dataclass`-es for immutable DSL entities, will use regular classes for orchestration.

- Prefer `frozen=True, slots=True` on dataclasses for immutability + memory savings.

### Units

- Define standardized units so we have a better translation target when parsing with LLMs

### Recipe DSL Entities

- Define `_uid` field for all entities that will be explicitly extracted into the graph

- Use `modifiers` field or "..." comment as a cop-out for representation we haven't strictly figured out yet

## Challenges (Playground)

- Name `Action` instances accordng to their PPC output
- Used LLMs as much as possible to generate challenge solutions, as a sort of "proof of concept" for development of automated pipeline

## To-Do

- Data validation
- lexicon construction and instance loader 
- DSL compiler