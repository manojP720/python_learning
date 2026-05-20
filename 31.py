def insert_element(lst):
    pos = int(input("enter position to insert:"))
    val = int(input("enter value to insert :"))
    lst.insert(pos,val)
    print("updated list :",lst)

def remove_element(lst):
    val = int(input("enter value to remove :")) 
    if val in lst :
        lst.remove(val)
        print("updated list:",lst) 
    else:
        print("element not found!")

          