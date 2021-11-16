
Run
```
sh setup.sh
```

```
pyinstaller -F main.spec --clean && dist/main --debug=all
```
Apparently  there's some dependency error in the build:

`Error loading ASGI app. Could not import module "main".`