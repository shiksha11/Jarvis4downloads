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

3.ui_further_updated.py


How to run file:
-----------------

Once you have cloned the directory to your local machine in the default directory as per the operating system,follow the directions below:

1.Run the transfer_files.py.

2.After transfering files to the respective folders,install python-docx and pyaudio.

3.To insall pyaudio run the command : pip install pyaudio.

4.To install python-docx run the command : pip install pyhton-docx.

5.Run ui_further_updated.py.

6.Input can be given in two ways.Either by tying it in the entry box or as voice input.

7.You can search file either by name or through body search(by typing words in the body of a particlar file.
But the latter works only for .pdf , .csv , .txt , .docx files.

8.Click on "Search Path" button.

9.To give input through entry box : a) Type the input in the entry box.Two options will appear. Click on "Search by filename" or "Body Saerch" as per your input.

10.If you have entered the file name along with its extension, then the path of the most likely files will appear as output.

11.Else,you are required to choose the folder of file you are searching for,and then the path of the most prabable file will appear as output.

12.To give input in the form of audio first press "Give Input In Audio Form".

13.Then speak the file name.

14.Rest of the process is same as for the input given through entry box.

15.While giving input in audio form speak loudly and near the mike of your device.

How the Project Works:
---
The transfer_files.py file sits on the download folder and on execution sends the files to one of the folders among documents,pictures,videos and projects according to their extensions.

Group of extensions which will be placed in a particular folder is listed down in config.txt file.

After transfering files to the respective folders,install python-docx and pyaudio.

If the name of the entered file contains extensions then as per the extension by using os.walk we try finding the path.

If the entered file name does not contain extension then the user is required to select the type of file he/she is searching for.Further search is done in the folder based upon type of file selected by user. 

For body search frequency of the word given as input is calculated in different files and file with highest frequency is returned as output. 
