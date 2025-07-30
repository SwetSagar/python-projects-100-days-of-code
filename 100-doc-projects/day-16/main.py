from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Name", ["Alice", "Bob", "Charlie"])
table.add_column("Age", [24, 30, 22])

table.align = "c"  # Align all columns to the left

print(table)