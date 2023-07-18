from google.colab import drive
drive.mount('/content/drive')
%cd "/content/drive/MyDrive/Minecraft-server-$suffix"
!echo "eula=true" > eula.txt

from google.colab import drive
drive.mount('/content/drive')
%cd "/content/drive/MyDrive/Minecraft-server-$suffix"
!echo "eula=true" > eula.txt

#@title Run the server
#@markdown #### Choose the suffix of your server folder:
suffix = "colab" #@param ["colab", "cts", "combat", "velocity", "flypvp", "adrip", "rizecookey", "lby", "pvp", "us", "eu", "ap", "au", "sa", "jp", "in"]
#@markdown #### Create a folder named `Minecraft-server-'your prefix'` in your Google Drive and put your server jar in it.
#@markdown #### Enter the name of your server jar:
JarName = "server" #@param {type:"string"}
#@markdown #### Does your server use Paper?
Paper = "Yes" #@param ["Yes", "No"]
#@markdown #### Choose the tunneling service:
TunnelService = "ngrok" #@param ["ngrok", "playit"]
#@markdown #### If you selected Ngrok, provide your Ngrok Auth Token:
NgrokAuthToken = "" #@param {type:"string"}
#@markdown #### Choose the region where your Minecraft server will be hosted:
NgrokRegion = "ap" #@param ["us", "eu", "ap", "au", "sa", "jp", "in", "None"]
#@markdown #### Choose the amount of RAM to allocate (in GB):
RAMAllocation = 8 #@param {type:"slider", min:1, max:8, step:1}
#@markdown #### Enable GPU acceleration
UseGPU = True #@param {type:"boolean"}

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
!mkdir "/content/drive/MyDrive/Minecraft-server-$suffix"
%cd "/content/drive/MyDrive/Minecraft-server-$suffix"

sleep_and_clear_output(0)

# Install Java Versions (8, 17)
!sudo apt update &>/dev/null && echo "apt cache successfully updated" || echo "apt cache update failed, you might receive stale packages"
!sudo apt-get install openjdk-17-jre-headless &>/dev/null && echo "OpenJDK 17 has been installed successfully." || echo "Failed to install OpenJDK 17."
!sudo apt-get install openjdk-8-jre-headless &>/dev/null && echo "OpenJDK 8 has been installed successfully." || echo "Failed to install OpenJDK 8."

sleep_and_clear_output(0)

# Display the Starting server text
display(HTML(''))

def progress_bar(value, max=100):
    return HTML("""
        <progress value='{value}' max='{max}', style='width: 100%'>{value}</progress>
    """.format(value=value, max=max))

out = display(progress_bar(0, 100), display_id=True)

# Start the server
subprocess.run(["python", "-c", "'while True:pass'"])

if UseGPU:
    # Set up GPU runtime
    from tensorflow.python.client import device_lib
    gpu_device_name = [device.name for device in device_lib.list_local_devices() if device.device_type == 'GPU']
    if len(gpu_device_name) > 0:
        print(f'Using GPU: {gpu_device_name[0]}')
    else:
        print('GPU not found. Please check if the runtime type is set to GPU.')
else:
    print('GPU acceleration is disabled.')

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
    !java -Xmx{RAMAllocation}G ${{server_flags}} -jar server.jar nogui

elif TunnelService == "playit":
    !curl -SsL https://playit-cloud.github.io/ppa/key.gpg | sudo apt-key add - &>/dev/null
    update_progress_bar(33.4)
    !sudo curl -SsL -o /etc/apt/sources.list.d/playit-cloud.list https://playit-cloud.github.io/ppa/playit-cloud.list &>/dev/null
    update_progress_bar(66.8)
    !sudo apt update &>/dev/null && sudo apt install playit &>/dev/null && echo "PlayIt installed" || echo "Failed to install PlayIt"
    update_progress_bar(100.2)
    sleep_and_clear_output(3)
    console()
    !playit & java -Xmx{RAMAllocation}G ${{server_flags}} -jar server.jar nogui
