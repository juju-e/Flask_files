# Flask_files
A flask web app that will give the option to upload a text file along with the title

# How it works:

This web app works with sqlite3 as the default database engine,<br>
When the user enters the file and it's title, the app will insert in th database the file's name, the first 100 characters, the title and the time at which the file was uploaded.
I then used templates to display html and all the source code is in main.py.

# How to run it:

To install the needed packages, just type in your termial:
```
$ pip install -r requirements.txt
```
Then to run it:
```
$ python3 main.py

```
It is set in debug mode and will run on port `2000`
<br><br><br><br><br>
Made by `Shadowblade` during `GCI 2019`, Open source
