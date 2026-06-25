from datetime import datetime,timedelta
current=datetime.now().date()
future=current+timedelta(days=15)
print(future)