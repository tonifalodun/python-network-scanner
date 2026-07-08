#import json module and datetime for timestamps
import json
from datetime import datetime

def create_result(targets):
    #empty list to store formatted results
    results = []
    #loop through each target
    for target in targets:
        #convert each target to dictionary with the fields
        results.append({"name": target.name, "status": target.status, "timestamp": datetime.now().isoformat()})#add timestamp

    return results

def save_result_json(targets):
    results = create_result(targets)
    #define the output path to the Output folder
    output_file_path = "output/result.json"
    #open file in write mode and save results as JSON file
    with open(output_file_path, "w") as file:
        json.dump(results, file, indent=4)
