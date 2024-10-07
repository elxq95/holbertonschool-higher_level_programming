import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error while serializing: {e}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError) as e:
            print(f"Error while deserializing: {e}")
            return None

# Testing the deserialization error handling
def test_corrupt_file():
    # Create a valid object and serialize it
    valid_obj = CustomObject("Jane", 30, False)
    valid_filename = "valid_obj.pickle"
    valid_obj.serialize(valid_filename)

    # Test loading from a valid file
    deserialized_obj = CustomObject.deserialize(valid_filename)
    if deserialized_obj:
        deserialized_obj.display()

    # Test loading from a corrupt or nonexistent file
    BAD_FILENAME = "corrupt_or_empty_file.pickle"
    deserialized_obj = CustomObject.deserialize(BAD_FILENAME)

if __name__ == "__main__":
    test_corrupt_file()
