import re

def is_date_format_correct(date:str)-> bool:
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    match = re.search(pattern, date)
    return print ("True") if match else print('False')
   
is_date_format_correct('2022/01/01') #False
is_date_format_correct('1999-01-01')#True
is_date_format_correct('20221129') #false    
