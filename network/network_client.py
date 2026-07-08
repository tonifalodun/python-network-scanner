import subprocess
import platform

def check_target(target_name):
    #perform network check
    system_name = platform.system().lower()
    if system_name == "windows":
        command = ["ping", "-n", "1", target_name]
    else:
        command = ["ping", "-c", "1", target_name]
    try:
        #return up, down, or timeout
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        if result.returncode == 0:
            return "UP"
        else:
            return "DOWN"
    #return result of timeout if ping times out/ catch timeouts
    except subprocess.TimeoutExpired:
        return "TIMEOUT"
    #catch any failed commands
    except Exception:
        return "DOWN"



