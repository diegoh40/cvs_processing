import csv
from collections import defaultdict


def process_csv(input_filename, output_filename):
    song_dict = defaultdict(dict)
    with open(input_filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = row["Song"]
            date = row["Date"]
            plays = int(row["Number of Plays"])
            print(song_dict)
            song_dict[song][date] = song_dict[song].get(date, 0) + plays
    with open(output_filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Song", "Date", "Total Number of Plays for Date"])
        for song, date_dict in song_dict.items(): # itera sobre el diccionario creando las lineas del CSV
            for date, total_plays in date_dict.items():
                writer.writerow([song, date, total_plays])# escribe el CSV
    print(song_dict,"LAST CREATED")
