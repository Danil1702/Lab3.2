import twitter2


def read_dictionary(json_info):
    """
    Returns the value of the dictionary by its key.
    Prints the message in case of invalid input
    """
    list_keys = list(json_info.keys())
    print("Your value is a dictionary")
    print(list_keys)
    key = input("Choose the section of the json file from the given: ")
    if key not in list_keys:
        print("Invalid input")
    else:
        return json_info[key]


def read_list(lst):
    """
    Returns the element of the list by its index.
    Prints the message in case of invalid input
    """
    print("Your value is a list")
    length = len(lst)-1
    print("Choose the index of your section range[0:{}]: ".format(length))
    index = int(input())
    try:
        return lst[index]
    except:
        print("Invalid input")    


if __name__ == "__main__":
    acct = input('Enter Twitter Account:')
    try:
        json_info = twitter2.get_json_file(acct)
    except:
        print("Invalid input")  
    info = json_info
    while True:
        if type(info) == dict:    
            new_info = read_dictionary(info)
        elif type(info) == list:
            if len(info) > 1:
                new_info = read_list(info)   
            else:
                print(info)
                break     
        else:
            print(info)
            break
        info = new_info

