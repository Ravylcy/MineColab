<p align="center"><a href="https://colab.research.google.com/github/LBY-L/MineColab/blob/master/MineColab_forked_by_LBY.ipynb"><img src="https://github.com/thecoder-001/MineColab/blob/master/Logo.png" alt="Logo" height="130"/></a></p>
<h1 align="center">MineColab</h1>
<p align="center">Forked By LBY_L and Forked by veeink</p>
<p align="center">Run Minecraft Server on Google Colab</p>
<p align="center"><a href="https://colab.research.google.com/github/LBY-L/MineColab/blob/master/MineColab_forked_by_LBY.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Logo" height="30"/></a></p>

# Guide on Using the script
1. Put your ngrok authkey and run the cell by pressing ``SHIFT + ENTER``
2. When it says "***Error: Unable to access jarfile server.jar***"
 Go to https://drive.google.com/ and open the created folder Minecraft-colab-(YOUR_SUFFIX)
3. Download the server software jar file you desire and upload it in the folder.
4. Run the cell script again and the script should run the minecraft server
5. To get the ip link go to your ngrok tunnels https://dashboard.ngrok.com/tunnels/agents
6. press the tunnel that is currently running
7. Scroll down to "Tunnel    Forwards to"
8. and copy the address.
   Example: 0.tcp.ap.ngrok.io:12345

# There are a few flaws in  this script
1. Jar files wont actually download automatically
2. No server software selector
3. no Version selector

You pretty much have to manually put the jar file in.
