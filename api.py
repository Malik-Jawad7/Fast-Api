import sys
import os
from pathlib import Path

# Get the absolute path to the directory this file is in
BASE_DIR = Path(__file__).resolve().parent

# Add the BASE_DIR to sys.path so 'app' can be found
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

# Import the FastAPI app
try:
    from app.main import app
except ModuleNotFoundError as e:
    raise RuntimeError(f"❌ Could not import app.main — make sure your folder structure is correct.\nError: {e}")
