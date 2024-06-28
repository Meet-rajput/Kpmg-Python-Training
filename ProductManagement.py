import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",passwd="rps@123",database="kpmg")
cursor = con.cursor()

def addProduct() :
    prodName = input("Enter Product Name :")
    prodPrice = input("Enter Product price :")
    prodCategory = input("Enter Product Category :")
    prodDescription = input("Enter Product Description :")

    try :
        "{:.2f}".format(float(prodPrice)) 
    except :
        print("Invalid Price ")
        return
    
    queryId ="select max(product_id) from product"
    cursor.execute(queryId)
    result = cursor.fetchall()
    
    for row in result:
        if row[0]==None:
            prodId=1
        else :
            prevProdId = row[0]
            prodId = prevProdId + 1
    
    insertQuery = ('insert into product (product_id,product_name,product_price,product_category,description) values(%s, %s, %s,%s,%s)')  
    cursor.execute(insertQuery, [prodId, prodName, prodPrice, prodCategory, prodDescription])
    con.commit()
    print("\nProduct added successfully.")    


def updateProduct():
    prodId = input("Enter product Id to update the same :")
    if  not(prodId.isdigit()):
        print("Invalid Id")
        return
    queryId ="select * from product where product_id=%s"
    cursor.execute(queryId,[prodId])
    result = cursor.fetchall()

    for row in result:
        if row[0]==None:
            print("No such product Id present")
            return
    
    prodName = input("Enter Product Name :")
    prodPrice = input("Enter Product price :")
    prodCategory = input("Enter Product Category :")
    prodDescription = input("Enter Product Description :")

    updateQuery = ('update product set product_name=%s, product_price=%s, product_category=%s,description=%s where product_id=%s')  
    cursor.execute(updateQuery, [prodName, prodPrice, prodCategory, prodDescription,prodId])
    con.commit()
    print("\nProduct updated successfully.")   

def deleteProduct():
    prodId = input("Enter product Id to delete the same :")
    if  not(prodId.isdigit()):
        print("Invalid Id")
        return
    if  not(prodId.isdigit()):
        print("Invalid Id")
        return
    queryId ="select * from product where product_id=%s"
    cursor.execute(queryId,[prodId])
    result = cursor.fetchall()

    for row in result:
        if row[0]==None:
            print("No such product Id present")
            return

    delQuery ="delete from product where product_id=%s"
    cursor.execute(delQuery,[prodId])
    con.commit()

def getProductByID():
    prodId = input("Enter product Id to get product details :")
    if  not(prodId.isdigit()):
        print("Invalid Id")
        return
    queryId ="select * from product where product_id=%s"
    cursor.execute(queryId,[prodId])
    result = cursor.fetchall()

    for row in result:
        if row[0]==None:
            print("No such product Id present")
            return
        
        print (f''' Result
               Id:{row[0]} , name:{row[1]}, price:{row[2]} , category:{row[3]}, description:{row[4]} ''')

def getAllProducts():
    
    queryId ="select * from product"
    cursor.execute(queryId,)
    result = cursor.fetchall()
    print("Result :")
    for row in result:
        if row[0]==None:
            print("No such product Id present")
            return
        
        print (f'''Id:{row[0]} , name:{row[1]}, price:{row[1]} , category:{row[1]}, description:{row[1]} ''')


def getAllProductsByCategory():
    prodCategory = input("Enter product category to get product category based :")
    queryId ="select * from product where product_category=%s"
    cursor.execute(queryId,[prodCategory])
    result = cursor.fetchall()
    print("Result :")
    for row in result:
        if row[0]==None:
            print("No product available under this category.")
            return
        
        print (f'''Id:{row[0]} , name:{row[1]}, price:{row[2]} , category:{row[3]}, description:{row[4]} ''')


def getAllProductsBetweenPrices():
    priceFrom = input("Enter price range From :")
    priceTo = input("Enter price range To :")
    queryRange ="select * from product where product_price between %s and %s"
    cursor.execute(queryRange,[priceFrom,priceTo])
    result = cursor.fetchall()
    print("Result Price range from {priceFrom} to {priceTo} : ")
    for row in result:
        if row[0]==None:
            print("No such product Id present")
            return
        
        print (f'''Id:{row[0]} , name:{row[1]}, price:{row[2]} , category:{row[3]}, description:{row[4]} ''')


i=0
while i!=8 :
    print('''
          1. Press 1 to Add Product 
          2. Press 2 to Update Product 
          3. Press 3 to Delete Product 
          4. Press 4 to Get Product By Id 
          5. Press 5 to list all Products 
          6. Press 6 to get Products by Category 
          7. Press 7. to get Product between price range 
          8. to EXIT ''')
    choice=input("Select an option now :")
    if (choice.isdigit() and (int(choice)>0 and int(choice)<=8)):
        i=int(choice)
        if i==1:
            addProduct()
        elif i==2:
            updateProduct()
        elif i==3:
            deleteProduct()
        elif i==4:
            getProductByID()
        elif i==5:
            getAllProducts()
        elif i==6:
            getAllProductsByCategory()
        elif i==7:
            getAllProductsBetweenPrices()
        elif i==8:
            print("\n\n Thank You :) \n")
        else :
            print("Invalid option selected. Please try again")

    

    