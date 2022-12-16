import mysql.connector

class select_product:
    pro_id = 0
    
    def __init__(self,pro_id) -> None:
        self.pro_id = pro_id
        
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="myshop"
        )
        
        #check pro_id ต้องไม่มากกว่า product_id หรือเป็น 0
        mycursor = conn.cursor()
        check = "SELECT MAX(product_id) FROM tb_product"
        mycursor.execute(check)
        #convers List to int
        mycheck = mycursor.fetchall()#[(number,)]
        mycheck2 = mycheck[0]#(number,)
        mycheck3 = mycheck2[0]#number
        # print(mycheck)
        # print(mycheck2)
        # print(mycheck3)
        if pro_id > mycheck3:
            print('รหัสสินค้าไม่ถูกต้อง')
        elif pro_id == 0:
            print('รหัสสินค้าไม่ถูกต้อง')
        
        sql = "SELECT * FROM tb_product WHERE product_id =" + str(pro_id)
        
        mycursor.execute(sql)
        
        myresult = mycursor.fetchall()
        for row in myresult:
            
            print("รหัสสินค้า: ",row[0],"\n","ชื่อสินค้า: ",row[1]+"\n","ราคา: ",row[2])
        
        conn.close()