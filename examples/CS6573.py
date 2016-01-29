from datetime import date,timedelta
from SyllabusSchedule import SyllabusSchedule

start = date(2016,1,31)
end = date(2016,5,9)
breaks = [ date(2016,2,15) ]# President's Day, no class
spring_break_start = date(2016,3,14) # Spring Break Week
for i in range(6):
    breaks.append(spring_break_start + timedelta(days=i))

schedule = SyllabusSchedule(start, end, breaks)

# Week 1
schedule.push("Intro to CS6573 and The Basics")
schedule.add_lab("Simple x86 assembly", 7)

# Week 2
schedule.push("WinDBG and IDA Pro")
schedule.add_lab("FSExploitMe: WinDBG Hoops", 7)

# Week 3
schedule.push("The Stack and Heap")
schedule.add_lab("Stack and Heap", 7)

# Week 4
schedule.push("Memory Corruption")
schedule.add_lab("Bad Code", 7)

# Week 5
schedule.push("Triaging Vulnerabilities")
schedule.add_lab("Triage", 7)

# Week 6
schedule.push("Stack Exploitation")
schedule.add_lab("Stack Exploitation", 7)

# Week 7
schedule.push("Use-After-Free Exploitation")
schedule.add_lab("Use-After-Free Exploitation", 7)

# Week 8
schedule.push("Exploit Mitigations")
schedule.add_lab("Exploit Mitigations", 14)

# Week 9
schedule.push("Case-Study: Analysis and Triage")
schedule.add_lab("Case-Study Triage", 7)

# Week 10
schedule.push("Case-Study: Replacing the Freed Object")
schedule.add_lab("Case-Study Replacing the Freed Object", 7)

# Week 11
schedule.push("Case-Study: Exploitation")
schedule.add_lab("Case-Study Exploitation", 14)

schedule.push("Open Lab")

# Week 12
schedule.push("Case-Study: Bypassing Mitigations")
schedule.add_lab("Case-Study Bypassing Mitigations", 14)

# Week 13
schedule.push("Exploit Kits")

print "Text Schedule output:\n"
schedule.get_txt()

print "HTML Schedule outout:\n"
schedule.get_html()

