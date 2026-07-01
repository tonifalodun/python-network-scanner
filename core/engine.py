#I Toni Falodun certify this file is my work. I did not use AI at any step of developing, modifying or debugging this code
#March 17, 2026

from network.network_client import check_target
import datetime

class Engine:
    def __init__(self, datastore):
        self.datastore = datastore
    def run(self):
        for target in self.datastore.targets:
            target.status = check_target(target.name)
            #create engine log file in log folder
            f = open("logs/engine.log", "a")
            #get timestamp
            timestamp = datetime.datetime.now()
            #write a line to the log file with time stamp, target name, simulated status
            line = (f"{timestamp}, {target.name}, {target.status} \n")
            f.write(line)


