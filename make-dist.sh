#!/bin/bash
git pull
python version.py -b
python setup.py sdist upload -r https://:5550/pypi/
git add .
git commit -m "up bot devop не стабильная"
git push