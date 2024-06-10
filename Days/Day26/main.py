# list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# sq_list = [num * num for num in list]
# print(sq_list)
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [num for num in numbers if num % 2 == 0]
# print(result)
# #
# import random
#
# names = ["Hirak", "Pranjal", "Mittal", "Amish"]
# students_score = {student:random.randint(1, 100) for student in names }
# print(students_score)
#
# scored = {student:score for (student, score) in students_score.items() if score > 10}
# print(scored)
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# res = {word:len(word) for word in sentence.split()}
# print(res)
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
#
# weather_f = {day:(temp * 9/5)+32 for (day, temp) in weather_c.items()}
# print(weather_c)
# print(weather_f)

student_dict = {
    "student": ["Hirak", "Pranjal", "Mittal", "Amish"],
    "score": [56, 65, 67, 76]
}
#
# for (key, value) in student_dict.items():
#     print(value)

# import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
# # print(student_data_frame)
#
# # # iter rows: loop through each of the row
# for (index, row) in student_data_frame.iterrows():
#     if row.score > 60:
#         print(row)


import pandas

letter_list = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_dict = {row.letter: row.code for (index, row) in letter_list.iterrows()}

while(True):
    name = input("Enter a name: ")
    try:
        pronounce = [letter_dict[char.upper()] for char in name]
    except KeyError:
        print("Enter values in the alphabets only and not even numbers")
    else:
        print(pronounce)
