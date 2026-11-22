import subprocess
import sys
import os

operator = sys.platform

def packet_import(packet_name:list[str]):
    for packet in packet_name:
        process = []
        match operator:
            case "win32":
                process.append(["pip", "install", packet, "--upgrade"])
            case "darwin":
                process.append(["pip3", "install", packet, "--upgrade"])
            case "linux":
                process.append(["pip3", "install", packet, "--upgrade"])
            case _:
                process.append(["pip", "install", packet, "--upgrade"])
        for cmd in process:
            try:    
                subprocess.run(cmd, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Failed to install {packet}: {e}")