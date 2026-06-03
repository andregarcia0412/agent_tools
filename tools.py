import os
from typing import List
from pathlib import Path

def calculate_percentage(part: float, total: float) -> str:
    if total == 0:
        return "Error: Total cannot be zero."
    
    percentage = (part / total) * 100
    return f"{percentage:.2f}%"

def list_dir_entries() -> List[str]:
    return os.listdir(".")

def list_all_dir_entries(path_str: str) -> List[str]:
    base = Path(path_str)
    return [str(p) for p in base.rglob("*")]

def read_file(path_str: str) -> str:
    path = Path(path_str)
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
    
def create_file(path_str: str, content: str) -> str:
    path = Path(path_str)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
        
    return content

available_functions = {
    "calculate_percentage": calculate_percentage,
    "list_dir_entries": list_dir_entries,
    "list_all_dir_entries": list_all_dir_entries,
    "read_file": read_file,
    "create_file": create_file
}