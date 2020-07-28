#!/bin/bash

echo "Start To Update EY-CONSOLE Tool"

git clone --depth=1 https://github.com/ehs4nnn/EY-Console.git
sudo chmod +x EY-Console/update.sh
bash EY-Console/update.sh
