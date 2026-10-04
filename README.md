# Contracts Lab: Routes Request Response Cycle

## Description

A small Flask application that manages sensitive contract and customer data. It has two routes and uses two response codes:

- **204**: the request succeeded but there is no data to send back (used to confirm a customer exists without exposing information).
- **404**: the requested data was not found.

## Installation

1. Fork and clone this repository.
2. Install the dependencies: `pipenv install`
3. Open the virtual environment: `pipenv shell`

## Usage

Start the server:

```
python3 server/app.py
```

The app runs at `http://localhost:5555`.

### Routes

| Route | Result | Status |
|---|---|---|
| `/contract/<id>` | Contract found, returns its information | 200 |
| `/contract/<id>` | Contract not found | 404 |
| `/customer/<customer_name>` | Customer found, empty body (data is sensitive) | 204 |
| `/customer/<customer_name>` | Customer not found | 404 |

## Testing

Run the autotests from the project's main folder:

```
pytest
```

The tests check all four behaviors above:

- `/contract/<id>` created with correct response
- `/contract/<id>` created with failed response
- `/customer/<customer_name>` created with correct response
- `/customer/<customer_name>` created with failed response

### Screenshot of completed work

![All tests passing](screenshots/tests-passed.png)