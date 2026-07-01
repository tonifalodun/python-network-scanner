#Toni Falodun
#Final Project
#March 17, 2026
#I Toni Falodun certify this file is my work. I did not use AI at any step of developing, modifying or debugging this code

from core.engine import Engine
from data.datastore import TargetList
from core.output_create import save_result_json

def main():
    datastore = TargetList()
    engine = Engine(datastore)
    #run program
    engine.run()

    #save to output folder
    save_result_json(datastore.targets)
if __name__ == "__main__":
    main()