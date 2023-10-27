# ------- Dictionary คือ ข้อมูลหลายข้อมูลที่เป็น key:value แก้ไขได้ ไม่มี index กำกับ ไม่มีลำดับ ซ้ำได้
# key เป็น String/Integer ส่วน value เป็นอะไรก็ได้ (number,string,boolean,list,tuple,set,dictionary) ------------
dicgu1 = {'name':'mod', 'age':30, 555:999, 'flag':True, 'wow':[10,20,30]}
dicgu2 = {  "data1":[10,20,30],
            "data2":(2,5,6),
            "data3":(45,3,4),
            "data4":{ "x":111,
                        "Y":222
            }
         }

# การเข้าถึงข้อมูลใดข้อมูลหนึ่ง
print(dicgu1["name"])
print(dicgu1[555])
dicgu1['age'] = 50
print(dicgu1)

# อยากเเสดงผล 20 ออกมาทำไง
print(dicgu1['wow'][1])
# อยากเเสดงผล 222 ออกมาทำไง
print(dicgu2['data4']["Y"])
dicgu2["data5"] = 888
print(dicgu2)
# การเข้าถึงทุกข้อมูล
for xx in dicgu1 :
    print(xx)

print("-----------------------")

for xx in dicgu1.values() :
    print(xx)

print("-----------------------")

for xx in dicgu1.keys() :
    print(xx)

print("-----------------------")

for xx,yy in dicgu1.items():
    print(xx,"-",yy)

#dictionary method
dicgu1.popitem() #เอาข้อมูลชุดสุดท้ายออก
dicgu1.popitem()
dicgu1.popitem()
print(dicgu1)

dicgu2.pop("data3") #เอาข้อมูลตัวสุดท้ายออก
print(dicgu2)

print("------------------------")
print(dicgu2["data2"])
print(dicgu2.get("data2"))