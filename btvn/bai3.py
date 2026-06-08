# # input
# # Lựa chọn menu
# # Mã (str)
# # Tên (str)
# # Giá (int)
# # Số lượng (int)
# tạo product_list
# Lặp vô hạn
#     menu
#     Nhập lựa chọn
#      chọn = 1
#         Hiển thị danh sách 
#     chọn = 2
#         Nhập thông tin sản phẩm
#         Chuẩn hóa mã sản phẩm
#         Kiểm tra trùng mã
#         Nếu trùng
#             Thông báo 
#         Ngược lại
#             Kiểm tra giá và số lượng
#             Nếu hợp lệ
#                 Thêm sản phẩm
#                 Thông báo 
#             Ngược lại
#                 Thông báo 
#     chọn = 3
#         Nhập mã sản phẩm
#         Tìm 
#         Nếu không tồn tại
#             Thông báo 
#         Nếu tồn tại
#             Nhập thông tin mới
#             Kiểm tra dữ liệu
#             Cập nhật sản phẩm
#     chọn = 4
#         Nhập mã 
#         Tìm sản phẩm
#         Nếu tồn tại
#             Xóa sản phẩm
#         Ngược lại
#             Thông báo 

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    print("""
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình
""")
    choice = input("Nhập lựa chọn: ")
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue
    choice = int(choice)
    match choice:
        case 1:
            if len(product_list) == 0:
                print("Danh sách đang trống.")
            else:
                print("Danh sách sản phẩm:")
                for i, product in enumerate(product_list, start=1):
                    print(f"{i}. Mã SP: {product['product_id']} | Tên: {product['product_name']} | Giá: {product['price']} | Số lượng: {product['quantity']}")
        case 2:
            product_id = input("Nhập mã sản phẩm: ").strip().upper()
            product_name = input("Nhập tên sản phẩm: ").strip()
            price = input("Nhập giá sản phẩm: ")
            quantity = input("Nhập số lượng sản phẩm: ")
            dup  = False
            for i in product_list:
                if i["product_id"] == product_id:
                    dup  = True
                    break
            if dup:
                print("Mã sản phẩm trùng")
                continue
            if int(price) <= 0 or int(quantity) <= 0:
                print("không hợp lệ")
                continue
            new_product = {
                "product_id": product_id,
                "product_name": product_name,
                "price": int(price),
                "quantity": int(quantity)
            }
            product_list.append(new_product)
            print("Thêm sản phẩm thành công")
        case 3:
            update_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
            for product in product_list:
                if product["product_id"] == update_id:
                    product_name = input("Nhập tên sản phẩm mới: ").strip()
                    price = input("Nhập giá sản phẩm mới: ")
                    quantity = input("Nhập số lượng mới: ")
                    if int(price) <= 0 or int(quantity) <= 0:
                        print("Giá - Số lượng không hợp lệ")
                        break
                    product["product_name"] = product_name
                    product["price"] = int(price)
                    product["quantity"] = int(quantity)
                    print("Cập nhật sản phẩm thành công")
                    break
            else:
                print("Không tìm thấy mã sản phẩm")
        case 4:
            delete_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
            for product in product_list:
                if product["product_id"] == delete_id:
                    product_list.remove(product)
                    print("Xóa thành công")
                    break
            else:
                print("Không tìm thấy mã")
        case 5:
            print("Thoát")
            break
        case _:
            print("Lựa chọn không hợp lệ")
