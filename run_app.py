import subprocess
import os

# Run FastAPI backend
subprocess.Popen(['uvicorn', 'backend:app', '--reload'])

# Run Streamlit frontend
subprocess.Popen(['streamlit', 'run', 'frontend.py'])