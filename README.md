# Project Documentation (created by the agent)

## Overview

This project implements an autonomous software agent using the Ollama model (`qwen3:8b`) to process tasks through a set of utility functions. The agent reads and processes files, executes directory operations, and provides mathematical calculations.

## Available Tools

### 1. `calculate_percentage(part: float, total: float) -> str`

**Description**: Calculates the percentage of a part relative to a total.  
**Example**:

```python
calculate_percentage(25, 100)  # Returns "25.00%"
```

### 2. `list_dir_entries() -> List[str]`

**Description**: Lists all files and directories in the current working directory.  
**Example**:

```python
list_dir_entries()  # Returns ["file1.txt", "folder1", ...]
```

### 3. `list_all_dir_entries(path_str: str) -> List[str]`

**Description**: Recursively lists all files and directories in the specified path. Ignores common irrelevant folders like `venv`, `__pycache__`, etc.  
**Example**:

```python
list_all_dir_entries("./src")  # Returns recursive list of entries in src/
```

### 4. `read_file(path_str: str) -> str`

**Description**: Reads and returns the content of a file at the specified path.  
**Example**:

```python
read_file("./src/tools.py")  # Returns the content of tools.py
```

### 5. `create_file(path_str: str, content: str) -> str`

**Description**: Creates a new file or overwrites an existing one at the specified path with the provided content.  
**Example**:

```python
create_file("./new_file.txt", "Hello, world!")  # Creates new_file.txt with the content
```

## Client Integration

The `client.py` file orchestrates the agent's behavior by:

1. Initializing the Ollama model (`qwen3:8b`)
2. Defining available tools via the `available_functions` dictionary
3. Handling user interactions through structured messages and tool calls

## Usage

To use this project:

1. Ensure Ollama is installed and running
2. Use the `read_file`/`create_file` tools to process files
3. Leverage mathematical and directory operations for task automation
