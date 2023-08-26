import os
from colorama import Fore, Style
from .product import Product

class Inventory:

  def __init__(self):
    self.products = []
    self.next_product_id = 1

  def display_menu(self):
    print(f"{Fore.CYAN}1{Style.RESET_ALL}- {Fore.GREEN}Add product")
    print(f"{Fore.CYAN}2{Style.RESET_ALL}- {Fore.GREEN}Display all products")
    print(f"{Fore.CYAN}3{Style.RESET_ALL}- {Fore.RED}Exit")

  def clear_terminal(self):
    os.system('cls' if os.name == 'nt' else 'clear')

  def display_products(self):
    if not self.products:
      print(f"{Fore.YELLOW}\nTHERE ARE NO PRODUCTS YET...{Style.RESET_ALL}\n")
    else:
      for product_entry in self.products:
        product_id = product_entry['id']
        product = product_entry['product']
        print(f"\n{Fore.MAGENTA}PRODUCT ID: {product_id}")
        print(
            f"{Fore.YELLOW}Name: {product.name}\nCost: {product.cost:.2f}$\nQuantity: {product.quantity} \nDetails: {product.details}{Style.RESET_ALL}"
        )
        print("-" * 50)

  def add_product(self, name, details, cost, quantity):
    product = Product(name, details, cost, quantity)
    product_id = self.next_product_id
    self.next_product_id += 1
    self.products.append({'id': product_id, 'product': product})