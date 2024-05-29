from google.colab import drive
drive.mount('/content/drive')
%cd "/content/drive/MyDrive/Minecraft-server-forge"
!echo "eula=true" > eula.txt

#@title Run the server
#@markdown #### Enter the name of your server jar:
JarName = "start_server.bat" #@param {type:"string"}
#@markdown #### Choose the tunneling service:
TunnelService = "ngrok" #@param ["ngrok", "playit"]
#@markdown #### If you selected Ngrok, provide your Ngrok Auth Token:
NgrokAuthToken = "20etqRLRX3IOsPDfoGrlMGO6VHV_7ULxc8b7VGupNfhJjMfzN" #@param {type:"string"}

from google.colab import drive
from IPython.core.display import display, HTML, clear_output
import subprocess
import time
import os

def update_progress_bar(progress):
    out.update(progress_bar(progress, 100))

def sleep_and_clear_output(seconds):
    time.sleep(seconds)
    clear_output()

def console():
    display(HTML(''))

# Mount Google Drive
drive.mount('/content/drive')

sleep_and_clear_output(0)

# Change directory to the Minecraft server folder on Google Drive
!mkdir -p "/content/drive/MyDrive/Minecraft-server-forge"
%cd "/content/drive/MyDrive/Minecraft-server-forge"

sleep_and_clear_output(0)

# Install Java Versions (8, 17)
!sudo apt update &>/dev/null && echo "apt cache successfully updated" || echo "apt cache update failed, you might receive stale packages"
!sudo apt-get install openjdk-17-jre-headless &>/dev/null && echo "OpenJDK 17 has been installed successfully." || echo "Failed to install OpenJDK 17."
!sudo apt-get install openjdk-8-jre-headless &>/dev/null && echo "OpenJDK 8 has been installed successfully." || echo "Failed to install OpenJDK 8."

sleep_and_clear_output(0)

# Display the Starting server text
display(HTML('<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://github.com/LBY-L/MineColab/blob/master/COLAB-26-11-2022.png?raw=true" alt="COLAB-26-11-2022.png" width="327" height="91" /></p>'))

def progress(value, max=100):
    return HTML("""
        <progress
            value='{value}'
            max='{max}',
            style='width: 100%'
        >
            {value}
        </progress>
    """.format(value=value, max=max))

out = display(progress(0, 100), display_id=True)

# Start the server
subprocess.run(["python", "-c", "'while True:pass'"])
if TunnelService == "ngrok":
    !pip -q install pyngrok &>/dev/null
    from pyngrok import conf, ngrok
    # Set ngrok authtoken
    !ngrok authtoken $NgrokAuthToken &>/dev/null
    # Set default ngrok region
    conf.get_default().region = "ap"  # Change to your closest region
    # Connect to ngrok
    url = ngrok.connect(25565, 'tcp')
    print('Your server address is ' + ((str(url).split('"')[1::2])[0]).replace('tcp://', ''))
    sleep_and_clear_output(3)
    console()

# Create eula.txt
!echo "eula=true" > eula.txt

# Generate configuration files by running the Forge Server Starter JAR
!java -jar minecraft_server_v3.5.7.jar

# Modify the server_starter.conf if needed
with open('server_starter.conf', 'a') as f:
    f.write('''\
# Additional configurations can be added here
java_path=/usr/lib/jvm/java-17-openjdk-amd64/bin/java
    ''')

# Ensure the start_server.bat is executable (if needed)
!chmod +x start_server.bat
