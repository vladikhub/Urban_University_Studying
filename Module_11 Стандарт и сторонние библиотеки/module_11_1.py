import pprint

import requests
import pandas

data = requests.get("https://binaryjazz.us/wp-json/genrenator/v1/genre/").json()
print(data)

urban = requests.get("https://urban-university.ru")
pprint.pprint(urban.text)
print()
students_marks_dict = {"student": ["Студент_1", "Студент_2", "Студент_3"],
                       "math": [5, 3, 4],
                       "physics": [4, 5, 5]}
students = pandas.DataFrame(students_marks_dict)
print(students)


