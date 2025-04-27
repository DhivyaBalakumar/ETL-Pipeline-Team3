import threading
import subprocess

def run_views():
    subprocess.run(["python", "extractViews.py"])

def run_likes():
    subprocess.run(["python", "extractLikes.py"])

def run_comments():
    subprocess.run(["python", "extractComments.py"])

# Create threads
t1 = threading.Thread(target=run_views)
t2 = threading.Thread(target=run_likes)
t3 = threading.Thread(target=run_comments)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all to complete (optional)
t1.join()
t2.join()
t3.join()
