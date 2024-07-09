import os

defualt_config = [
    "theme=light",
]

class ConfigEditor:
    def __init__(self, file_path):
        self.config = {}

        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                for line in defualt_config:
                    file.write(f"{line}\n")
        with open(file_path, "r") as file:
            for line in file:
                key, value = line.split("=")
                self.config[key] = value

    def get_config(self, key):
        try:
            return self.config[key]
        except KeyError:
            return {}
    
    def set_config(self, key, value):
        self.config[key] = value

    def save_config(self, file_path):
        with open(file_path, "w") as file:
            for key, value in self.config.items():
                file.write(f"{key}={value}\n")

if __name__ == "__main__":
    None