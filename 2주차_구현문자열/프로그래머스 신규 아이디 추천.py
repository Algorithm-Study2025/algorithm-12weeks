import re

def solution(new_id):
    s = new_id.lower()                         
    s = re.sub(r"[^a-z0-9\-_.]", "", s)         
    s = re.sub(r"\.+", ".", s)                  
    s = s.strip(".")                            

    if not s:                                  
        s = "a"

    if len(s) >= 16:                           
        s = s[:15]
        s = s.strip(".")                        

    while len(s) < 3:                          
        s += s[-1]

    return s
