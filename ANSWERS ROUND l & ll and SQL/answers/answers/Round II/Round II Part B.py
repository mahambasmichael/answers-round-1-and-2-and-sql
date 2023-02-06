import pandas as pd

teachers = [
    {"name": "Pep Guardiola", "age": 27, "height": "2.1m", "school": "Manchester High School", "married": True},
    {"name": "Jurgen Klopp", "age": 31, "height": "2.1m", "school": "Liverpool High School", "married": True},
    {"name": "Mikel Arteta", "age": 21, "height": "2.1m", "school": "Arsenal High", "married": False}
]

students = [
    {"teacher": "Pep Guardiola", "name": "Jack Grealish"},
    {"teacher": "Jurgen Klopp", "name": "Roberto Firmino"},
    {"teacher": "Jurgen Klopp", "name": "Andrew Robertson"},
    {"teacher": "Jurgen Klopp", "name": "Darwin Nunez"},
    {"teacher": "Pep Guardiola", "name": "Ederson Moraes"},
    {"teacher": "Pep Guardiola", "name": "Manuel Akanji"},
    {"teacher": "Mikel Arteta", "name": "Bukayo Saka"},
    {"teacher": "Mikel Arteta", "name": "Gabriel Martinelli"},
    {"teacher": "Mikel Arteta", "name": "Thomas Partey"}
]

df_teacher = pd.DataFrame(teachers)
df_student = pd.DataFrame(students)

import pandas as pd
import numpy as np

df_teacher = pd.DataFrame({
    "name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"], 
    "married": [True, True, False, True], 
    "school": ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan]
})

df_student = pd.DataFrame({
    "teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola", "Pep Guardiola", "Mikel Arteta"], 
    "name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino", "Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"], 
    "age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
    "height": ["2.1m", "2.1m", "2.1m", "2.1m", "2.1m", "2.1m", "2.1m", "2.1m", "2.1m"]
})

[
{
"teacher": "Pep Guardiola",
"students": [
{
"name": "Jack Grealish",
"age": 27,
"height": '2.1m',
"weight": '80kg'
},
{
"name": "Ederson Moraes",
"age": 29,
"height": '2.1m',
"weight": '80kg'
},
{
"name": "Manuel Akanji",
"age": 27,
"height": '2.1m',
"weight": '88kg'
}
]
},
{
"teacher": "Jurgen Klopp",
"students": [
{
"name": "Roberto Firmino",
"age": 31,
"height": '2.1m',
"weight": '73kg'
},
{
"name": "Andrew Robertson",
"age": 28,
"height": '2.1m',
"weight": '60kg'
},
{
"name": "Darwin Nunez",
"age": 23,
"height": '2.1m',
"weight": '70kg'
}
]
},
{
"teacher": "Mikel Arteta",
"students": [
{
"name": "Bukayo Saka",
"age": 21,
"height": '2.1m',
"weight": '80kg'
},
{
"name": "Gabriel Martinelli",
"age": 21,
"height": '2.1m',
"weight": '70kg'
},
{
"name": "Thomas Partey",
"age": 29,
"height": '2.1m',
"weight": '74kg'
}
]
}
]