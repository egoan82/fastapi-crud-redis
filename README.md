# FastAPI Redis API

This is an API built with FastAPI that interacts with a Redis database. The API allows performing CRUD (Create, Read, Update, Delete) operations on Redis.

## Requirements

- Python 3.8+
- Redis

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/egoan82/fastapi-with-redis.git
    cd fastapi-with-redis
    ```

2. Create a virtual environment:
    ```bash
    poetry shell
    ```

3. Install the dependencies:
    ```bash
    poetry install
    ```

4. Configure the environment variables in the `.env` file:
    ```dotenv
    REDIS_HOST="localhost"
    REDIS_PORT=6379
    ENVIRONMENT="local"
    ```

## Running the Application

To run the application, use the following command:
```bash
uvicorn main:app --port 8001 --reload
```

## Endpoints

### Search for a Key in Redis

- **URL**: `/v100/search`
- **Method**: `GET`
- **Description**: Searches for a key in Redis by pattern.
- **Parameters**:
  - `search` (query): Search pattern (key*).
- **Response**: List of keys matching the pattern.

### Create a Key-Value in Redis

- **URL**: `/v100/create`
- **Method**: `POST`
- **Description**: Creates a key-value in Redis.
- **Parameters**:
  - `key` (query): Key to create in Redis.
  - `value` (query): Value to create in Redis.
- **Response**: Success message.

### Get Value by Key in Redis

- **URL**: `/v100/get_by_key/{key}`
- **Method**: `GET`
- **Description**: Gets the value of a key in Redis.
- **Parameters**:
  - `key` (path): Key to search in Redis.
- **Response**: Value associated with the key.

### Delete a Key in Redis

- **URL**: `/v100/delete/{key}`
- **Method**: `DELETE`
- **Description**: Deletes a key in Redis.
- **Parameters**:
  - `key` (path): Key to delete in Redis.
- **Response**: Success message.

## Project Structure

```plaintext
.
├── api
│   ├── router.py
│   └── v100
│       └── routes
│           └── redis_api.py
├── dependencies
│   └── redis.py
├── core
│   └── settings.py
├── .env
├── requirements.txt
└── README.md
```

## Dependencies

- `fastapi`
- `redis`
- `uvicorn`

## Contributions

Contributions are welcome. Please open an issue or a pull request to discuss any changes you wish to make.

## License

This project is licensed under the terms of the MIT license.
```