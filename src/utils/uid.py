from dataclasses import field, Field
from typing import TypeVar, Callable
from nanoid import generate


T = TypeVar("T", bound=str)


def uid_field(factory: Callable[[str], T]) -> Field[T]:
    return field(default_factory=lambda: factory(generate(size=12)), init=False)