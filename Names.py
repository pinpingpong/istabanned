DB_PATH = "name_list.txt" # Edit this when we need to
import pdb

class Names:
    def __init__(self):
        self.path = DB_PATH

    def check_if_name_exists(self, name):
        with open(self.path, "r") as f:
            for line in f:
                if line.strip("\n") == name:
                    return True
        return False

    def add_name(self, name):
        # checks if name exists in the database. 
        # Adds name to db if doesnt yet exist.
        # Returns true if name added successfully.
        if not self.check_if_name_exists(name):
            f = open(self.path, "a")
            f.write(name + "\n")
            f.close()
            return True
        else:
            return False
    
    def delete_name(self, target):
        result = False
        
        with open(self.path, "r") as f:
            names = f.readlines()
        
        output = []
        
        for name in names:
            if name.strip("\n") != target:
                output.append(name) 
            else:
                result = True
        
        f = open(self.path, 'w')
        f.writelines(output)
        f.close()
        
        return result

    