It is a worm that
  1. implementing worm feature: a)infect and copy; b)spread through local network
  2. it will pop out windows to interact with User: a) dialog; b)ask for string
  3. it will encrpted the file in the current folder by using fernet cryptography
  4. it contains a game called Zork, a text-based adventure game
  5. if the user win, he can get the key and decrypt his file. Otherwise, everything will be deleted
  6. Zork game is in java, and worm is python, so it includes a part of code that could compile and run java code
  7. for running this, we need download this by enter " pip install cryptography" in the terminal

It still has lots of problems:
  1. it can only runs on Mac, because it need to run as administrator, windows do not give us such kind of privilege
  2. it can only encrpt one file, but it can infect all files in the folder
  3. the path of runing zork is fix, we need to manually change it
  4. many documents remains after the user finished the game and that is caused by the encrypt and decrypt method

Notes:
  1. It will only infect the file in the current folder
  2. I limit the power of infection so it won't use spread() method
  3. The infect_files() method will not actually infect, but just add a line of sentences "This file is infected" instead of the code of the worm.
  4. Also, the infected files show with a prefix "infected_fileName"

