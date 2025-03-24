# README

## Daily Notes

Daily notes is an app inspired by a plugin I use for work in the Obsidian app. In Obsidian, I can hit cmd+p and type "daily", and it will open a tab with a note for the current date. If it doesn't exist yet, it will create one.

This script does the same thing, but for your local filesytem.

## Behavior

After invoking the `daily` alias, you will enter a vim buffer that was created for today's date. If the file already exists, it won't overwrite anything.

Here is the daily directory structure after I run my `daily` alias
```
 ❯ tree ~/daily
/home/michael/daily
└── 2025
    └── March
        └── 23.md
```

### Details

daily.py will get the current date (in your timezone by default) and make the correct file. It outputs the path to the file, which is fed into vim, so invoking the `daily.sh` script will both make the correct file (if it DNE) and enter a vim buffer for you (for me).


Directory structure:

~/daily/Year/Month/Day
  - month is spelt out
  - year is 4 digits
  - day is 2 digits and is a file

### Add alias

Modify this based on your shell.

```sh
echo "alias daily=\"sh `pwd`/daily.sh\"" >> ~/.zshrc
```
