from collections import defaultdict

# Read the file
with open('Headlines_and_Dates.txt', 'r') as file:
    lines = file.readlines()

# Extract the date and headline, and count occurrences
date_headlines = defaultdict(list)
for line in lines:
    parts = line.split('T', 1)
    date = parts[0]
    headline_parts = parts[1].split(':', 3)
    headline = headline_parts[3].split('- ')
    headline = headline[0]
    date_headlines[date].append(headline)

# Print the date and headline counts
for date, headlines in date_headlines.items():
    print(f"{date}")
    for headline in headlines:
        print(f"{headline}")
   