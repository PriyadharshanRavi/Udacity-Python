import os

def rename_files():
    fileslst = os.listdir(r"C:\Users\Priyadharshan\Downloads\Programs\Python\Secret_message")
    print(fileslst)
    saved_path = os.getcwd()
    print (saved_path)
    os.chdir(r"C:\Users\Priyadharshan\Downloads\Programs\Python\Secret_message")
    for filename in fileslst:
        print("old name - " +filename)
        os.rename(filename, filename.strip("0123456789"))
        print("new name - " +filename.strip("0123456789"))
    os.chdir(saved_path)

rename_files()
