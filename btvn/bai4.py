# # Input
# # Lựa chọn (1-5)
# # Mã  (str)
# # Số lượng mua (int)
# # Số lượng nhập kho (int)
# tạo product_list
# while True
#     menu
#     Nhập lựa chọn
#     chọn = 1
#         Hiển thị danh sách 
#         Tính trạng thái tồn kho
#     chọn = 2
#         Nhập mã sản phẩm
#         Chuẩn hóa mã
#         Kiểm tra tồn tại
#         Nếu không tồn tại
#             Báo lỗi
#         Nhập số lượng mua
#         Kiểm tra hợp lệ
#         Nếu vượt tồn kho
#             Báo lỗi
#         Cập nhật:
#             quantity -= số lượng mua
#             sold += số lượng mua
#         Tính tiền thanh toán
#     chọn = 3
#         Nhập mã sản phẩm
#         Kiểm tra tồn tại
#         Nhập số lượng nhập
#         Kiểm tra hợp lệ
#         quantity += số lượng nhập
#     chọn = 4
#         Tính doanh thu từng sản phẩm
#         Tính tổng doanh thu
#         Tìm sản phẩm bán chạy nhất
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:
    print("""
===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====
1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho
2. Bán sản phẩm cho khách hàng
3. Nhập thêm hàng vào kho
4. Xem báo cáo doanh thu
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
                print("Danh sách trống")
            else:
                print("Danh sách sản phẩm:")
                for index, product in enumerate(product_list, start=1):
                    if product["quantity"] == 0:
                        status = "Hết hàng"
                    elif product["quantity"] <= 5:
                        status = "Sắp hết hàng"
                    else:
                        status = "Còn hàng"
                    print(f"{index}. Mã SP: {product['product_id']} | Tên: {product['product_name']} | Giá: {product['price']} | Tồn kho: {product['quantity']} | Đã bán: {product['sold']} | Trạng thái: {status}")
        case 2:
            product_id = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()
            found = False
            for product in product_list:
                if product["product_id"] == product_id:
                    found = True
                    buy_quantity = input("Nhập số lượng khách mua: ")
                    if not buy_quantity.isdigit() or int(buy_quantity) <= 0:
                        print("Số lượng không hợp lệ")
                        break
                    buy_quantity = int(buy_quantity)
                    if buy_quantity > product["quantity"]:
                        print("Số lượng trong kho không đủ để bán")
                        break
                    product["quantity"] -= buy_quantity
                    product["sold"] += buy_quantity
                    total_price = buy_quantity * product["price"]
                    print("Bán thành công")
                    print(f"thanh toán: {total_price}")
                    break
            if not found:
                print("Không tìm thấy sản phẩm")
        case 3:
            product_id = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()
            found = False
            for product in product_list:
                if product["product_id"] == product_id:
                    found = True
                    import_quantity = input("Nhập số lượng: ")
                    if not import_quantity.isdigit() or int(import_quantity) <= 0:
                        print("Số lượng không hợp lệ")
                        break
                    import_quantity = int(import_quantity)
                    product["quantity"] += import_quantity
                    print("Nhập thành công")
                    break
            if not found:
                print("Không tìm thấy sản phẩm")
        case 4:
            total_revenue = 0
            total_sold = 0
            best_seller = ""
            max_sold = -1
            for index, product in enumerate(product_list, start=1):
                revenue = product["price"] * product["sold"]
                total_revenue += revenue
                total_sold += product["sold"]
                if product["sold"] > max_sold:
                    max_sold = product["sold"]
                    best_seller = product["product_name"]
                print(f"{index}. {product['product_name']} | Đã bán: {product['sold']} | Doanh thu: {revenue}")
            if total_sold == 0:
                print("Chưa có doanh thu")
            else:
                print()
                print(f"Tổng doanh thu: {total_revenue}")
                print(f"Sản phẩm bán chạy nhất: {best_seller}")
        case 5:
            print("Thoát")
            break
        case _:
            print("Lựa chọn không hợp lệ")
