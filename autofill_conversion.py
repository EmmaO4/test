from autofill import Autofill

def main():
    
    while True:
        user_input = input("select option(p/d): ")

        autofill = Autofill()

        autofill.set_format(user_input)

main()

if "__name__" == "__main__":
    main()