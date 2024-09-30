# creating a laptop class that will capture information about laptops in a given laptop store
class Laptop:
    def __init__(self, manufacturer, model, processor, ram, storage, gpu=None, price=None, release_year=None, os="Windows"):
        self.manufacturer = manufacturer  # Laptop brand, e.g., 'Dell', 'HP', 'Apple'
        self.model = model  # Model name, e.g., 'XPS 13', 'MacBook Pro'
        self.processor = processor  # Processor info, e.g., 'Intel i7', 'AMD Ryzen 5'
        self.ram = ram  # RAM size in GB, e.g., 8, 16
        self.storage = storage  # Storage capacity in GB or TB, e.g., '512GB SSD', '1TB HDD'
        self.gpu = gpu  # Optional: GPU, e.g., 'NVIDIA GTX 1650' (default is None)
        self.price = price  # Optional: Price of the laptop (default is None)
        self.release_year = release_year  # Optional: Release year of the laptop (default is None)
        self.os = os  # Operating system (default is 'Windows')

    def __str__(self):
        return (f"Laptop: {self.manufacturer} {self.model}\n"
                f"Processor: {self.processor}\n"
                f"RAM: {self.ram}GB\n"
                f"Storage: {self.storage}\n"
                f"GPU: {self.gpu if self.gpu else 'Integrated'}\n"
                f"Operating System: {self.os}\n"
                f"Price: {'$'+str(self.price) if self.price else 'N/A'}\n"
                f"Release Year: {self.release_year if self.release_year else 'Unknown'}")

# Example usage:
laptop1 = Laptop(manufacturer="Apple", model="MacBook Air", processor="M1", ram=8, storage="256GB SSD", price=999, release_year=2020)
laptop2 = Laptop(manufacturer="Dell", model="XPS 13", processor="Intel i7", ram=16, storage="512GB SSD", gpu="Intel Iris Xe", os="Ubuntu", release_year=2021)

print(laptop1)
print()
print(laptop2)
