import re
import urllib
url = "http://www.espncricinfo.com/ci/engine/match/index.html?date="
date = raw_input("What is the date(yyyy-mm-dd) of the match?")
url1 = url + date
data = urllib.urlopen(url1).read()
#print data
#team = raw_input("Give name of first team involved in the match:")
###FIRST INNINGS
m = re.search('<div class="innings-info-1">',data)
start = m.start()
end = start + 300
#print data[start:end]
x=data[start:end]
#print x
firstInnings = re.search('<div class="innings-info-1">',x)
firstInnings_start=firstInnings.end()
firstInnings_end=firstInnings_start + 60
#print x[firstInnings_start:firstInnings_end]
firstInnings_final= x[firstInnings_start:firstInnings_end]
p=re.search('<span class="bold"',firstInnings_final)
team_first = firstInnings_final[0:p.start()]
#print team_first
#print firstInnings_final
q = re.search('<span class="bold">',firstInnings_final)
score_first_start = q.end()
q = re.search('</span>',firstInnings_final)
score_first_end = q.start()
score_final = firstInnings_final[score_first_start:score_first_end]
print team_first+":"+score_final
###SECOND INNINGS
m = re.search('<div class="innings-info-2">',data)
start = m.start()
end = start + 300
#print data[start:end]
x=data[start:end]
#print x
secondInnings = re.search('<div class="innings-info-2">',x)
secondInnings_start=secondInnings.end()
secondInnings_end=secondInnings_start + 80
#print x[firstInnings_start:firstInnings_end]
secondInnings_final=x[secondInnings_start:secondInnings_end]
p=re.search('<span class="bold"',secondInnings_final)
team_second = secondInnings_final[0:p.start()]
#print team_first
#print firstInnings_final
q = re.search('<span class="bold">',secondInnings_final)
score_second_start = q.end()
q = re.search('</span>',secondInnings_final)
score_second_end = q.start()
score_final = secondInnings_final[score_second_start:score_second_end]
print team_second+":"+score_final
#RESULT
m = re.search('<div class="match-status">',data)
start = m.start()
end = start + 200
#print data[start:end]
x= data[start:end]
a = re.search('<span class="bold">',x)
status_start = a.end()
a = re.search('</span>',x)
status_end = a.start()
status_final = x[status_start:status_end]
print ("\nThe current status of the match is:" + status_final + "\n")  






