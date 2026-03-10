
import json
import os

# utils/file_manager.py

def load_data(filename):
    """
    Load data from JSON file in data/ folder
    
    Args:
        filename: Name of the file (e.g., "customers.json")
    
    Returns:
        List or dict depending on file type
    """
    file_path = os.path.join("data", filename)
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        # Return empty list for customer files, empty dict for admin
        if filename == "admin.json":
            return {}
        return []
    except json.JSONDecodeError:
        print(f" Error reading {filename}. File might be corrupted.")
        return [] if filename != "admin.json" else {}
    except Exception as e:
        print(f"Unexpected error: {e}")
    except:
        print("some error happened")

def save_data(filename, data):
    """
    Save data to JSON file in data/ folder
    
    Args:
        filename: Name of the file
        data: Data to save (list or dict)
    
    Returns:
        True if successful, False if failed
    """
    file_path = os.path.join("data", filename)
    
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving to {filename}: {e}")
        return False