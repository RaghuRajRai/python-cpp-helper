import subprocess
import glob
import os
import argparse

# Defaults
CPP_ENV = "g++"
CODE_DIR = "cpp_source_files"

def translate_to_exe(filename):
    return filename.split('.')[0] + ".exe"

def run(cpp_file, exe_name_gen):
    exe_file = exe_name_gen(cpp_file)
    _output = subprocess.getoutput(CPP_ENV + ' ' + cpp_file + ' -o ' + exe_file)
    if _output == "":
        subprocess.run(exe_file)
        os.remove(exe_file)
    else:
        print(_output)

def flow():
    os.chdir(CODE_DIR)
    cpp_files = list(filter(lambda filename: "cpp" in filename.split('.'), glob.glob("*")))
    for file in cpp_files:
        run(file, translate_to_exe)

def validate_dir_path():
    if not os.path.isdir(CODE_DIR):
        raise Exception("Invalid directory path/path does not exists.")

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--cpp_env', help='Name of the cpp environment installed (eg: g++).')
    parser.add_argument('--code_dir', help='Path to directory containing cpp files to be executed.')
    args=parser.parse_args()

    if args.cpp_env:
        CPP_ENV = args.cpp_env
    
    if args.code_dir:
        CODE_DIR = args.code_dir
        validate_dir_path()

    flow()