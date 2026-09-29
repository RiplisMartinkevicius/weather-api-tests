import os
from datetime import date
    
today = str(date.today())

for filename in os.listdir("."):
    new_name = f"{today}_{filename}"
    os.rename(filename, new_name)
    print(new_name)