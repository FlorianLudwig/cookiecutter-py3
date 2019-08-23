#!/bin/sh
set -e

echo "# install dependencies"
pipenv install --dev

echo "# start backend"
pipenv run adev runserver {{ cookiecutter.project_slug }} -p 8000
