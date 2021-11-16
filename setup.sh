pip3 install -r requirements.txt
pip3 install "uvicorn[standard]"
pyinstaller -F main.py --clean && dist/main --debug=all