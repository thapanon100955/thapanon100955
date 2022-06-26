CP = []
Name = input('ป้อนชื่อ : ')
while True :
    print('ตอนนี้คุณมี'+ Name,':',CP)
    print ('เพิ่ม add\tแทรก in\tลบล่าสุด pop\tลบทั้งหมด del\tลบจุดนึง rem\tดูว่ามีกี่ตัว len')
    i = str(input(''))
    if i == 'add' :
        add = input('ใส่ตัวอักษร : ')
        CP.append(add)
    elif i == 'in' :
        ins = input('ใส่ตัวอักษร : ')
        print(CP)
        ins2 = int(input('ใส่ตัวเลขทีจะแทรก : '))
        ins2 -= 1
        CP.insert(ins2,ins)
    elif i == 'pop' :
        CP.pop()
        print('ลบแล้ว')
    elif i == 'del' :
        CP.clear()
        ('ลบแล้ว')
    elif i == 'rem' :
        print(CP)
        rem = int(input('ป้อนตัวเลขที่ต้องการลบ : '))
        rem -= 1
        CP.pop(rem)
    elif i == 'len' :
        print('ทั้งหมด ',len(CP))
    else :
        print('ระบบผิดพลาด')
