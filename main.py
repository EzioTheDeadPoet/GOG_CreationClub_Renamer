import os
import json

if __name__ == '__main__':
    with open("filename_index.json") as json_file:
        filename_index = json.load(json_file)
        for filename_index_pair in filename_index:
            try:
                os.rename(
                    filename_index_pair.get("input_name"),
                    filename_index_pair.get("output_name")
                )
                print("File "
                      + filename_index_pair.get("input_name")
                      + " renamed to "
                      + filename_index_pair.get("output_name"))
            except FileNotFoundError:
                print("File " + filename_index_pair.get("input_name") + " not found")
