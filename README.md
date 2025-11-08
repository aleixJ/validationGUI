https://github.com/user-attachments/assets/8288f189-ed67-489f-a98c-ac4abd3bca1c

## Setup

1. Clone the repository
2. Create a virtual environment
   - Anaconda
        ```bash
        conda create -n <env_name> python=3.11.9
        conda activate <env_name>
        pip install -r requirements.txt
        ```
3. Run the application from the root directory
    ```bash
    python .\src\main.py
    ```
## Documentation

### can_model
- `data`: Contains the data in memory received from the CAN bus.
   Is built dynamically in function of the `.dbc` file. The function `setup_data` is used to initialize the structure.
   The class `Utils` contains a method `print_data_structure` to print the data structure withouth the data.
   Example:
   ```
   self.data =
   {
      'Cell_Temperatures': 
      {
         'Cell_Temperature_1': None,
         'Cell_Temperature_2':
         {
            "timestamp": deque(maxlen=3),
            "value": deque(maxlen=3)
         }
	   }
   }
   ```
   'None' until the first message is received.


### Interface

The file interface.ui is the Qt Designer file. It can be opened with the Qt Designer tool to modify the interface.
When the file is modified, it must be converted to a Python file using the following command:
```bash
pyside6-uic ui_index.ui -o ui_index.py
```

