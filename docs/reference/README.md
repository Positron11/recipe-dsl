# Recipe DSL: Reference

Authoritative reference for the `dsl` package: core types, semantics, and usage patterns for modeling recipes as graphs of actions over ingredients and environments.

This reference complements conceptual docs in `docs/notes/` and focuses on concrete APIs and invariants.

## Contents

- Architecture and semantics: see `architecture.md`
- API Reference
  - Actions: `api-action.md`
  - Ingredients: `api-ingredient.md`
  - Environments: `api-environment.md`
  - Temperature profiles: `api-temperature.md`
  - Timing: `api-timing.md`
  - Canonical lexicon: `api-lexicon.md`
  - Units: `api-units.md`
  - Identifiers and IDs: `api-identifiers.md`
  - Curves: `api-curves.md`
- Usage Patterns and Examples: `usage-patterns.md`

## Conventions

- All DSL entities are immutable `dataclass` types with `slots` for memory efficiency.
- IDs are auto-generated with `nanoid` and are stored in the `_uid` field where present.
- Unit categories are standardized. Physical conversions are not implemented; interpret values in SI base units of the category (e.g. kilograms for `WEIGHT`).

