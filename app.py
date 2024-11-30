from flask import Flask, render_template
import psutil
import requests
import socket

app = Flask(__name__)

def check_server_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Online"
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def get_cpu_usage():
    return psutil.cpu_percent()

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

@app.route('/')
def dashboard():
    server_status = check_server_status("https://example.com") 
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    
    return render_template('dashboard.html', server_status=server_status,
                           cpu_usage=cpu_usage, memory_usage=memory_usage,
                           disk_usage=disk_usage)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
