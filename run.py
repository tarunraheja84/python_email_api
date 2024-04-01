import subprocess

# Execute commands
commands = [
    "python3 -m venv myenv",
    "source myenv/bin/activate",
    "pip install --upgrade pip",
    "pip install -r requirements.txt"
]

for cmd in commands:
    subprocess.run(cmd, shell=True)

# Run Flask application
subprocess.run("python3 app.py", shell=True)
