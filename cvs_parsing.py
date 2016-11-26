import csv
import re


def max_crime(year, filename):
    count_dict = {}

    with open(filename) as f:
        for row in csv.reader(f, delimiter=","):
            date = row[2]
            primary_type = row[5]

            try:
                if re.search(r"\d{2}/\d{2}/(\d{4})", date).group(1) == year:
                    count_dict[primary_type] = count_dict.get(primary_type, 0) + 1

            except AttributeError:
                pass

    print(sorted(count_dict.items(), key=lambda x: x[1], reverse=True)[0][0])


max_crime("2015", "crimes.csv")
