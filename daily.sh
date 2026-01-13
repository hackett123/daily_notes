DIR=$(dirname "$(realpath "$0")")
nvim $(python3 $DIR/daily.py)
