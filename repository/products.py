import json
import os
from typing import Dict, Any

class ProductsRepository:
    def __init__(self):
        self.products: Dict[str, Dict[str, Any]] = {}
        self.__file_path = os.path.join("db", "products.json")
        self.__load_products(self.__file_path)

    def add_product(self, product):
        self.products[product['id']] = product

    def get_products(self):
        return self.products

    def find_product(self, id):
        return self.products.get(id, None)
    
    def __load_products(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.products = json.load(file)
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {file_path}.")

    def remove_product(self, product_id: str):
        if product_id in self.products:
            del self.products[product_id]