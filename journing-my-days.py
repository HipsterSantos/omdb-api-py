import data_service
def print_heaer():
    print("_______________________")
    print("     Journing app")
    print("_______________________")
def run_event_loop():
    print("What do you want to do ?")
    cmd = None
    while cmd != 'x':
        cmd = input("Choose between [L]ist , [A]add , E[x]it:")
        cmd = cmd.lower().strip()
        if cmd == 'l':
            listing()
        elif cmd == 'a':
            adding()

def listing():
    for item in enumerate(data_service.load()):
        print('listing items--', item)
def adding():
    text_to_save = input("item to add in the list")
    data_service.saving(text_to_save)
    print("item add ")
def main():
    print_heaer()
    run_event_loop()

main()