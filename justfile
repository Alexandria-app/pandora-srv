set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

# makes the server DISTRIBUTABLE
# IMPORTANT DO NOT USE RELATIVE PATHS LIKE ./app (NO DOTS), IT BREAKS THE GENERATOR
zip:
    puro pub get
    puro dart run serious_python:main package --asset assets/pandora_mobile.zip app/ --mobile
    puro dart run serious_python:main package --asset assets/pandora_desktop.zip app/
