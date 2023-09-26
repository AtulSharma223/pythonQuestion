def candidateName(s):
    name=s.split('0')
    print(name)
    while(len(name)>3):
        for i in name:
            if(len(i)==0):
                name.remove(i)
    print(name)
    dict={
        "first_name":name[0],
        "last_name":name[1],
        "id":name[2],
    }
    return dict
information=candidateName("John000Deo000123")
print(information)



        