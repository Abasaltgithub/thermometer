import csv

# Replace 'your_file.csv' with the path to your CSV file
input_csv_file = 'S5_test.csv'
# Adjust the output file as needed
output_csv_file = 'S5_test_edited.csv'

# Initialize a set to store unique "S1 temp" values
unique_s1_temp_values = set()

# Open the input CSV file
with open(input_csv_file, 'r') as input_file:
    # Create a CSV reader object
    csv_reader = csv.reader(input_file)

    # Open the output CSV file for writing
    with open(output_csv_file, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)

        # Iterate through the rows in the input file
        for row in csv_reader:
            # Assuming "S1 temp" is in the first column (adjust index if needed)
            s1_temp = row[0]

            # Check if the "S1 temp" value is not in the set of unique values
            if s1_temp not in unique_s1_temp_values:
                # If it's not in the set, write the row to the output file and add it to the set
                csv_writer.writerow(row)
                unique_s1_temp_values.add(s1_temp)

# Print the total number of rows in the original and output CSV files
print(f"Number of rows in {input_csv_file}: {len(unique_s1_temp_values)}")
print(f"Number of rows in {output_csv_file}: {len(unique_s1_temp_values)}")
