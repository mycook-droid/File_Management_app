import os
sample = "sample.txt"


def create_file(filename):
    try:
        with open(filename, "x") as f:
            print(f"File named {filename} created successfully")
    except FileExistsError:
        print(f"{filename} already exists!")
    except Exception as e:
        print("An error occurred")


def view_all_files():
    files = os.listdir()
    if not files:
        print("No file Found")
    else:
        print("Files in Directory \n")
        for file in files:
            print(file)


def remove_files(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print(f"File {filename} dont exist")
    except Exception as e:
        print("An Error Occurred")


def read_files(filename):
    try:
        with open(sample, "r") as f:
            content = f.read()
            print(f"Content of {filename}: \n{content}")
    except FileNotFoundError:
        print(f"File {filename} dont exist")
    except Exception as e:
        print("An Error Occurred")


def edit_files(filename):
    try:
        with open(sample, "a") as f:
            content = input(f"Enter updated Content Down - \n")
            f.write(content + "\n")
            print(f"Content added to {filename}")
    except FileNotFoundError:
        print(f"File {filename} dont exist")
    except Exception as e:
        print("An Error Occurred")

def main():
    while True:
        print("-------------FILE MANAGEMENT--------------")
        print("1. Create File\t\t\t\t\t4. Edit File\n"
              "2. View all File\t\t\t\t5. Read File\n"
              "3. Delete File\t\t\t\t\t6. Exit app\n")

        choice = int(input("Enter your choice [1-6] : "))

        if choice == 1:
            filename = input("Enter Filename to create - ")
            create_file(filename)
        elif choice == 2:
            view_all_files()
        elif choice == 3:
            filename = input("Enter Filename to Delete - ")
            remove_files(filename)
            print(f"{filename} deleted !!")
        elif choice == 4:
            filename = input("Enter Filename to Edit - ")
            edit_files(filename)
        elif choice == 5:
            filename = input("Enter Filename to Read - ")
            read_files(filename)
        elif choice == 6:
            exit("Thanks For Visiting")
            break
        else:
            print("Invalid choice")
if __name__ == '__main__':
    main()
