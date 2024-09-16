import yaml

class Config:
    def __init__(self):
        self.max_diagnostic_messages = 500  # Default value
        self.date_format = "%d/%m/%Y %H:%M:%S"  # Default date format
        self.diagnostic_colors = { # Default colors
            'default': 'white',
            'FC0': 'yellow',
            'FC1': 'orange',
            'FC2': 'red'
        }

    def load_settings(self, file_path: str):
        """
        Load the settings from a YAML file.
        :param file_path: The path to the settings file
        """
        with open(file_path, 'r') as file:
            settings = yaml.safe_load(file)
        
        self.max_diagnostic_messages = settings.get('max_diagnostic_messages', self.max_diagnostic_messages)
        self.date_format = settings.get('date_format', self.date_format)
        self.diagnostic_colors = settings.get('diagnostic_colors', self.diagnostic_colors)