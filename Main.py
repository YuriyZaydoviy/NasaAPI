from GetData import *
from FormMessage import *
from Telegram import *
from Settings import *


all_data_arr = get_array()
record,name,id,count = form(all_data_arr)
string = message(record,name,id,count)
main_tele(string)


    