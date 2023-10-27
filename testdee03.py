# OOP or Object / Instance
#ชื่อ class ควรขึ้นต้นด้วยตัวใหญ่
class BARAMEE :
    #data / property/field/attribute คุณสมบัติ
    major = "SAU"
    name = ""

    #method การทำงาน (คือ function เเต่ไม่เรียก function)
    def showHi(self):
        print("Hi.....")
    
    def introduceMySelf(self):
        print(f"My name is {self.name}")
        print(f"My major is {self.major}")

# -----------------------
# สร้าง object
odA = BARAMEE() # เป็นการเรียกใช้ constructor ของคลาสให้ทำงาน (ถ้ามี)
odB = BARAMEE()


# การใช้งาน data ของ object คือ เอาค่ามันมาใช้ หรือเปลี่ยนค่าให้มันใหม่
print(odA.major)
odA.major = "Meow"
odA.name = "อิคึ๊"
odB.name = "อิไต๋"

# การใช้งาน data ของ object คือ สั่งให้เมธอดของ object นั้นๆ ทำงาน
odA.introduceMySelf()
odB.introduceMySelf()