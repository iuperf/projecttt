import subprocess

process1 = subprocess.Popen(["python", "main.py"]) # Create and launch process pop.py using python interpreter
process2 = subprocess.Popen(["python", "discord_bot.py"])
process3 = subprocess.Popen(["python", "vk_group_bot.py"])

process1.wait() # Wait for process1 to finish (basically wait for script to finish)
process2.wait()
process3.wait()