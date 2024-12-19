import os
import requests
from dotenv import load_dotenv


load_dotenv()

api_address = 'api_container'
api_port = 8000

def authentication_test():
    test_cases = [
        {"username": "alice", "password": "wonderland", "expected_code": 200},
        {"username": "bob", "password": "builder", "expected_code": 200},
        {"username": "clementine", "password": "mandarine", "expected_code": 403},
    ]

    for case in test_cases:
        r = requests.get(
            f'http://{api_address}:{api_port}/permissions',
            params={"username": case["username"], "password": case["password"]}
        )
        status_code = r.status_code
        test_status = "SUCCESS" if status_code == 200 else "FAILURE"
        output = f"""
        ============================
            Authentication Test
        ============================
        request done at "/permissions"
        Username: {case["username"]}
        Password={case["password"]}
        Expected result = 200
        ==> {test_status}
        """
        print(output)
        log_file = os.getenv("LOG_FILE", "/shared_logs/api.log")
        if os.environ.get('LOG') == '1':
             with open(log_file, 'a') as file:
                 file.write(output)


authentication_test()