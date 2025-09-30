import os
import re


def check_output_path(output: str) -> bool:
    """Check correctness of output file's abolute path: directory exists and fname mathces regex"""
    head, tail = os.path.split(output)
    if os.path.exists(head):
        if re.fullmatch("^\\w+\\.(?:png|jpg|jpeg)$", tail) is not None:
            return True
        else:
            print(f"Output file error: Can't create file with name: {tail}")
            return False
    else:
        print(f"Output file error: Directory {head} doesn't exist")
        return False
