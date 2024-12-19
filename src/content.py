import os
import requests
from dotenv import load_dotenv


load_dotenv()


api_address = 'api_container'
api_port = 8000

def test_content():
    sentences = [
        {"text": "life is beautiful", "expected_sign": 1},
        {"text": "that sucks", "expected_sign": -1}
    ]
    user = {"username": "alice", "password": "wonderland"}

    for model in ["v1", "v2"]:
        for sentence in sentences:
            endpoint = f"/{model}/sentiment"
            r = requests.get(
                f'http://{api_address}:{api_port}{endpoint}',
                params={"username": user["username"], "password": user["password"], "sentence": sentence["text"]}
            )
            score = r.json().get("score", 0)
            test_status = "SUCCESS" if (score > 0 and sentence["expected_sign"] > 0) or (score < 0 and sentence["expected_sign"] < 0) else "FAILURE"
            log_output = f"""
            ============================
                Content Test
            ============================
            Users : {user['username']}
            Model: {model}
            Sentence: {sentence["text"]}
            Expected: {sentence["expected_sign"]}
            Actual: {score}
            ==> {test_status}
            """
            print(log_output)
            log_file = os.getenv("LOG_FILE", "/shared_logs/api.log")
            if os.environ.get('LOG') == '1':
                with open(log_file, 'a') as file:
                    file.write(log_output)


test_content()
