#Mark Hendri
#Professor Eckert
#Average From Input File Assignment

# Open the file and initialize the sum and count variables
with open('numbers.txt', 'r') as f:
    total = 0
    count = 0

    # Read each line of the file using a while loop
    line = f.readline()
    while line:
        # Convert the line to an integer and add it to the sum
        num = int(line.strip())
        total += num

        # Increment the count and print the current sum and count
        count += 1
        print(f"I read in {count} number(s). Current number is: {num:.2f}. Total is: {total:.2f}")

        # Read the next line
        line = f.readline()

    # Calculate and print the average
    if count > 0:
        average = total / count
        print("Average:")
        print(f"{average:.1f}")



