import sys
from subprocess import Popen, PIPE
from settings import BASE_DIR
import time

PROBLEM_DIR = BASE_DIR / "templates" / "problems"

def evaluator(code):
    user_code_file = PROBLEM_DIR / "user_code.py"

    input_data_file = PROBLEM_DIR / "input_data.txt"
    expected_output_file = PROBLEM_DIR / "output_data.txt"

    user_output_file = PROBLEM_DIR / "real_output.txt"
    user_error_file = PROBLEM_DIR / "real_output_err.txt"
    
    with open(user_code_file, "wt") as f:
        f.write(code)
    stdin = open(input_data_file, "rt")
    stdout = open(user_output_file, "wt")
    stderr = open(user_error_file, "wt")

    time_start = time.time()
    p = Popen(["python3", user_code_file], stdin=stdin, stdout=stdout, stderr=stderr)
    while not p.poll() != None:
        pass
    p.terminate()
    time_end = time.time()

    stdin.close()
    stdout.close()
    stderr.close()
    
    # check result
    error = ""
    with open(user_error_file, "rt") as f:
        error = f.read().strip()
    
    with open(user_output_file, "rt") as f:
        user_output = f.read().strip()
    
    with open(expected_output_file, "rt") as f:
        expected_output = f.read().strip()
    
    result = True
    if user_output != expected_output:
        result = False
    print(user_output)
    print(expected_output)
    
    duration = time_end - time_start

    
    return result, error, duration