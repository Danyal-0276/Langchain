from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


new_person: Person = {"name": "John Doe", "age": 30}


print(new_person)  # Output: {'name': 'John Doe', 'age': 30}


# =============================================================================
# When to Use What?
# =============================================================================
#
# Feature                      | TypedDict | Pydantic | JSON Schema
# -----------------------------|-----------|----------|-------------
# Basic structure              |    ✅     |    ✅    |     ✅
# Type enforcement             |    ✅     |    ✅    |     ✅
# Data validation              |    ❌     |    ✅    |     ✅
# Default values               |    ❌     |    ✅    |     ❌
# Automatic conversion         |    ❌     |    ✅    |     ❌
# Cross-language compatibility |    ❌     |    ❌    |     ✅
#
# =============================================================================
