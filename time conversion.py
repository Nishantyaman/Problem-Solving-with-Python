

time = input().strip()
h, m, s = map(int, time[:-2].split(':'))
p = time[-2:]
h = h % 12 + (p.upper() == 'PM') * 12
print(('%02d:%02d:%02d') % (h, m, s))

# ##########################################
from datetime import datetime
t = input()

dt=datetime.strptime(t, '%I:%M:%S%p')
print(dt.strftime('%H:%M:%S'))