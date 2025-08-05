import os

num_days = int(input("Enter the Folder days that you would want to create : "))

for i in range(1, num_days):
	folder_name = f"day-{21+i}"

	try : 
		os.makedirs(folder_name, exist_ok=True)
		print(f"Created folder: {folder_name}")
	except Exception as e : 
		print(f"Error creating folder {folder_name}: {e}")