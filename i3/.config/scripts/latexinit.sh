#!/bin/bash

echo "Generating Latex Template 🚀"

mkdir latex && cd latex && \
  wget https://github.com/Typing-Monkeys/MonkeyLatexTemplate/releases/latest/download/template.zip && \
  unzip template.zip && \
  rm template.zip
