import json
import os
from typing import Dict, Any

class CategoriesRepository:
    def __init__(self):
        self.categories: Dict[str, Dict[str, Any]] = {}
        self.__file_path = os.path.join("db", "categories.json")
        self.__load_categories(self.__file_path)

    def __load_categories(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.categories = json.load(file)
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {file_path}.")

    def print_categories(self, categories=None, indent=0):
        # if no categories are passed, start from the root
        if categories is None:
            categories = self.categories

        for category, subcategories in categories.items():
            print(" " * indent + category)
            if isinstance(subcategories, dict) and subcategories:
                self.print_categories(subcategories, indent + 2)