import os
from datetime import datetime
for i in os.walk('.'):
    print(i)

print(os.path.join('pythonUrbanUniversity', 'Module 7', 'homework7-5.py'))

change_time = os.path.getmtime('homework7-5.py')

print(datetime.fromtimestamp(change_time))

print(os.path.getsize('homework7-5.py'))

print(os.path.dirname(r'C:\Users\Роман\PycharmProjects\pythonUrbanUniversity'))