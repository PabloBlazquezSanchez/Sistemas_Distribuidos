# Adding and multiplying an arbitrary number of integers using gRPC

In this exercise we will create a simple client-server application that adds or multiplies any number of integers. The client will send the request with the list of numbers, then the server will return the sum/multiplication of the numbers. The client must print the result, and the server must run forever, listening for incoming messages.

Design the schema. Then, implement this application in Python with gRPC and Protocol Buffers.

## Code Execution

### Environment Setup

1. **Install dependencies and create a virtual environment:**

    ```bash
    make install
    ```

2. **Generate Protocol Buffers files:**

    ```bash
    make proto
    ```

3. **Run the full preparation process:**

    ```bash
    make all
    ```

### Application Execution

1. **Run the server** (in one terminal):

    ```bash
    make run-server
    ```

    The server will run on `localhost:10001` and will keep listening for connections.

2. **Run the client** (in another terminal):

    ```bash
    make run-client
    ```

    This command will automatically execute three test cases:
    - Sum of numbers: `1 + 2 + 3 + 4 + 5`
    - Multiplication of numbers: `1 × 2 × 3 × 4 × 5`
    - Invalid operation (subtract) to test error handling

### Additional Commands

- **Clean generated files:**

  ```bash
  make clean
  ```

- **Clean everything (including the virtual environment):**

  ```bash
  make distclean
  ```

### Manual Client Usage

You can also run the client manually with different parameters:

```bash
# Activate virtual environment
. venv/bin/activate

# Sum of numbers
python client.py localhost:10001 add 10 20 30

# Multiplication of numbers
python client.py localhost:10001 multiply 2 3 4 5
```
