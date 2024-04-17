          _____                    _____                    _____            _____                    _____                    _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \          /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\____\        /::\    \                /::\    \                /::\____\                /::\    \                /::\    \                /::\    \        
       /::::\    \               \:::\    \              /:::/    /       /::::\    \              /::::\    \              /:::/    /               /::::\    \              /::::\    \              /::::\    \       
      /::::::\    \               \:::\    \            /:::/    /       /::::::\    \            /::::::\    \            /:::/   _/___            /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/\:::\    \               \:::\    \          /:::/    /       /:::/\:::\    \          /:::/\:::\    \          /:::/   /\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \               \:::\    \        /:::/    /       /:::/__\:::\    \        /:::/__\:::\    \        /:::/   /::\____\        /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
   /::::\   \:::\    \              /::::\    \      /:::/    /       /::::\   \:::\    \       \:::\   \:::\    \      /:::/   /:::/    /       /::::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \   
  /::::::\   \:::\    \    ____    /::::::\    \    /:::/    /       /::::::\   \:::\    \    ___\:::\   \:::\    \    /:::/   /:::/   _/___    /::::::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \  
 /:::/\:::\   \:::\    \  /\   \  /:::/\:::\    \  /:::/    /       /:::/\:::\   \:::\    \  /\   \:::\   \:::\    \  /:::/___/:::/   /\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\ 
/:::/  \:::\   \:::\____\/::\   \/:::/  \:::\____\/:::/____/       /:::/__\:::\   \:::\____\/::\   \:::\   \:::\____\|:::|   /:::/   /::\____\/:::/__\:::\   \:::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    |
\::/    \:::\   \::/    /\:::\  /:::/    \::/    /\:::\    \       \:::\   \:::\   \::/    /\:::\   \:::\   \::/    /|:::|__/:::/   /:::/    /\:::\   \:::\   \::/    /\:::\   \:::\   \::/    /\::/    \:::\  /:::|____|
 \/____/ \:::\   \/____/  \:::\/:::/    / \/____/  \:::\    \       \:::\   \:::\   \/____/  \:::\   \:::\   \/____/  \:::\/:::/   /:::/    /  \:::\   \:::\   \/____/  \:::\   \:::\   \/____/  \/_____/\:::\/:::/    / 
          \:::\    \       \::::::/    /            \:::\    \       \:::\   \:::\    \       \:::\   \:::\    \       \::::::/   /:::/    /    \:::\   \:::\    \       \:::\   \:::\    \               \::::::/    /  
           \:::\____\       \::::/____/              \:::\    \       \:::\   \:::\____\       \:::\   \:::\____\       \::::/___/:::/    /      \:::\   \:::\____\       \:::\   \:::\____\               \::::/    /   
            \::/    /        \:::\    \               \:::\    \       \:::\   \::/    /        \:::\  /:::/    /        \:::\__/:::/    /        \:::\   \::/    /        \:::\   \::/    /                \::/____/    
             \/____/          \:::\    \               \:::\    \       \:::\   \/____/          \:::\/:::/    /          \::::::::/    /          \:::\   \/____/          \:::\   \/____/                  ~~          
                               \:::\    \               \:::\    \       \:::\    \               \::::::/    /            \::::::/    /            \:::\    \               \:::\    \                                  
                                \:::\____\               \:::\____\       \:::\____\               \::::/    /              \::::/    /              \:::\____\               \:::\____\                                 
                                 \::/    /                \::/    /        \::/    /                \::/    /                \::/____/                \::/    /                \::/    /                                 
                                  \/____/                  \/____/          \/____/                  \/____/                  ~~                       \/____/                  \/____/                                  
 

This application organizes files in a specified directory into folders based on their extensions. It supports a variety of file types including images, videos, documents, 3D files, zipped files, and more.

Prerequisites
Before you begin, ensure you have the following installed:

Python (3.7 or higher)
PyInstaller
Tkinter (usually comes with Python)
You can install Python from here and PyInstaller using pip:

bash
Copy code
pip install pyinstaller
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/file-sorter.git
cd file-sorter
Usage
Run the Script Directly

You can run the script directly using Python:

bash
Copy code
python GUI_sort_files.py
This will open the GUI where you can interact with the application.

Build the Executable

To build an executable so you can run the application without a Python installation:

bash
Copy code
pyinstaller --onefile --windowed GUI_sort_files.py
This command will generate a single executable file in the dist directory inside your project folder.

Running the Executable

Navigate to the dist directory.
Double-click on GUI_sort_files.exe to launch the application.
How to Use the Application
Open the Application: Double-click on the executable or run the Python script.
Select the Directory:
Click the "Durchsuchen..." button to browse and select a directory.
Alternatively, you can manually enter the path in the text field provided.
Start Sorting:
Click the "Sortieren" button to start sorting the files into folders based on their extensions.
The application will create new folders within the selected directory to organize the files.
Completion:
Once the sorting is complete, a pop-up will appear summarizing the actions taken (e.g., which files were moved to which folders).
Rebuilding the Executable
If you make changes to the Python script and want to update the executable:

Open your Command Line Interface and navigate to the project directory.

Run PyInstaller:

bash
Copy code
pyinstaller --onefile --windowed GUI_sort_files.py
This will update the .exe file in the dist directory.

Troubleshooting
PyInstaller Not Found: If you encounter an error stating that PyInstaller is not found, make sure that the Python Scripts folder is in your PATH environment variable.
Tkinter Issues: If the GUI does not start, ensure that Tkinter is installed correctly on your system. This can typically be checked by running python -m tkinter from your Command Line Interface.
Support
For support, create an issue in the GitHub repository, and someone will assist you as soon as possible.

Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please ensure to update tests as appropriate.

Feel free to customize this README according to your application's needs and specific details! This template provides a general structure for an open-source project hosted on GitHub, including instructions for installation, usage, and contribution.

___  ___ _____ _____   ___ 
|  \/  ||____ |  _  | /   |
| .  . |    / /\ V / / /| |
| |\/| |    \ \/ _ \/ /_| |
| |  | |.___/ / |_| \___  |
\_|  |_/\____/\_____/   |_/

