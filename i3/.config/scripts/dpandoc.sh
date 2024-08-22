#!/bin/bash

# generate latex file from mardwon
# usage:
#   ./docker_pandoc.sh latex LinkPrediction.md
#
# NOTE: use just the file name, not the actual path
# (omit the ../)
if [ "$1" = "latex" ]; then
  docker run --rm --volume "$(dirname `pwd`):/data" --user `id -u`:`id -g` \
      pandoc/latex --pdf-engine=lualatex -f markdown -s $2 -o latex/tmp.tex
fi

# generate PDF file from Markdown 
# usage:
#   ./docker_pandoc.sh pdf LinkPrediction.md
#
if [ "$1" = "pdf" ]; then
    docker run --rm --volume "`pwd`:/data" --user `id -u`:`id -g` pandoc/latex --pdf-engine=lualatex -f markdown -s $2 -o out.pdf
fi
