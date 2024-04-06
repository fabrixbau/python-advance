# Trabajos con archivos csv
import csv
from pathlib import Path


FILE_PATH = Path('users.csv')


def read_csv():
    try:
        with open(FILE_PATH, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row.get('first_name'), ' : ', row.get('email'))
    except Exception as e:
        print('no se encontro el archivo', e)


def write_csv():
    try:
        with open(
            FILE_PATH, "a", newline=""
        ) as file:
            writer = csv.DictWriter(
                file, fieldnames=["first_name", "last_name", "email"]
            )
            writer.writerows(
                [
                    {
                        "first_name": "Fabrizio",
                        "last_name": "Bautista",
                        "email": "bautistafabrizio@gmail",
                    },
                    {
                        "first_name": "Jose",
                        "last_name": "Jimenez",
                        "email": "jimenezfabrizio@gmail.com",
                    },
                ]
            )
    except Exception as e:
        print("Ocurrió un error:", e)


if __name__ == '__main__':
    write_csv()
    read_csv()
