<p align="center"><a href="https://colab.research.google.com/github/Ravylcy/MineColab/blob/master/MineColab.ipynb"><img src="https://github.com/thecoder-001/MineColab/blob/master/Logo.png" alt="Logo" height="130"/></a></p>
<h1 align="center">MineColab</h1>
<p align="center">Forked By LBY_L and then Forked by veeink</p>
<p align="center">Run Minecraft Server on Google Colab</p>
<p align="center"><a href="https://colab.research.google.com/github/LBY-L/MineColab/blob/master/MineColab_forked_by_LBY.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Logo" height="30"/></a></p>

# Description
`MineColab is a script that allows you to run a Minecraft server on Google Colab. It leverages the power of Google Colab's computing resources to host and manage your Minecraft server.`

# Getting Started
`Follow the steps below to use the script:`

1. Put your ngrok authkey and run the cell by pressing `SHIFT + ENTER.`

2. If you encounter the error "Error: Unable to access jarfile server.jar," perform the following
 ・Go to https://drive.google.com/ and open the folder named "Minecraft-colab-(YOUR_SUFFIX)"
 (replace (YOUR_SUFFIX) with your specific suffix).
 ・Download the server software JAR file of your choice and upload it to the folder.

3. Run the script cell again, and it should successfully start the Minecraft server.

4. To obtain the server IP address, follow these steps:
 ・Go to your ngrok tunnels at https://dashboard.ngrok.com/tunnels/agents.
 ・Locate the currently running tunnel and click on it.
 ・Scroll down to the "Tunnel Forwards to" section and copy the address. The format should be similar to 0.tcp.ap.ngrok.io:12345.

# Known Limitations
`While using MineColab, please be aware of the following limitations of the script I forked:`

1. JAR files won't be automatically downloaded by the script. You need to manually upload the desired server software JAR file to the designated folder.
2. There is no built-in server software selector. You have to manually choose and upload the specific server software JAR file.
3. Version selection functionality is currently not available. You will need to ensure that the uploaded server software JAR file matches the desired Minecraft version.
Feel free to contribute to the project and make improvements to address these limitations.
 
