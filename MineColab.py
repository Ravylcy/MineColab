from google.colab import drive
drive.mount('/content/drive')
%cd "/content/drive/MyDrive/Minecraft-server-java"
!echo "eula=true" > eula.txt

from google.colab import drive
drive.mount('/content/drive')
%cd "/content/drive/MyDrive/Minecraft-server-java"
!echo "eula=true" > eula.txt

#@title Run the server
#@markdown #### Enter the name of your server jar:
JarName = "server" #@param {type:"string"}
#@markdown #### Choose the tunneling service:
TunnelService = "ngrok" #@param ["ngrok", "playit"]
#@markdown #### If you selected Ngrok, provide your Ngrok Auth Token:
NgrokAuthToken = "" #@param {type:"string"}
#@markdown #### Choose the region where your Minecraft server will be hosted:
NgrokRegion = "ap" #@param ["us", "eu", "ap", "au", "sa", "jp", "in", "None"]

from google.colab import drive
from IPython.core.display import display, HTML, clear_output
import subprocess
import time

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
!mkdir "/content/drive/MyDrive/Minecraft-server-java"
%cd "/content/drive/MyDrive/Minecraft-server-java"

sleep_and_clear_output(0)

# Install Java Versions (8, 17)
!sudo apt update &>/dev/null && echo "apt cache successfully updated" || echo "apt cache update failed, you might receive stale packages"
!sudo apt-get install openjdk-17-jre-headless &>/dev/null && echo "OpenJDK 17 has been installed successfully." || echo "Failed to install OpenJDK 17."
!sudo apt-get install openjdk-8-jre-headless &>/dev/null && echo "OpenJDK 8 has been installed successfully." || echo "Failed to install OpenJDK 8."

sleep_and_clear_output(0)

# Display the Starting server text
display(HTML('<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://github.com/LBY-L/MineColab/blob/master/COLAB-26-11-2022.png?raw=true" alt="COLAB-26-11-2022.png" width="327" heig<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://github.com/LBY-L/MineColab/blob/master/Starting-Serever-12-12-2022.png?raw=true" alt="Starting-Serever-12-12-2022.png" width="335" height="91" /></p>'))
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
    update_progress_bar(16.7)
    from pyngrok import conf, ngrok
    update_progress_bar(33.4)
    # Set ngrok authtoken
    !ngrok authtoken $NgrokAuthToken &>/dev/null
    update_progress_bar(50.1)
    # Set default ngrok region
    conf.get_default().region = NgrokRegion
    update_progress_bar(66.8)
    # Connect to ngrok
    url = ngrok.connect(25565, 'tcp')
    update_progress_bar(83.5)
    print('Your server address is ' + ((str(url).split('"')[1::2])[0]).replace('tcp://', ''))
    update_progress_bar(100.2)
    sleep_and_clear_output(3)
    console()
    !java -Xmx12G ${server_flags} -Djava.awt.headless=true -jar server.jar nogui
