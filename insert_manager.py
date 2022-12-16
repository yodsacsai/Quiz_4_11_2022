import mysql.connector

class insert_product:
    pro_name = ''
    pro_price = 0
    
    def __init__(self, pro_name, pro_price) -> None:
        self.pro_name = pro_name
        self.pro_price = pro_price
        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="myshop"
        )
        
        mycursor = conn.cursor()
        
        sql = "INSERT INTO tb_product (product_name, product_price) VALUES (%s, %s)"
        val = (pro_name, pro_price)
        mycursor.execute(sql, val)
        
        conn.commit()
        
        print('บันทึกข้อมูลสินค้าเรียบร้อยแล้ว')
        
        conn.close()