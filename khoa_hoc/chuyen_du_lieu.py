import os
import json

# Đường dẫn đến thư mục chứa ảnh
folder_path = r"D:\tool_tong\code\on_luyen_tsa\khoa_hoc\khobaitap_toan"

# Lấy danh sách tên file trong thư mục
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Tạo danh sách câu hỏi
questions = [f"khobaitap_toan/{image}" for image in image_files]

# Tạo nội dung JavaScript
js_content = f"const questions = {json.dumps(questions, indent=2)};"

# Đường dẫn file JavaScript đầu ra
output_file = r"D:\tool_tong\code\on_luyen_tsa\khoa_hoc\khobaitap_toan.js"

# Ghi nội dung vào file JavaScript
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"File JavaScript đã được tạo tại: {output_file}")