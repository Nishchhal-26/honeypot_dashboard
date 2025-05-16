import subprocess

def start_cowrie():
    subprocess.run(["docker", "run", "-d", "-p", "2222:2222", "cowrie/cowrie"])

def stop_cowrie():
    subprocess.run(["docker", "stop", "$(docker ps -q --filter ancestor=cowrie/cowrie)"], shell=True)
