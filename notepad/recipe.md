# Recipe

Documentation for a foundational understanding of what comprises a recipe.

## Table of Contents

- [Recipe](#recipe)
	- [Table of Contents](#table-of-contents)
	- [What is a Recipe?](#what-is-a-recipe)
	- [Recipe State](#recipe-state)
	- [Ingredients](#ingredients)
		- [Schema](#schema)
	- [Environments](#environments)
		- [Schema](#schema-1)
	- [Actions](#actions)
		- [`PROCESS`](#process)
			- [Schema](#schema-2)
			- [Temperature](#temperature)
				- [Schema](#schema-3)
		- [`TRANSFER`](#transfer)
			- [Environment Association](#environment-association)
		- [`PLATE`](#plate)
	- [Concurrency](#concurrency)
		- [Examples of Concurrency](#examples-of-concurrency)
		- [Interjections and Relative Timing](#interjections-and-relative-timing)
		- [Merging Semantics](#merging-semantics)

## What is a Recipe?

> **Recipe** [ˈrɛsɪpi] *n.* a directed sequence of actions that transform raw ingredients (ultimately, into a final dish) through structured operations. Each action consumes $\geq 1$ inputs, applies a well-defined action, and produces an (implicit) output, which may feed into subsequent steps.

- Actions are sequentially or concurrently composed, forming a directed acyclic graph (DAG) of transformations.

- Intermediate outputs are treated as partially processed components (PPCs), implicitly represented by the structure of the graph.

- The recipe yields a single final output, which may be an aggregation of multiple subcomponents (e.g. sauce, protein, garnish).

## Recipe State

A partially processed component (PPC) is any intermediate product resulting from one or more action steps applied to raw ingredients.

- PPCs are not explicitly represented as standalone nodes in the action graph. Instead, they are the implicit outputs of `PROCESS` and `TRANSFER` actions, passed directly as inputs to subsequent actions.

- The current state of a PPC - its form, temperature, texture, etc. - is inferred from the structure and parameters of the subgraph rooted at a given point.

- A PPC may recursively expand to a series of action steps that define how it was derived from base ingredients.

- Only the final output of the recipe is treated as an explicit, named PPC for presentation or aggregation purposes.

## Ingredients

Ingredients are the base components of a recipe, parameterized by *name* (reference to a standardized/canonical representation of the ingredient in a curated dataset) *quantity*, *unit*, *form*, and *modifiers*. They serve as the starting points for all action steps.

### Schema

```
name:      string
quantity:  float
unit:      string
form:      (optional) string
modifiers: (optional) list[string]
```

## Environments

An environment is described by an (optional) **container** (eg. pan, mixing bowl, baking tray) and a **location** (eg. counter, cutting board, stovetop)

- An ingredient is not associated with an environment by default.

- An ingredient or PPC is assigned an environment by a `TRANSFER` action (see below), and implicitly continues to be associated with this environment through any `PROCESS` steps.

### Schema

```
location:    string
container:   (optional) string
modifiers:   (optional) map
```

## Actions

We define a small set of generalized, atomic actions that form the structural backbone of any recipe. These actions represent transformations to ingredient state, position, or presentation. All recipe steps can be decomposed into one or more of these fundamental actions:

### `PROCESS`

A process represents a state-altering action applied to an ingredient or partially processed component (PPC). This includes any transformation - thermal, mechanical, or chemical - excluding relocation or plating. It is the primary unit of physical change in a recipe.

> **A process** can be conceptualized as: (Modifiers $\xrightarrow{\text{describe}}$ Technique $\xrightarrow{\text{applied to}}$ Item $\xrightarrow{\text{using}}$ Tool) $\xrightarrow{\text{at}}$ Temperature $\xrightarrow{\text{until}}$ Time Elapsed / Outcome Achieved

#### Schema

```
technique:   <Technique>
input:       <Ingredient> or PPC # i.e. another <Action>
tool:        <Tool>
temperature: (optional) <Temperature>
time:        (optional) <Timing>
condition:   (optional) string
modifiers:   (optional) string
```

*`technique` references an external technique lexicon with validation logic, default parameters, and postconditions.*

#### Temperature

We introduce an additional temperature component that defines a `START_TEMP`, `END_TEMP`, and a `TEMP_CURVE`, which interpolates between the given endpoints within the time frame defined by the parent process.

##### Schema

For ramping behavior:

```
start: float
end:   float
curve: (optional) <Curve> # callback that defines a curve
```

For static behavior:

```
value: float
```

### `TRANSFER`

Represents the **relocation** of an ingredient or PPC between environments. It does not alter the intrinsic state of the item but may initiate or terminate environmental effects (e.g. chilling, heating, resting) due to the new context.

- Transfers associate an item with a **new environment** (container and/or location).
- Transfers are used to:
  - Place ingredients into tools or cooking vessels (e.g. pan, oven tray)
  - Transition between locations (e.g. counter $\to$ oven)
  - Initiate context-sensitive processes (e.g. chilling by placing in fridge)
- `TRANSFER` can optionally include intent metadata (e.g. for resting, holding, staging)

#### Environment Association

After a `TRANSFER`, the item is implicitly associated with the destination environment in **all subsequent actions**, unless re-transferred.

### `PLATE`

Described in a single string field, as of now.

## Concurrency

A concurrent process is any set of actions that occur in **parallel over the same timeframe**, often operating on the same item or environment. This is used to model real-world multitasking in cooking, such as stirring while heating, or basting while frying.

Concurrent processes are represented as **parallel branches** in the action graph, which **merge at a synchronization point** once all branches are complete.

### Examples of Concurrency

- *"Gradually add flour while stirring milk at 60°C"*
- *"Fry the egg while tilting the pan"*

### Interjections and Relative Timing

Interjections (e.g. "add garlic halfway through sautéing onions") are modeled as **time-relative subprocesses** nested inside a primary action.

- These are also represented as concurrent actions, but are scheduled based on **relative time offsets** from a parent process.

- Relative timing can be expressed in the `Timing.relative_to` field

### Merging Semantics

All concurrent branches are **joined** at the end of their execution:

- The graph resumes from the point where all concurrent branches have completed.

- If one branch terminates earlier, it may **wait** or **produce partial effects** (implementation-defined).

