import os
import json
import re

# Đường dẫn đến thư mục chứa ảnh
folder_path = r"D:\tool_tong\code\tsa\khoahoc\khotailieu_b6"

# Hàm để trích xuất số từ tên tệp
def extract_number(filename):
    match = re.search(r'_b5_(\d+)\.', filename)
    return int(match.group(1)) if match else 0

# Lấy danh sách tên file trong thư mục
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Sắp xếp danh sách tệp theo số
image_files.sort(key=extract_number)

# Tạo danh sách câu hỏi
questions = [f"khotailieu_b6/{image}" for image in image_files]

# Tạo nội dung JavaScript
js_content = f"const questions = {json.dumps(questions, indent=2)};"

# Đường dẫn file JavaScript đầu ra
output_file = r"D:\tool_tong\code\tsa\khoahoc\khobaitap_toan.js"

# Ghi nội dung vào file JavaScript
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"File JavaScript đã được tạo tại: {output_file}")