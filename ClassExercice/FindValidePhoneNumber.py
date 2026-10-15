import re

FILE_NAME = "fileDirectory/phones_numbers.txt"

with open(FILE_NAME, "w") as file:

    file.write("Mohamed: 06123456789\n"
               "Sara: +2126123456789\n"
               "Faux numero: 12345\n"
               "Tareq: 0623334455")


    numero_extrait = file.readlines()
    for i in numero_extrait:

        print(i.strip(re.search(r"[A-Za-z]$")))

#Non finit
