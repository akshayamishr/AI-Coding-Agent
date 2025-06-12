import os

def write_in_file(file_name,content):
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("\n".join(content))

def change_dir_and_write_code(path,file_name,content):
    os.chdir(path)
    write_in_file(file_name,content)

def run_command(cmd: str):
    result = os.system(cmd)
    return result
