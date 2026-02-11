class XYZ:
    def print_string(self, yurt):
       print("greetings", yurt)
       self.yurt = yurt
    
    # when the class is instantiated, this will run
    def __init__(self, x = 1, y = 2, z = 3):
        print("hi")
        a = x 
        b = y
        c = z
        print(a, b, c)    

def main():
    dunder = XYZ() # object instantiation

    dunder.print_string(9)

if __name__ == "__main__":
    main()