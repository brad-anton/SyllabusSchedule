'''
SyllabusSchedule
@brad_anton

A simple Python module to create schedules. Provide content 
and dates, and it will return the date
'''

from datetime import date, timedelta
from collections import deque
from tabulate import tabulate

class SyllabusSchedule:
    """
    Creates a Syllabus Schedule

    Keyword Arguments: 
    start -- DateTime object for the start date of the semester
    end -- DateTime object for the end date of the semester
    breaks -- A list of DateTime objects where each element is a day in which there is no class
    day -- Day of the week class is held (0=Monday, 1=Tuesday, 2=Wednesday...)
    """
    def __init__(self, start, end, breaks, day=2):
        self.start = start
        self.end = end
        self.day = day
        self.__schedule = []
        self.__final_schedule = []
        self.__breaks = breaks 

    def __build_schedule(self):
        """Populates the weeks within self.__final_schedule starting at 
        self.start and ending at self.end. Should be called before any
        get_* methods
        """
        self.__final_schedule = []
        week_num = 1 
        week_start = self.start

        if week_start.weekday() is not 0:
            week_start = self.start + timedelta(days=0-self.start.weekday())

        task_queue = deque(self.__schedule)

        while week_start < self.end:
            week_end = week_start + timedelta(days=4)
                
            breaks = []
            for br in self.__breaks:
                if week_start <= br <= week_end:
                    breaks.append(br)

            if len(breaks) >= 5:
                self.__final_schedule.append({ 'Week' : week_num,
                    'Dates': '{0:%m/%d} - {1:%m/%d}'.format(week_start, week_end),
                    'Topic': 'No Class!'})
                week_start += timedelta(weeks=1)
                week_num +=1
                continue

            try:
                task = task_queue.popleft()

                self.__final_schedule.append({ 'Week' : week_num,
                    'Dates': '{0:%m/%d} - {1:%m/%d}'.format(week_start, week_end),
                    'Topic': task['Topic']})

                # Labs are displayed as its own row for the available week
                lab_num = 1
                for lab in task['Labs']:
                    due_date = week_start + timedelta(days=(self.day + lab['Days'] ))

                    # Extend the due_date to account for breaks between
                    # self.day of current week and due_date
                    # TODO:account for breaks in the next week
                    for br in breaks:
                        if br > (week_start + timedelta(days=self.day)):
                            due_date = due_date + timedelta(days=1)

                    # Disallow due_dates on breaks
                    for br in self.__breaks:
                        if due_date == br:
                            due_date = due_date + timedelta(days=1)

                    # Disallow due_dates on weekends
                    if due_date.weekday() >= 5: 
                        due_date = due_date + timedelta(days=7-due_date.weekday())

                    # Disallow due_dates after the last day of class
                    if due_date > self.end:
                        due_date = self.end

                    self.__final_schedule.append({ 'Week' : week_num,
                        'Dates': '{0:%m/%d} - {1:%m/%d}'.format(week_start, week_end),
                        'Topic': 'Lab {0}: {1} - Due: {2:%m/%d}'.format(lab_num, lab['Title'], due_date)
                        })
                    lab_num+=1

            except IndexError: # Add in blank week if there are not enough topics
                self.__final_schedule.append({ 'Week' : week_num,
                    'Dates': '{0:%m/%d} - {1:%m/%d}'.format(week_start, week_end),
                    'Topic': ''})
           
            # Breaks are displayed on their own row for the week.
            for day in breaks:
                self.__final_schedule.append({ 'Week' : week_num,
                    'Dates': '{0:%m/%d} - {1:%m/%d}'.format(week_start, week_end),
                    'Topic': 'No Class: {:%m/%d}'.format(day)
                    })
            week_start += timedelta(weeks=1)
            week_num+=1

        # Last Day of Class is own row. 
        self.__final_schedule.append({ 'Week': week_num,
            'Dates': '{0:%m/%d}'.format(self.end),
            'Topic': 'Last day of Class!' 
            })

        if len(task_queue) > 0:
            print "\n[!] Warning: Not enough weeks in the semester to accomodate these tasks:"
            for task in task_queue:
                print "\t{0}".format(task['Topic'])
                for lab in task['Labs']:
                    print "\t\t{0}".format(lab['Title'])
    
    def push(self, title):
        """Add a weekly topic to the schedule
        """
        self.__schedule.append({ 'Topic': title, 'Labs': [] })

    def pop(self):
        """Removes the last item added to the Schedule and returns is
        """
        return self.__schedule.pop()

    def add_lab(self, title, days):
        """Add a Lab to the current week that is due after the number of days
        """
        self.__schedule[len(self.__schedule)-1]['Labs'].append({'Title': title, 'Days': days })

    def get_html(self):
        """Return an HTML table of the Schedule
        """
        self.__build_schedule()
        print tabulate(self.__final_schedule, headers="keys", tablefmt="html")

    def get_txt(self):
        """Return an txt table of the Schedule
        """
        self.__build_schedule()
        print tabulate(self.__final_schedule, headers="keys")

    def get_pdf(self, block):
        """TODO: Create a PDF that includes a block of text and the schedule
        """
        self.__build_schedule()
        print "Sorry! This feature is not yet implemented!"

if __name__ == '__main__':
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

    print "PDF Schedule output:\n"
    schedule.get_pdf("")


