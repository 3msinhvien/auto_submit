from login import LoginManager
from fetch_problem import ProblemFetcher
from submit import Submitter
from checker import ResultChecker
import os
import time

if __name__ == "__main__":
    print("Chọn chế độ:")
    print("1. Submit theo thứ tự file từ x đến y trong folder Python-PTIT")
    print("2. Nhập thủ công mã bài muốn submit")
    mode = int(input("Nhập lựa chọn (1 hoặc 2): "))

    if mode == 1:
        files = sorted([f for f in os.listdir("Python-PTIT") if f.endswith(".py")])
        print(f"Có {len(files)} file trong thư mục Python-PTIT.")
        x = int(input("Nhập chỉ số bắt đầu (x, bắt đầu từ 1): "))
        y = int(input("Nhập chỉ số kết thúc (y): "))
        files_to_submit = files[x-1:y]
        problem_ids = []
        for fname in files_to_submit:
            code_file = os.path.join("Python-PTIT", fname)
            # Lấy mã bài là phần trước dấu '-' và bỏ khoảng trắng
            problem_id = fname.split('-')[0].strip().replace(' ', '')
            problem_ids.append((problem_id, code_file))
    else:
        n = int(input("Nhập số lượng bài muốn submit: "))
        problem_ids = []
        for i in range(n):
            pid = input(f"Nhập mã bài thứ {i+1}: ")
            # Tìm file code bắt đầu bằng mã problem_id
            code_file = None
            for fname in os.listdir("Python-PTIT"):
                if fname.startswith(pid) and fname.endswith(".py"):
                    code_file = os.path.join("Python-PTIT", fname)
                    break
            problem_ids.append((pid, code_file))

    compiler_id = "4"  # Python3 trên PTIT OJ
    token = "ZWXP8v1VgNMF6BSkTYwisIKyuHVqX0EfffbGFZ1O"  # Lấy từ form submit thực tế
    cookies = {
        # Dán các cookie cần thiết lấy từ trình duyệt vào đây
         "ptit_code_session": "eyJpdiI6IlZBVWxTRGFacE80S3N4bXhqcjZHcFE9PSIsInZhbHVlIjoiT09wUW1qNktlOGVLMUM1aVNVaUh3a3lzdEZjMjZoeEp2VVBSdkFnNnpxazhPbTJqQThJdVI2NHJITE9IK3QrbWQrL2xNenUyYmtvaG5BYnpCWDU3TkZPMDYyOVhQVVJYUlNjTEFPeWFveDJxVGZWRVpMcDY4WFR1cjRDMkkrUFAiLCJtYWMiOiJhZjc0NzQ2Y2E3ZWNiMmMxODZhN2U1ODM2NjMwYzZkMjBiMGU3MjEyNTQ0ZDk4ZGIxOGEzMjBhOWFiM2E1NDI3IiwidGFnIjoiIn0%3D",
         "XSRF-TOKEN": "eyJpdiI6Ilk1L0d1b3o2L3dnUVNRZ3Z3WXh2VFE9PSIsInZhbHVlIjoiUTBLSC9jVlBRVW0rdUdqSHFpTWpnTGJCYi9mWHJHVDVidVg3MllySEsrRFlQUlVlc2YyL09aeit5RnFyUEVZTG0xcEhiNE0xbnYzOFlCc3VSSXVlc1kyRFpYZU9vUDQrMHdNYnA4U24wSFFwZXdZRnBQTHl4cVRiRi9LVGs0QXEiLCJtYWMiOiJhZjU2OTdhZjliZWQzMTJmZDEzMDU2ZjU5N2ExOWZhM2Y2YjMwYzVlOWIxM2YzY2Q1ZjIzOTdkNzEyOWEwZTk4IiwidGFnIjoiIn0%3D"
        # Thêm các cookie khác nếu cần
    }

    for problem_id, code_file in problem_ids:
        print(f"DEBUG: Đang submit bài: {problem_id}, file: {code_file}")
        if not code_file or not os.path.exists(code_file):
            print(f"Không tìm thấy file code cho bài {problem_id} trong thư mục Python-PTIT!")
            continue
        submitter = Submitter(problem_id, code_file, compiler_id, token, cookies)
        submitter.submit()
        time.sleep(10)  # Giãn cách 10 giây giữa các lần submit

        # Theo dõi kết quả (nâng cấp sau nếu cần lấy submission_id tự động)
        # submission_id = "submission_id"
        # checker = ResultChecker(submission_id)
        # checker.check_result()
