import json
import os

class JMetadata:
    def __init__(self, file_path):
        """
        Initialize the JMetadata with a file path.
        
        :param file_path: Path to the JSON file.
        """
        self.file_path = file_path
        # Load existing data from file or initialize with an empty dictionary
        self.data = self._load_data()

    def _load_data(self):
        """
        Load data from the JSON file.
        
        :return: Dictionary loaded from the JSON file or an empty dictionary if file does not exist.
        """
        if not os.path.exists(self.file_path):
            return {}
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def _save_data(self):
        """
        Save the current data to the JSON file.
        """
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def read(self, key=None):
        """
        Read a value from the JSON data.

        :param key: Optional key to retrieve a specific value. If None, return the whole data.
        :return: Value associated with the key, or the entire data if key is None.
        """
        if key is None:
            return self.data
        return self.data.get(key)

    def write(self, key, value):
        """
        Write a new value to the JSON data or update an existing value.

        :param key: Key under which the value will be stored.
        :param value: Value to be stored.
        """
        self.data[key] = value
        self._save_data()

    def update(self, key, value):
        """
        Update an existing value in the JSON data.

        :param key: Key for which the value will be updated.
        :param value: New value to be updated.
        :raises KeyError: If the key does not exist.
        """
        if key not in self.data:
            raise KeyError(f"Key '{key}' does not exist in the JSON data.")
        self.data[key] = value
        self._save_data()

    def delete(self, key):
        """
        Delete a key-value pair from the JSON data.

        :param key: Key to be deleted.
        :raises KeyError: If the key does not exist.
        """
        if key not in self.data:
            raise KeyError(f"Key '{key}' does not exist in the JSON data.")
        del self.data[key]
        self._save_data()

    def get_nested(self, path):
        keys = path.split('.')
        for key in keys:
            if isinstance(self.data, dict) and key in self.data:
                self.data = self.data[key]
            else:
                return None
        return self.data

    def set_nested(self, path, value):
        keys = path.split('.')
        last_key = keys.pop()
        current = self.data
        
        for key in keys:
            if key not in current:
                current[key] = {}
            current = current[key]
        
        current[last_key] = value

    def delete_nested(self, path):
        keys = path.split('.')
        last_key = keys.pop()
        current = self.data
        
        for key in keys:
            if key not in current:
                return
            current = current[key]
        
        if last_key in current:
            del current[last_key]



"""

# Usage examples
print('Original JSON self.data:', json.dumps(json_self.data, indent=2))

# Add a new node
set_nested_dict(json_self.data, 'user.address.city', 'New York')
print('After adding a new node:', json.dumps(json_self.data, indent=2))

# Update an existing node
set_nested_dict(json_self.data, 'user.computer.model', 'e7450')
print('After updating a node:', json.dumps(json_self.data, indent=2))

# Delete a node
delete_nested_dict(json_self.data, 'user.computer.model')
print('After deleting a node:', json.dumps(json_self.data, indent=2))

"""