# Syllabus Schedule
A simple Python module to create schedules, mostly for the use in a Syllabus. 

## Background
If you teach classes, you know that creating the schedule every semester can be painful since you have to account for breaks and other things. This module hopes to solve that. 

## Usage
Grab a copy of the repository:
```
cd ~/
git clone https://github.com/brad-anton/SyllabusSchedule.git
```

Create a virtual environment for your project (slight overkill):
```
cd project_folder
virtualenv venv
source venv/bin/activate
pip install -r ~/SyllabusSchedule/requirements.txt
cp ~/SyllabusSchedule/SyllabusSchedule.py .
```


Then you'll just need to include some imports:
```python
from datetime import date,timedelta
from SyllabusSchedule import SyllabusSchedule
```

And then create a schedule:
```python
start = date(2016,1,31)
end = date(2016,5,9)

breaks = [ date(2016,2,15) ]# President's Day, no class

spring_break_start = date(2016,3,14) # Spring Break Week

for i in range(6):
    breaks.append(spring_break_start + timedelta(days=i))

schedule = SyllabusSchedule(start, end, breaks)

schedule.push("Intro to CS6573!")
schedule.add_lab("Hax", 7)

print "Text Schedule output:\n"
schedule.get_txt()

print "HTML Schedule outout:\n"
schedule.get_html()

```


