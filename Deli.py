sandwich_orders = ["salami", "blt", "ham and cheese", "peanut butter and jelly", "tuna"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")

for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
    