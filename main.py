from colorama import init, Fore, Style
from inventory_system.inventory import Inventory

init(autoreset=True)  # Initialize colorama


def main():
  inventory = Inventory()
  inventory.clear_terminal()

  while True:
    inventory.display_menu()
    choice = input("\nEnter your choice: ")

    inventory.clear_terminal()

    if choice == '1':
      name = input("Enter the product name: ")
      details = input("Enter details of the product: ")

      while True:
        try:
          cost = float(input("Enter the product cost: "))
          break
        except ValueError:
          print(
              f"{Fore.RED}Please enter a valid number for cost.{Style.RESET_ALL}"
          )

      while True:
        try:
          quantity = int(input("Enter the product quantity: "))
          break
        except ValueError:
          print(
              f"{Fore.RED}Please enter a valid integer for quantity.{Style.RESET_ALL}"
          )

      inventory.add_product(name, details, cost, quantity)
      inventory.clear_terminal()
    elif choice == '2':
      inventory.clear_terminal()
      inventory.display_products()

    elif choice == '3':
      print(f"{Fore.RED}\nExiting the program.{Style.RESET_ALL}\n")
      break

    else:
      print(
          f"{Fore.RED}\nInvalid choice. Please select a valid option.{Style.RESET_ALL}\n"
      )


if __name__ == "__main__":
  main()
