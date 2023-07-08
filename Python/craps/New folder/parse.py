import csv

def remove_timestamp(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the header row

        # Find the index of the timestamp column
        timestamp_index = headers.index('Timestamp')

        # Remove the timestamp column from the headers
        headers.pop(timestamp_index)

        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)

            # Write the modified headers to the output file
            writer.writerow(headers)

            # Iterate through each row in the input file
            for row in reader:
                # Remove the timestamp column from the row data
                row.pop(timestamp_index)

                # Write the modified row to the output file
                writer.writerow(row)

    print(f"Timestamp removed from '{input_file}'. New CSV saved to '{output_file}'.")

# Usage example:
input_file = 'tonys.csv'
output_file = 'output.csv'
remove_timestamp(input_file, output_file)
