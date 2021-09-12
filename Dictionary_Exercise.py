room_num = {"CS101": 3004, "CS102": 4501,
            "CS103": 6755, "NT110": 1244, "CM241": 1411}

instructor = {'CS101': 'Haynes', 'CS102': 'Alvarado',
              'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}

meeting_time = {'CS101': '8:00 am', 'CS102': '9:00 am',
                'CS103': '10:00 am', 'NT110': '11:00 am', 'CM241': '1:00 pm'}

course = input("What is your Course Number? ")

print(room_num[course])
print(instructor[course])
print(meeting_time[course])
