# ------- set คือ ข้อมูลหลายข้อมูล คนละชนิด ซํ้ากันไม่ได้ (ถ้าซํ้ากันถือว่าเป็นตัวเดียวกัน) เเละไม่มีลำดับ เเละเเก้ไขไม่ได้ เเต่เพิ่มลบได้ ------------
setgu1 = {10,20,True,10,"SAU",(20,"Iot")}

#เข้าถึงทุกข้อมูลใน set
for deta in setgu1 :
    print(deta)

# เเก้ไขข้อมูลใน set ทำไม่ได้โดยตรง เเต่ทำได้โดยอ้อมเหมือนกับ Tuple
listgu1 = list(setgu1)
print(listgu1)
listgu1[2] = "TEE"
print(listgu1)
setgu1 = set(listgu1)
print(setgu1)

# Set Method
setgu1.add(999) # add ข้อมูลเข้าไปได้
setgu1.add("WOWW")
print(setgu1)
setgu1.pop() # เอาข้อมูลออก เเบบสุ่ม
print(setgu1)
setgu2 = setgu1.copy() # copy เซ็ตไปอีกเซ็ตนึง
print(setgu2)
setgu1.remove(999) #เอาข้อมูลใน set ออก
print(setgu1)

# Set function
# len() เอาไวนับจำนวนข้อมูล
print(len(setgu1)) 
# min() , max() ต้องเป็น str ทั้งหมดหรือเป็น int ทั้งหมด
setgu3 = (10,20,30,40,50)
print(min(setgu3))
print(max(setgu3))