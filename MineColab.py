# @title Claude AI
import subprocess
import time
import os
import threading
import signal
from IPython.display import display, HTML, clear_output
from google.colab import drive

# Constants
DRIVE_PATH = "/content/drive/MyDrive/Minecraft-server-java"
JAVA_VERSIONS = ["8", "17", "21"]
SERVER_JAR = "paper-1.21-130.jar"

# Global variables
running = True
process = None

# Function to run shell commands and handle errors
def run_command(command, success_msg, error_msg):
    try:
        subprocess.run(command, check=True, shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        print(success_msg)
    except subprocess.CalledProcessError:
        print(error_msg)

# Function to display HTML content
def display_image(url, width, height):
    display(HTML(f'<p><img style="display: block; margin-left: auto; margin-right: auto;" src="{url}" alt="Server Image" width="{width}" height="{height}" /></p>'))

# Mount Google Drive
drive.mount('/content/drive')

# Create and change to Minecraft server directory
os.makedirs(DRIVE_PATH, exist_ok=True)
os.chdir(DRIVE_PATH)

# Create eula.txt
with open("eula.txt", "w") as f:
    f.write("eula=true")

# Install Java versions
print("Installing Java versions...")
run_command("sudo apt update", "apt cache successfully updated", "apt cache update failed, you might receive stale packages")
for version in JAVA_VERSIONS:
    run_command(f"sudo apt-get install -y openjdk-{version}-jre-headless", 
                f"OpenJDK {version} has been installed successfully.", 
                f"Failed to install OpenJDK {version}.")

# Display starting server image
display_image("https://github.com/LBY-L/MineColab/blob/master/COLAB-26-11-2022.png?raw=true", 327, 91)

# Set up tunneling service
tunnel_service = "playit"  # Change this to "ngrok" if you prefer ngrok
ngrok_auth_token = "YOUR_NGROK_AUTH_TOKEN"  # Replace with your actual token if using ngrok

if tunnel_service == "ngrok":
    print("Setting up ngrok...")
    run_command("pip install pyngrok", "pyngrok installed successfully", "Failed to install pyngrok")
    from pyngrok import conf, ngrok
    ngrok.set_auth_token(ngrok_auth_token)
    conf.get_default().region = "ap"  # Change to your closest region
    url = ngrok.connect(25565, 'tcp')
    print(f"Your server address is {url.public_url.replace('tcp://', '')}")
elif tunnel_service == "playit":
    print("Setting up PlayIt...")
    run_command("curl -SsL https://playit-cloud.github.io/ppa/key.gpg | sudo apt-key add -", "PlayIt key added", "Failed to add PlayIt key")
    run_command("sudo curl -SsL -o /etc/apt/sources.list.d/playit-cloud.list https://playit-cloud.github.io/ppa/playit-cloud.list", "PlayIt source list added", "Failed to add PlayIt source list")
    run_command("sudo apt update && sudo apt install -y playit", "PlayIt installed", "Failed to install PlayIt")
    subprocess.Popen(["nohup", "playit"], stdout=open("playit_output.log", "w"), stderr=subprocess.STDOUT)
    time.sleep(10)  # Wait for PlayIt to initialize
    with open("playit_output.log", "r") as f:
        print("PlayIt tunnel information:")
        print("\n".join(f.readlines()[-4:]))  # Display the last 4 lines of the log

# Display console image
display_image("https://github.com/LBY-L/MineColab/blob/master/CONSOLE-12-12-2022.png?raw=true", 511, 175)

# Function to handle server output with timestamp
def output_reader(process):
    global running
    start_time = time.time()
    while running:
        try:
            line = process.stdout.readline()
            if line:
                elapsed_time = time.time() - start_time
                print(f"[{elapsed_time:.2f}s] [SERVER] {line.strip()}")
            else:
                time.sleep(0.1)  # Short sleep to prevent CPU overuse
        except Exception as e:
            print(f"Error reading output: {e}")
            break

# Function to handle user input
def input_handler(process):
    global running
    while running:
        try:
            command = input("Enter a command (or 'stop' to quit): ")
            if command.lower() == "stop":
                process.stdin.write(f"{command}\n")
                process.stdin.flush()
                break
            if process.poll() is None:  # Check if the process is still running
                process.stdin.write(f"{command}\n")
                process.stdin.flush()
                print(f"[YOU] {command}")
            else:
                print("Server process has terminated. Cannot send command.")
                break
        except EOFError:
            break
        except BrokenPipeError:
            print("Server process has terminated. Cannot send command.")
            break
        except Exception as e:
            print(f"Error handling input: {e}")

# Function to handle graceful shutdown
def shutdown(signum, frame):
    global running, process
    running = False
    print("\nShutting down the Minecraft server...")
    if process and process.poll() is None:
        try:
            process.stdin.write("stop\n")
            process.stdin.flush()
        except:
            pass  # Ignore errors when trying to send stop command
        try:
            process.wait(timeout=30)  # Wait up to 30 seconds for the server to stop
        except subprocess.TimeoutExpired:
            print("Server didn't stop gracefully. Forcing termination.")
            process.terminate()

# Register the shutdown function
signal.signal(signal.SIGINT, shutdown)

# Start Minecraft server
print("Starting Minecraft server...")
java_args = [
    "java", "-Xms6G", "-Xmx12G",  # Reduced memory allocation
    "-jar", SERVER_JAR, "nogui"
]

# Function to handle server output with timestamp
def output_reader(process):
    global running
    start_time = time.time()
    while running:
        line = process.stdout.readline()
        if line:
            elapsed_time = time.time() - start_time
            print(f"[{elapsed_time:.2f}s] [SERVER] {line.strip()}")
        else:
            time.sleep(0.1)  # Short sleep to prevent CPU overuse

try:
    process = subprocess.Popen(java_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)
    
    # Start threads for handling output and input
    output_thread = threading.Thread(target=output_reader, args=(process,))
    input_thread = threading.Thread(target=input_handler, args=(process,))
    
    output_thread.start()
    input_thread.start()
    
    # Wait for the process to complete
    process.wait()
    
    # Signal threads to stop
    running = False
    
    # Wait for threads to finish
    output_thread.join()
    input_thread.join()

except KeyboardInterrupt:
    shutdown(None, None)

except Exception as e:
    print(f"An error occurred: {e}")
    shutdown(None, None)

print("Minecraft server has stopped.")

# Clean up ngrok tunnel if it was used
if tunnel_service == "ngrok":
    ngrok.kill()
