import psutil
import os

def monitor_resources(stage):
    """
    Fungsi untuk memantau penggunaan CPU dan memori (RAM) selama tahap tertentu
    """
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    cpu_percent = psutil.cpu_percent(interval=1)  # CPU usage over 1 second
    memory_mb = memory_info.rss / (1024 ** 2)  # Memory usage in MB
    print(f"--- {stage} ---")
    print(f"CPU usage: {cpu_percent}%")
    print(f"Memory usage: {memory_mb:.2f} MB")
