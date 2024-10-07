In Python, **context managers** provide a way to allocate and release resources efficiently. The most common example is the `with` statement, which ensures that resources like files, locks, or network connections are properly cleaned up after their usage, regardless of whether an exception occurred or not. This eliminates the need to explicitly manage resources (like closing files) and helps prevent resource leaks.

### Key Points:
1. **Context managers** are used for setting up and cleaning up resources.
2. They ensure that resources are cleaned up automatically.
3. Commonly used with the `with` statement.

### Example:
Let's look at an example with file handling:

```python
with open('example.txt', 'r') as file:
    data = file.read()
    print(data)
# The file is automatically closed here, even if an exception occurs
```

In this example, Python's `open()` function returns a context manager. The file is automatically closed when the block under the `with` statement is exited, even if an error occurs within the block. This is a much cleaner way of handling resources compared to manually opening and closing the file using `file.close()`.

### How Context Managers Work
A context manager is an object that defines two methods:
1. `__enter__(self)`: Sets up the context and returns the resource.
2. `__exit__(self, exc_type, exc_value, traceback)`: Cleans up the resource, handling exceptions if necessary.

When you use a `with` statement:
- The `__enter__()` method is executed before the block starts.
- The `__exit__()` method is executed when the block finishes, whether it exits normally or due to an exception.

### Implementing a Custom Context Manager

You can implement your own context managers by defining these two methods. Here's an example of a custom context manager to handle a file:

```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file  # Return the file object to be used in the 'with' block

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()  # Ensure the file is closed when the block ends

# Usage
with FileManager('example.txt') as f:
    data = f.read()
    print(data)
```

In this case:
- `__enter__()` opens the file and returns it to be used inside the `with` block.
- `__exit__()` closes the file when the block exits.

### Context Managers Using `contextlib`
Python also provides a module called `contextlib` that simplifies the creation of context managers. For example, you can use the `@contextmanager` decorator to create context managers without the need to define a class.

Here’s an example:

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename):
    file = open(filename, 'r')
    try:
        yield file  # This is where the 'with' block runs
    finally:
        file.close()  # This runs after the block ends

# Usage
with file_manager('example.txt') as f:
    data = f.read()
    print(data)
```

### Benefits of Context Managers:
1. **Automatic resource management**: Resources like files, network connections, and locks are automatically cleaned up, even in case of errors.
2. **Cleaner code**: No need to write `try-finally` blocks manually to handle cleanup.
3. **Readability**: Using the `with` statement makes code more readable and concise.

### Use Cases of Context Managers:
- **File I/O**: Automatic closing of files after reading or writing.
- **Locking resources**: Ensuring exclusive access to resources like threads or databases.
- **Managing database connections**: Opening and closing connections or transactions.
- **Temporary changes in settings**: Temporarily modify settings or environment variables and revert them back afterward.

In summary, context managers provide a clean, efficient way to manage resources in Python by ensuring proper setup and teardown in an automated manner.