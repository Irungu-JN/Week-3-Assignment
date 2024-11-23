def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply the discount.
    Otherwise, return the original price.

    :param price: float, original price of the item
    :param discount_percent: float, discount percentage to apply
    :return: float, final price after applying discount or original price
    """
    if discount_percent >= 20:
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount
    else:
        return price

# Prompt user for inputs
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate and display the final price
    final_price = calculate_discount(original_price, discount_percentage)
    if final_price < original_price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
except ValueError:
    print("Please enter valid numerical values for the price and discount percentage.")
