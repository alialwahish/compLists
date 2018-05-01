list_one = [1,2,5,6,5]
list_two = [1,2,5,1,5,2]
stat = True
if len(list_one)==len(list_two):
    j=0
    for i in list_one:
        if i != list_two[j]:
           stat=False
        j+=1
        

else:            
    stat= False

if stat == True:
    print("lists are the same")
else:
    print("lists are not the same")