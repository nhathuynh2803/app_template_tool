from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Tạo thư mục uploads nếu chưa có
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    data = None
    if request.method == 'POST':
        # Kiểm tra xem người dùng đã chọn file chưa
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        # Nếu người dùng không chọn file nào
        if file.filename == '':
            return redirect(request.url)
        
        # Nếu có file thì lưu trữ và xử lý
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Đọc file Excel và lưu dữ liệu vào pandas DataFrame
            data = pd.read_excel(file_path)

            # Hiển thị dữ liệu trên trang web
            return render_template('upload.html', data=data)
    
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=True)
