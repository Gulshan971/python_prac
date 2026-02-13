datesheet = [
       {"date": "10/02/2026", "subject" :"software engineering" , "invigilator" : "vp"},
       {"date":"10/02/2026" , "subject": "industrial management" , "invigilator" : None},
       {"date":"11/02/2026" , "subject" : "oots" , "invigilator" : "pb"},
       {"date": "11/02/2026" , "subject" : "e commerce" , "invigilator":"urvashi"},
       {"date" : "12/02/2026" , "subject" : "cn" , "invigilator" : "vs"},
       {"date":"12/02/2026" , "subject" : "cd" , "invigilator" : "skt"}
]
print(datesheet , sep=":")

# for i in datesheet:
#     for exam in datesheet[i]:
#         print(exam , datesheet[exam] , sep=" , ")


for exam in datesheet:
    print( exam["date"] , exam["subject"] , exam["invigilator"] , sep="| " )