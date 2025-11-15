"""
Take the items in this list of lists: 
[["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]] 
and write them to a CSV file. The data from each list should be a row in the file, with each item in the list separated by a comma.
"""
import csv

movies = [["Top Gun", "Risky Business", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fire", "Flight"]]
with open('movies.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(movies)
print("Movies have been written to movies.csv")
    