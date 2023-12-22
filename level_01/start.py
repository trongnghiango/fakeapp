
"""
Bien va Kieu du lieu
"""
x = 10 # Khai báo biến x và khởi tạo với value: 10
xType = type(x) #Check kiểu của biến x là gì?
xAdr = id(x) # id là lấy địa chỉ vùng nhớ của x dạng cơ số 10 
hexAdr = hex(xAdr) # địa chỉ vùng nhớ dạng hex của biến x
print(f"Bien x co gia tri {x} co kieu du lieu {xType} luu ow Addr: {hexAdr}")