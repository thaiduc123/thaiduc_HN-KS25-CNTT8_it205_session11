# Tuple product_info ban đầu có 4 phần tử
# Phần tử "SP001" đang nằm ở index index 0
# product_info[1] là phần tử ở vị trí thứ 2 của tuple "Áo polo nam" trong khi mã sản phẩm "SP001" nằm ở index 0
# Phần tử "Áo polo nam" đang nằm ở index 1
# product_info[2] là "Size L" trong khi tên sản phẩm "Áo polo nam" nằm ở index 1
#dòng sau gây lỗi product_length = product_info.length() vì kiểu dữ liệu tuple không có phương thức length()
#Muốn đếm số phần tử trong tuple cần dùng hàm len()
# dòng sau không hợp lệ product_info[3] = 279000 product_info là một tuple, là kiểu dữ liệu immutable
product_info = ("SP001", "Áo polo nam", "Size L", 299000)
product_code = product_info[1]
product_name = product_info[2]
product_length = len(product_info)
new_product_info = product_info[:3] + (279000, )
print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", new_product_info)
