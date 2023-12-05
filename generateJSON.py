import json


class NamePair(dict):
    def __init__(self, input_name, output_name):
        dict.__init__(self, input_name=input_name, output_name=output_name)
        self.input_name = input_name
        self.output_name = output_name


if __name__ == '__main__':
    with (open("CC_Steam.md") as cc_files):
        steam_file_names = cc_files.read().splitlines()
        gog_file_names = open("CC_GOG.md").read().splitlines()
        filename_index = []
        i = 0
        for filename in steam_file_names:
            name_pair = NamePair(gog_file_names[i], filename)
            i += 1
            filename_index.append(name_pair)
            with open("filename_index.json", "w") as filename_index_json:
                filename_index_json.write(json.dumps(filename_index, indent=2))
