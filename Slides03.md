
# Step 3

# Finding Meaning

## `find` in 3 steps

> 1. Starting at location *X*
> 2. Recursively find all entries that match
> 3. Do something for each match

## Example

```
~ $ find //myserver/myshare/logs/000[4-9] -name \*.dat -newer logchecker.csv \
    -exec /home/myuser/Sandbox/FileCheckers/logchecker \{\} \;
```

> 1. Starting at `//myserver/myshare/logs/000[4-9]`
> 2. Find all files that end in `.dat`
> 3. That are also newer than `logchecker.csv`
> 4. Execute `logchecker`, passing in path to file

## What's with the backslashes?

```
~ $ find //myserver/myshare/logs/000[4-9] -name \*.dat -newer logchecker.csv \
    -exec /home/myuser/Sandbox/FileCheckers/logchecker \{\} \;
```

Backslashes prevent "shell expansion"

## Useful `find` tests

* **`-executable`** - the file is executable or the directory is searchable
* **`-group <gname>`** - file belongs to group *gname*
* **`-iname <pattern>`** - case-insensitive name search
* **`-name <pattern>`** - case-sensitive name search
* **`-newer <file>`** - newer than *file*
* **`-size <n>`** - file uses *n* units of space
    * various measures like 512-byte blocks (`b`) through gigabytes (`G`).
* **`-type <c>`** - file is of type *c*
    * two most common - `d` (directory) or `f` (file).
* **`-user <uname>`** - file is owned by *uname*.

## Useful `find` actions

* **`-delete`** - deletes any files matched so far
    * Actions are also tests (predicates)
    * Don't put this first!
* **`-exec` and `-execdir`** - executes a command or script
* **`-print`** - prints the full path of the found file or directory
* **`-printf`** - prints a formatted string, useful for reports

## `find -printf`

```
~ $ find . -type f -printf "%p\n%u\n%TY-%Tm-%TdT%TT\n\n"
./a
myuser
2015-10-21T11:02:51.7014527000
```