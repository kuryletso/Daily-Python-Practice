# Excercise: https://www.hackinscience.org/exercises/csv-and-python
#
#
# Solution:

from collections.abc import Iterable
import csv, datetime



def format_value(v):
    match v:
        case datetime.date():
            return f"{v:%m/%d/%Y}"
        case str():
            return v
        case Iterable():
            return ",".join(i for i in v)
        case _:
            return v

def generate_csv(a_list):
    with open(r"results.csv", "w", newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(i[0] for i in a_list[0])
        for row in a_list:
            csv_writer.writerow(format_value(d[1]) for d in row)



def parse_csv():
    with open(r"students.csv", "r", newline='') as f:
        csv_reader = csv.DictReader(f)
        result = [*csv_reader]
        for r in result:
            r['Birthdate'] = datetime.datetime.strptime(r['Birthdate'], '%m/%d/%Y').date()
            r['Marks'] = list(map(lambda x: int(x), r['Marks'].split(",")))
        return result



if __name__ == "__main__":
    meteo1 = [(('temperature', 42),
            ('date', datetime.date(2017, 1, 22)),
            ('locations', ('Berlin', 'Paris')),
            ('weather', 'sunny')),
            (('temperature', -42),
            ('date', datetime.date(2017, 1, 22)),
            ('locations', ('Marseille', 'Moscow')),
            ('weather', 'cloudy'))]
    meteo = [
            (('temperature', 21), ('date', datetime.date(2042, 2, 22)), ('locations', ('Lyon', 'Nime', 'Paris')), ('weather', 'sunny')),
            (('temperature', -21), ('date', datetime.date(2000, 1, 22)), ('locations', ['Moscow', 'Budapest']), ('weather', 'something strange'))]
    generate_csv(meteo)
    print(parse_csv())
