# Architecture and Semantics

This document explains how the DSL models a recipe as a graph of actions applied to ingredients within environments, and how timing and temperature constraints are represented.

## Core Concepts

- Ingredient: The base material with quantity, unit, and optional form/modifiers.
- Action: A step that consumes one or more inputs and implicitly produces an output (a partially processed component, PPC). An action’s identity is its `_uid`.
- Process: A state-transforming action (e.g. chop, sauté, bake) with optional tool, temperature, time, and stop condition.
- Transfer: A relocation action that associates the current item with a destination environment (container/location) and optional timing.
- Plate: A terminal action for presentation; currently stores a description.
- Environment: The context (location, container, modifiers) associated with an item after a transfer.
- Canonical Lexicon: Stable IDs and metadata for tools, locations, containers, ingredients, and techniques.
- Timing: Expresses absolute or relative time, with blocking and repeating flags for scheduling semantics.
- Temperature: Either static or ramping profile, with optional interpolation curve.

## Graph Model

- Each `Action` has a unique `_uid` (type `ActionID`).
- `Action.inputs` is a tuple of either `Ingredient` or `ActionID` values. Passing an `ActionID` references the PPC output of a previous action.
- The output of an action is implicit: use the action’s `_uid` as an input to downstream actions.
- `Transfer` assigns an environment to the moving item. That environment persists in conceptual context until another transfer occurs.
- `Process` applies a technique (optionally using a tool) and may define temperature and/or time windows.

### Environments as Destinations

`Transfer.destination` can be either:

- A concrete `Environment` instance, or
- An `ActionID` that resolves to an environment produced/associated by a prior step (e.g. “into the pan from step 3”). This indirection allows reuse of previously established environments.

## Immutability and IDs

- All DSL entities are `dataclass(frozen=True, slots=True)` to encourage declarative graph construction.
- Canonical entities in the lexicon expose their ID in an internal `_uid` field. Actions also carry `_uid`.
- Use these IDs when referencing entities across actions to avoid coupling to names.

## Units and Values

- `StandardUnit` defines categories: `TEMPERATURE`, `VOLUME`, `WEIGHT`, `LENGTH`, `TIME`.
- Values are interpreted in SI-like base units of each category:
  - WEIGHT: kilograms; 0.1 → 100 g
  - VOLUME: liters; 0.25 → 250 mL
  - TIME: seconds; 90 → 1.5 minutes
  - TEMPERATURE: degrees Celsius
  - LENGTH: meters

No automatic conversion helpers are provided; model sub-units via fractional values.

## Timing Semantics

- `Timing.value` < 1.0: fractional/relative (e.g. 0.5 = halfway through a reference).
- `Timing.value` ≥ 1.0: absolute time in seconds.
- `Timing.relative_to`: optional `ActionID` that anchors relative timing.
- `Timing.blocking`: if true, a scheduler should not advance past the step until completion.
- `Timing.repeating`: if true, indicates periodic behavior (e.g. stir every 10s).

## Temperature Profiles

- `StaticTemperature(value)` holds a constant °C value.
- `RampTemperature(start, end, curve)` interpolates from start to end in [0,1] progress via `curve(start,end,frac)`.
- Curves live in `dsl.curves` (e.g. `linear`, `exp_increase`) and can be user-defined callables.

## Concurrency and Scheduling

The DSL encodes constraints (time, temperature, tool, environment). It does not ship an execution engine, but supports modeling:

- Parallel branches by creating multiple actions that share predecessors and converge later.
- Interjections via `Timing.relative_to` to schedule a secondary action relative to a primary process (e.g. add salt at 0.5 progress).
- Blocking vs. non-blocking subtasks via `Timing.blocking`.

Downstream tooling (not included) can interpret these constraints to plan or simulate execution.

