# Gunicorn configuration file
import multiprocessing

max_requests = 1000
max_requests_jitter = 50

log_file = "-"

host = os.environ.get("HOST", "0.0.0.0")  # Default to '0.0.0.0' if not set
port = os.environ.get("PORT", "50505")    # Default to '50505' if not set

bind = f"{host}:{port}"

workers = (multiprocessing.cpu_count() * 2) + 1
threads = workers

timeout = 120