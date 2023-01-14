"""
    Name: Ankan Bhattacharya
    Roll Number: 22001003505
    
    Question: Program to find fuzzy set corresponding to age
"""
age=int(input('your age: \n'))
if (age > 0 and age <=18):
    print('fuzzy set=child')
    if (age <=8):
        mc=1
    else:
        mc=((18-age)/10)
    print('membership='+str(mc))
    
if (age >= 8 and age <=45):
    print('fuzzy set=young')
    if (age <=18):
        my=((age-8)/10)
    else:
        if(age <=30):
            my=1
        else:
            my=((45-age))/15
    print('membership='+str(my))
    
if (age >= 30 and age <=60):
    print('fuzzy set=middle age')
    if (age <=45):
        mm=((age-30)/15)
    else:
        if(age <=55):
            mm=1
        else:
            mm=((60-age))/5
    print('membership='+str(mm))
    
if (age >= 55 and age <=75):
    print('fuzzy set=old')
    if (age <=60):
        mo=((age-55)/5)
    else:
        if(age <=70):
            mo=1
        else:
            mo=((75-age))/5
    print('membership='+str(mo))
    
if (age >= 70):
    print('fuzzy set=very old')
    if (age <=80):
        mvo=((age-70)/10)
    else:
        mo=1
    print('membership='+str(mo))
    
            