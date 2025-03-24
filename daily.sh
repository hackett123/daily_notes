DIR=$(dirname "$(realpath "$0")")
vim $(python3 $DIR/daily.py) -c "Prose" # Prose is a custom function I have that utilizes https://github.com/junegunn/goyo.vim?tab=readme-ov-file
