from ollama import chat
from tools import available_functions

model = "qwen3:8b"

tools = [
    {
        'type': 'function',
        'function': {
            'name': 'calculate_percentage',
            'description': 'Calculate the percentage of a part relative to a total.',
            'parameters': {
                'type': 'object',
                'required': ['part', 'total'],
                'properties': {
                    'part': {'type': 'number', 'description': 'The partial value'},
                    'total': {'type': 'number', 'description': 'The total value'},
                },
            },
        },
    },
    {
        'type': 'function',
        'function': {
            'name': 'list_dir_entries',
            'description': 'Lists all files and directories in the current folder',
            'parameters': {
                'type': 'object',
                'properties': {},
            },
        },
    },
    {
        'type': 'function',
        'function': {
            'name': 'list_all_dir_entries',
            'description': 'List all directories and files recursively in the selected folder path. If not requested, ignore folders like venv, __pycache__, node_modules, as those are not useful for your context',
            'parameters': {
                'type': 'object',
                'required': ['path_str'],
                'properties': {
                    'path_str': {
                        'type': 'string', 
                        'description': 'The directory path to list entries from (e.g., "." for current directory or an absolute path)'
                    }
                },
            },
        },
    },
    {
        'type': 'function',
        'function': {
            'name': 'read_file',
            'description': 'Reads and returns the content of a file from a given file path.',
            'parameters': {
                'type': 'object',
                'required': ['path_str'],
                'properties': {
                    'path_str': {
                        'type': 'string', 
                        'description': 'Path to the file to read. Can be relative (e.g. "./file.txt") or absolute path.'
                    }
                },
            },
        },
    },
    {
        'type': 'function',
        'function': {
            'name': 'create_file',
            'description': 'Creates a new file or overwrites an existing one at the specified path with the provided content, returning the saved content.',
            'parameters': {
                'type': 'object',
                'required': ['path_str'],
                'properties': {
                    'path_str': {
                        'type': 'string', 
                        'description': 'Path where the file will be created. Can be relative (e.g., "./new_file.txt") or an absolute path.'
                    },
                    'content': {
                        'type': 'string',
                        'description': 'The text content to be written into the file.'
                    }
                },
            },
        },
    }
]

messages = [
    {"role": "user", "content": "Read client.py, tools.py and requirements.txt files at root folder and create me a readme documentation file for this project at the root folder"}
]

response = chat(
    model=model,
    messages=messages,
    tools=tools,
    stream=False,
)

print(response)

msg = response["message"]
messages.append(msg)

if "tool_calls" in msg:
    for tool_call in msg["tool_calls"]:
        func_name = tool_call["function"]["name"]
        func_args = tool_call["function"]["arguments"]

        if func_name in available_functions:
            function_to_call = available_functions[func_name]
            result = function_to_call(**func_args)

            print(f"Ollama decidiu usar a ferramenta {func_name} com os argumentos {func_args}")

            messages.append({
                "role": "tool",
                "content": str(result)
            })

final = chat(
    model=model,
    messages=messages,
    stream=True
)

for chunk in final:
    print(chunk["message"].get("content", ""), end="")