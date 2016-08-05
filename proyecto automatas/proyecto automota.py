#leonardo ismael valle jimenez
#manuel ortiz fortiz
#miguel rodriguez

edges={                 
       (1,'a'):2,
       (2,'a'):2,
       (2,'b'):3,
       (3,'b'):3,
       (3,'a'):4,
       (4,'c'):5}
aceptacion=[5]  

def fsmsim(string, current, edges, aceptacion)
    if string == "":
        return current in aceptacion 
    else:
        letter= string[0]
        if(current,letter)in edges:
            destination=edges[(current,letter)] 
            remaining_string=string[1:]
            return fsmsim(remaining_string,destination,edges,aceptacion)
        else:
            return False 

print(fsmsim("aaabbbac",1,edges,aceptacion))

def fsmsim(string, current, edges, aceptacion):
    if string == "a":
        return current in aceptacion 
    else:
        letter= string[0] 
        if(current,letter)in edges: 
            destination=edges[(current,letter)]
            remaining_string=string[1:]
            return fsmsim(remaining_string,destination,edges,aceptacion)
        else:
            return False 
        
print(fsmsim("aaabbbac",1,edges,aceptacion))

def fsmsim(string, current, edges, aceptacion):
    if string == "b":
        return current in aceptacion 
    else:
        letter= string[0] 
        if(current,letter)in edges:
            destination=edges[(current,letter)]
            remaining_string=string[1:
            return fsmsim(remaining_string,destination,edges,aceptacion)
        else:
            return False 

print(fsmsim("aaabbbac",1,edges,aceptacion))

def fsmsim(string, current, edges, aceptacion):
    if string == "ab":
        return current in aceptacion 
    else:
        letter= string[0]
        if(current,letter)in edges: 
            destination=edges[(current,letter)]
            remaining_string=string[1:]
            return fsmsim(remaining_string,destination,edges,aceptacion)
        else:
            return False 

print(fsmsim("aaabbbac",1,edges,aceptacion))

def fsmsim(string, current, edges, aceptacion):
    if string == "aba":
        return current in aceptacion 
    else:
        letter= string[0] 
        if(current,letter)in edges: 
            destination=edges[(current,letter)]
            remaining_string=string[1:]
            return fsmsim(remaining_string,destination,edges,aceptacion)
        else:
            return False 

print(fsmsim("aaabbbac",1,edges,aceptacion))

def fsmsim(string, current, edges, aceptacion):
    if string == "aabbaa":
        return current in aceptacion 
    else:
        letter= string[0] 
        if(current,letter)in edges: 
            destination=edges[(current,letter)]
            remaining_string=string[1:]
            return fsmsim(remaining_string,destination,edges,aceptacion)
        else:
            return False 

print(fsmsim("aaabbbac",1,edges,aceptacion))

def fsmsim(string, current, edges, aceptacion):
    if string == "aaabbbaab":
        return current in aceptacion 
    else:
        letter= string[0] 
        if(current,letter)in edges: 
            destination=edges[(current,letter)]
            remaining_string=string[1:]
            return fsmsim(remaining_string,destination,edges,aceptacion)
        else:
            return False 

print(fsmsim("aaabbbac",1,edges,aceptacion))
