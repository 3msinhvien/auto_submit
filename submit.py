import os
import requests

# Gửi code lên OJ
class Submitter:
    def __init__(self, problem_id: str, code_file: str, compiler_id: str, token: str, cookies: dict):
        self.problem_id = problem_id
        self.code_file = code_file  # Đường dẫn file code
        self.compiler_id = compiler_id
        self.token = token
        self.cookies = cookies

    def submit(self):
        url = "https://code.ptit.edu.vn/student/solution"
        # Đọc code từ file
        with open(self.code_file, 'r', encoding='utf-8') as f:
            code_content = f.read()
        # Tạo payload multipart/form-data
        files = {
            'code_file': (os.path.basename(self.code_file), code_content, 'text/x-python')
        }
        data = {
            '_token': self.token,
            'question': self.problem_id,
            'compiler': self.compiler_id
        }
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Origin': 'https://code.ptit.edu.vn',
            'Referer': f'https://code.ptit.edu.vn/student/question/{self.problem_id}'
        }
        response = requests.post(url, data=data, files=files, cookies=self.cookies, headers=headers)
        if response.status_code == 200:
            print('Submit thành công!')
            print("URL:", url)
            print("Cookies:", self.cookies)
            # Có thể xử lý lấy submission_id từ response nếu cần
        else:
            print(f'Lỗi submit: {response.status_code}')
            print(response.text)
