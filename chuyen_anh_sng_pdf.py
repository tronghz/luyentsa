import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Đường dẫn đến thư mục chứa ảnh
image_folder = r"C:\Users\Welcome\Downloads\dap_an_toan"

# Tạo danh sách các tệp ảnh trong thư mục
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
image_files.sort()  # Sắp xếp các tệp theo thứ tự

# Tạo tệp PDF
pdf_filename = r"C:\Users\Welcome\Downloads\dap_an_toan.pdf"
c = canvas.Canvas(pdf_filename, pagesize=letter)
width, height = letter

for i, image_file in enumerate(image_files, start=1):
    img_path = os.path.join(image_folder, image_file)
    img = Image.open(img_path)
    
    # Thêm tiêu đề câu hỏi
    c.setFont("Helvetica-Bold", 14)
    c.drawString(inch, height - inch, f"Câu {i}:")
    
    # Tính toán kích thước và vị trí cho ảnh
    img_width, img_height = img.size
    aspect = img_width / float(img_height)
    max_width = width - 2*inch
    max_height = height - 2*inch - 20  # Trừ đi khoảng trống cho tiêu đề
    
    if aspect > 1:  # ảnh ngang
        new_width = min(img_width, max_width)
        new_height = new_width / aspect
    else:  # ảnh dọc
        new_height = min(img_height, max_height)
        new_width = new_height * aspect
    
    x = (width - new_width) / 2
    y = height - inch - 20 - new_height  # Đặt ảnh dưới tiêu đề
    
    # Chèn ảnh vào PDF
    c.drawImage(img_path, x, y, width=new_width, height=new_height, preserveAspectRatio=True)
    
    c.showPage()

c.save()

print(f"PDF đã được tạo: {pdf_filename}")