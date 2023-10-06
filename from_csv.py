def parse_csv_file(csv_file):
	data =[]
	try:
		if csv_file.lower().endswith(".csv"):
			with open(csv_file, "r") as the_file:
				data = the_file.readlines()
				data = [line.strip() for line in data if line]
				data = [line.split(",") for line in data]
				return data if data else False
		else:
			print("File is not a CSV.")
			return False
	except FileNotFoundError:
		print(f"File not found: {csv_file}")
		return None
	except Exception as e:
		print(f"An error occurred: {str(e)}")
		return None
the_data = parse_csv_file("data.csv")

if the_data:
	for row in the_data:
		print(row)

# TO DO: More error catching etc