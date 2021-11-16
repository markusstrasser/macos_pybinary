pip3 install -r requirements.txt
pyinstaller -F main.py --clean && dist/main --debug=all