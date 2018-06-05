File_Search_Engine
====

Authors:
---------------
Shiksha Rawat

Pranjal Yadav

File List:
----------

1.config.txt

2.transfer_files.py

3.ui.py


How to run file:
-----------------

Once you have cloned the directory to your local machine in the default directory as per the operating system,follow the directions below:

1.Run the transfer_files.py.

2.Run ui.py.

3.Type the name of the file whose path you want to find in the entry box.The code tries to give the closest output even if you have entered incomplete file name or words of file name are randomly placed or the file name is not spelled correctly.

4.Click on "Search Path" button.

5.If you have entered the file name along with its extension, then the path of the most probable files will appear as output.

6.Else,you are required to choose the type of file you are searching for,and then the path of the most prabable file will appear as output.

How the Project Works:
---
The first.py file sits on the download folder and on being executed send the files to one of the folders among documents,pictures,videos and projects according to their extensions.

Group of extensions which will be placed in a particular folder is listed down in config.txt file.

After transfering files to the respective folders,run ui.py.If the name of the entered file contains extensions then as per the extension by using os.walk we try finding the path in the required folder.

If the entered file name does not contain extension then the user is required to select the type of type he/she is searching for.Further search is done in the folder based upon the choice of the user. 
