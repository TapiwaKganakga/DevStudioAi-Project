# Run simple static analysis (flake8). For demo we will just run flake8 as subprocess
# and return output string.

import subprocess

def run_flake8(file_path: str) -> str:
    try:
        result = subprocess.run(
            ["flake8", file_path, "--format=default"],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error running flake8: {e}"
