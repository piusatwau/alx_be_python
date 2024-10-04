import unittest

# List all the callables (functions and classes) in the unittest module
callable_items = [item for item in dir(unittest) if callable(getattr(unittest, item))]

# Print the callable items
print(callable_items)


