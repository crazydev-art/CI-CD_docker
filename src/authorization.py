import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_address = 'api_container'
api_port = 8000

def authorization_test():
    users = [
        {"username": "bob", "password": "builder", "models": ["v1","v2"]},
        {"username": "alice", "password": "wonderland", "models": ["v1","v2"]}
    ]
    sentence = "test sentence"

    for user in users:
        for model in user["models"]:
            endpoint = f"/{model}/sentiment"
            r = requests.get(
                f'http://{api_address}:{api_port}{endpoint}',
                params={"username": user["username"], "password": user["password"], "sentence": sentence}
            )
            status_code = r.status_code
            test_status = "SUCCESS" if status_code == 200 else "FAILURE"
            log_output = f"""
            ============================
                Authorization Test
            ============================
            User: {user["username"]}
            Model : {model}
            Expected: 200
            Actual: {status_code}
            ==> {test_status}
            """
            print(log_output)
            log_file = os.getenv("LOG_FILE", "/shared_logs/api.log")
            if os.environ.get('LOG') == '1':
                with open(log_file, 'a') as file:
                    file.write(log_output)


authorization_test()
