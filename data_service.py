import os
data = []
def load(name):
    """
    This methods create and load a new data for journal
    :param name: name of fifle to loead
    :return:    this return a list of items from this named file
    """
    filename = get_file_name("hover_text")
    with open(filename,"r") as fin:
        for e in fin:
            data.append(e)
    return data

def saving(text):
    filename = get_file_name("hover_text")
    with open(filename,"w") as fout:
        for e in entry:
            fout.write(e)
    print("Saved")
def add_entry(text):
    data.append(text)

def get_file_name(file):
    filename = os.path.abspath(os.path.join('.','data',f"{file}.txt"))
    return filename