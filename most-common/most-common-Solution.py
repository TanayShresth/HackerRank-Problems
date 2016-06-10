# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
inp_string = raw_input() #input string
reverse_sorted_od = OrderedDict()
new_od = OrderedDict()
last_od = OrderedDict()
somelist = list()
if 3 < len(inp_string) and len(inp_string) <= 10000 : #checking length of inp string    
    letter_dict = dict()
    for item in inp_string :
        letter_dict[item] = letter_dict.get(item , 0) + 1 #dict contains all letters and their count
    for k in sorted(letter_dict , key = letter_dict.get , reverse = True) :
        reverse_sorted_od[k] = letter_dict[k] #lh dict contains all letters and count in desc order as per the count
    somelist = reverse_sorted_od.values() #list has all values in reverse order
    somelist.sort(reverse = True) # seems redunant
    largest_value = somelist[0] #largest count
    for k,v in reverse_sorted_od.items() : 
        current_value = v       
        if current_value == largest_value : #adds 
            new_od[k] = current_value
        else :            
            sorted_list = sorted(new_od.items())
            for m,n in sorted_list :                
                last_od[m] = n
            del sorted_list[:]
            new_od.clear()
            largest_value = current_value #adds 
            new_od[k] = current_value
    if new_od :
        sorted_list = sorted(new_od.items())
        for m,n in sorted_list :
            last_od[m] = n 
    count = 0
    for a in last_od :
        if count < 3 :
            count = count + 1
            print a , last_od[a]
        else :
            break
