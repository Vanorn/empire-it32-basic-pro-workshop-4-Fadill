gang_members = []

def add_members(name, age, gang):
    new_guy = {"name": name,
               "age": age,
                "gang": gang}
    gang_members.append(new_guy)

while True:
    choice = input("1:new members,2:member list,3:about our boss")
    if choice == "1":
        name = str(input("ชื่อสมาชิก:"))
        age = int(input("กี่ขวบจั๊ฟ"))
        gang = str(input("มาเข้าแกงค์อะไรหนิ:"))

        add_members(name, age, gang)
        print("เสร็จแล้วมึงไปได้ละ")

    elif choice == "2":
        print(gang_members)
    else:
        print("จะมาดูอะไรในนี้ไม่มีหรอกไอ้ฟายเอ้ยยยยยยยยยยยยยยยยยยยยยยยยยยยย")
        break