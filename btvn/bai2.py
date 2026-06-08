#Dictionary trên có 4 key "employee_id" "full_name" "department" "status"
#dòng sau gây lỗi employee_id = employee[0]: dictionary truy cập dữ liệu thông qua key, không phải vị index
# Dictionary ko truy cập phần tử bằng index giống list 
#Muốn lấy mã nhân viên "NV001": employee_id = employee["employee_id"]
#dòng sau gây lỗi full_name = employee["name"]: trong dictionary không có key "name"
#Key đúng là "full_name"
#dòng sau chưa cập nhật đúng trạng thái employee["employee_status"] = "official", nó tạo thêm một key mới "employee_status"
#Muốn cập nhật trạng thái nhân viên, cần dùng key "status"
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}
employee_id = employee["employee_id"]
full_name = employee["full_name"]
employee["employee_status"] = "official"
employee["base_salary"] = 15000000
del employee["department"]
print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)
