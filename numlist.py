import readline
from os.path import isfile


print("Enter a number and it will be added to the list")
print("Type \"help\" for list of commands")
arr = []


def help_message():
    file = open("/usr/bin/numlist_files/help.txt", "r")
    file_contents = file.read()
    print(file_contents)
    file.close()


def find_value(x):
    for i in range(len(arr)):
        if x == arr[i]:
            return i


def is_number(num):
    try:
        number = float(num)
        arr.append(number)
    except ValueError:
        print("List empty or invalid command!")


def export_list(dir):
    file = open(dir, "x")
    for i in range(len(arr)):
        if i > 0:
            file.write("\n" + str(arr[i]))
        else:
            file.write(str(arr[i]))
    file.close()


def import_list(dir):
    file = open(dir, "r")
    lines = file.readlines()
    valerror = False
    count = 0
    error_line = []
    for line in lines:
        count += 1
        try:
            arr.append(float(line))
        except ValueError:
            valerror = True
            error_line.append(count)
    if valerror:
        print("line", count, "is invalid")
    file.close()


input_history = []
current_input_index = 0
while True:
    user_input = input("> ")

    if user_input:
        input_history.append(user_input)
        
    if len(input_history) > 1:
        readline.set_startup_hook(lambda: readline.insert_text(input_history[current_input_index]))
        
    if user_input == "" and current_input_index > 0:
        current_input_index -= 1
    elif user_input == "" and current_input_index == 0:
        current_input_index = len(input_history) - 1
    else:
        current_input_index = len(input_history)

    if user_input == "help":
        help_message()
    elif user_input == "exit":
        break
    elif user_input.startswith("im"):
        dir = user_input.lstrip("im ")
        if isfile(dir):
            import_list(dir)
        else:
            print("File does not exist or cannot be opened")
    elif arr != []:
        if user_input == "ls":
            print(arr)
        elif user_input.startswith("rm"):
            rmvalue = user_input.lstrip("rm ")
            try:
                rmvalue = int(rmvalue)
                arr.remove(rmvalue)
            except ValueError:
                print("Not a valid number to remove")
        elif user_input == "clear":
            arr = []
        elif user_input == "a":
            total = 0
            for i in range(len(arr)):
                total = total + arr[i] 
            print(total)
        elif user_input == "m":
            total = 1
            for i in range(len(arr)):
                total = total * arr[i]
            print(total)
        elif user_input == "ra":
            if arr != []:
                arr_temp = sorted(arr)
                print(arr_temp[len(arr_temp)-1] - arr_temp[0])
        elif user_input == "ma":
            action = "mean"
        elif user_input == "o":
            print(sorted(arr))
        elif user_input == "l":
            print(sorted(arr)[len(arr)-1])
        elif user_input == "s":
            print(sorted(arr)[0])
        elif user_input.startswith("ex"):
            dir = user_input.lstrip("ex ") + ".txt"
            if isfile(dir) == False:
                print("\"" + dir + "\"" + " created")
                export_list(dir)
            else:
                print("File already exists")
        else:
            is_number(user_input)
    else:
        is_number(user_input) 
