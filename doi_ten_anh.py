import os

# Đường dẫn đến thư mục chứa ảnh
folder_path = r"C:\Users\Welcome\OneDrive\Hình ảnh\Ảnh chụp màn hình"

# Lấy danh sách tất cả các file trong thư mục
files = os.listdir(folder_path)

# Lọc ra chỉ các file ảnh (có thể thêm các định dạng khác nếu cần)
image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# Sắp xếp các file ảnh (tùy chọn)
image_files.sort()

# Đổi tên các file ảnh
for index, old_name in enumerate(image_files, start=1):
    # Tạo tên mới
    new_name = f'tai_lieu_b5_{index}.jpg'
    
    # Đường dẫn đầy đủ cho file cũ và mới
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    
    # Đổi tên file
    os.rename(old_path, new_path)
    print(f'Đã đổi tên {old_name} thành {new_name}')

print('Hoàn tất đổi tên ảnh.')