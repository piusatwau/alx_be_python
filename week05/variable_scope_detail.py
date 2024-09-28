# Global Namespace
x = 10  # Global variable

def outer_function():
    # Enclosing Namespace
    x = 20  # Enclosing variable

    def inner_function():
        # Local Namespace
        x = 30  # Local variable
        print("Inside inner_function:", x)  # Accesses local x (30)
    
    inner_function()
    print("Inside outer_function:", x)  # Accesses enclosing x (20)

outer_function()
print("In the global scope:", x)  # Accesses global x (10)
