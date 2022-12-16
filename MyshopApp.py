import select_manager
import insert_manager
print('============================')
print('======กรุณาเลือกรายการ========')
print('============================')
print('1.เพิ่มรายการสินค้า\n2.เรียกดูรายการสินค้า')
print('============================')
user_select = int(input(''))
if user_select == 1:
    print('============================')
    pro_name = input('กรุณาระบุชื่อสินค้า: ')
    pro_price = int(input('กรุณาระบุราคาสินค้า: '))
    print('============================')
    insert_manager.insert_product(pro_name, pro_price)
    
    
elif user_select == 2:
    print('============================')
    pro_id = int(input('กรุณาระบุรหัสสินค้า: '))
    print('============================')
    select_manager.select_product(pro_id)
    
    
else:
    print('============================')
    print('คุณใส่ตัวเลือกไม่ถูกต้อง!!!')
print('============================')