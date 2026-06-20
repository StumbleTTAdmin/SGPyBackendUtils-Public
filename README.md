# StumbleUtils

A lightweight Python package for interacting with the Stumble Guys backend API.

## Included Features

- Create or log in to Stumble Guys accounts
- Use helper methods such as `Backend.search("Player")` to search usernames
- Send custom `GET`, `POST`, `PUT`, and `DELETE` requests to endpoints that are not directly wrapped by the utility

## Example Login Script

```python
from StumbleUtils import Backend

Backend.switchServer("live")
login = Backend.login("")
print(login)
```

## Example Usage

```python
from StumbleUtils import Backend

# Search for a player by username
result = Backend.search("Player")
print(result)
```

## Installation

```bash
pip install -e .
```
