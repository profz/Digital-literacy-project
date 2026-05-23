# test_code.py
import os
import hashlib
import pickle

# --- SECURITY VULNERABILITY & CODE SMELL ---
# Global configuration token hardcoded (Smell)
API_TOKEN = "ghp_AbCdEf1234567890SecretTokenDoNotShare"

def process_user_data(user_input_string):
    """
    Simulates parsing user payload data.
    """
    # --- SECURITY: Insecure Deserialization ---
    # Accepting raw input directly into pickle.loads is a critical RCE vulnerability
    data = pickle.loads(user_input_string)
    return data

def hash_password_insecurely(password):
    """
    Hashes user passwords for storage.
    """
    # --- SECURITY & PERFORMANCE: Weak/Fast Hash Function ---
    # MD5 is broken for security applications. 
    # Also, calling .encode('utf-8') repeatedly inside complex logic can be optimized.
    hasher = hashlib.md5()
    hasher.update(password.encode('utf-8'))
    return hasher.hexdigest()

def calculate_analytics(numbers_list):
    """
    Calculates moving square metrics on a numeric list.
    """
    results = []
    
    # --- PERFORMANCE: O(N^2) Bottleneck ---
    # Using 'in' lookups or inner scanning inside loops creates drastic performance issues on large lists
    for i in range(len(numbers_list)):
        current_num = numbers_list[i]
        
        # Inefficient duplicate calculation inside a loop
        if current_num not in results:
            # --- BUG / SMELL: Inefficient lookup array append ---
            results.append(current_num ** 2)
            
    return results

def read_log_file(file_path):
    """
    Reads lines from a local file path string.
    """
    # --- BUG / SMELL: Resource Leak ---
    # File descriptor opened manually without a context manager (with open) or close() block.
    # If an exception occurs, the file handler hangs open indefinitely.
    file_handler = open(file_path, 'r')
    contents = file_handler.read()
    return contents

def divide_user_scores(score_a, score_b):
    """
    Divides two computed user matrix metrics.
    """
    # --- BUG: ZeroDivisionError & Missing Return Path ---
    # If score_b evaluates to 0, this will crash the runtime process.
    # Also, it missing an explicit edge-case handling routine.
    if score_b != 0:
        final_score = score_a / score_b
        return final_score
    # If score_b == 0, it implicitly returns None, which might break the calling function

# --- CODE SMELL: Dead Code & Complex Syntax ---
class DataProcessor:
    def __init__(self):
        pass  # Unnecessary empty constructor
        
    def placeholder_function(self):
        # Unused variable arguments and nested dead-ends
        x = 10
        y = 20
        z = x + y
        return None
