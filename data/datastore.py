#I Toni Falodun certify this file is my work. I did not use AI at any step of developing, modifying or debugging this code
#Mach 17, 2026
class Target:
    def __init__(self, name):
        self.name = name

#Create a class that stores a list
class TargetList:
    def __init__(self):
        self.targets = []

        try:
            #open and read the file
            f = open("data/targets.txt", "r")
        #Error handling if file can't be found
        except FileNotFoundError:
            print("File not found")
            return

        for line in f:
            #remove white space from end and beginning of string
            line = line.strip()
            #Create target object
            target = Target(line)
            #Add target to the list
            self.targets.append(target)
