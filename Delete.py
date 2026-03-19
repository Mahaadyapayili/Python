Student_Data={"ID1":{"Name":"sara","Class":"v","Subject_Integration":"English,Science,math"},
              "ID2":{"Name":"David","Class":"v","Subject_Integration":"English,Science,math"},
              "ID3":{"Name":"sara","Class":"v","Subject_Integration":"English,Science,math"},
              "ID4":{"Name":"vicky","Class":"v","Subject_Integration":"English,Science,math"},}
result={}
seen_keys=[]
for student_id,details in Student_Data.items():
    unique_key=(details["Name"],details["Class"],details["Subject_Integration"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id]=details
for k,v in result.items():
    print(k,":",v)