
# Step 6

# `vi`

## Why `vi`?

> * Use `nano` if available
> * But `vi` is (almost) ***always*** there
> * Good to know the basics "just in case"

## `vi` strangeness

`vi` is a "modal" editor

> * In "command" mode to start
> * Need to go into "insert mode" to insert new text
> * Confusing to almost everyone at first

## `vi` commands

> * `d` - "delete"
> * `b` - "jump 'back' one 'word'"
> * `i` - enter "insert" mode
> * `ESC` - exit "insert" mode
> * `dw` - "delete 'word'"
> * `3dw` - "delete 3 'words'"

## Get me out of here!

> * `:q!` - exit without saving
> * `u` - "undo" command
> * `3u` - "undo" last three changes
> * `view` - "read-only" version of `vi`

## Navigating

> * Arrow and page keys ***tend*** to work right
>     * Except in insert mode!
> * `0` - jump to beginning of line
> * `$` - jump to end of line
> * `w` - jump forward a "word"
> * `b` - jump backward a "word"
> * `:0` - jump to beginning of file
> * `G` - jump to end of file

## I've been searching

> * `/foo` - find "foo" from cursor forward
> * `?foo` - find "foo" from cursor backward
> * `n` - find next instance of last search
> * `p` - find previous instance of last search

## Insertion

All of the following enter "insert mode":

> * `i` - at cursor
> * `I` - at beginning of line
> * `A` - "append" at end of line
> * `o` - insert line below (lowercase) current line
> * `O` - insert line above (uppercase) current line
> * `ESC` - exit insert mode

## Ctrl-X

> * `d` - "delete" is same as "cut"
> * `dd` - delete/cut current line
> * `3dw` - delete/cut three "words"

## Ctrl-C

> * `y` - "yank" is the same as "copy"
> * `yy` - yank/copy current line
> * `3yw` - yank/copy three "words"

## Ctrl-V

> * `p` - paste contents of buffer at cursor
> * `P` - paste contents of buffer above (uppercase) current line
> * `u` - remember "undo" when you need it!

## "X" marks the spot

You can constrain the lines you want to affect by a command by "marking" a
"range":

> 1. Mark line with `m` command followed by a character
> 2. Mark another line with `m` command, but
***with a different label character***
> 3. Use the `'` character to reference a label
> 4. `:'m,'ns/This/That/`

## Invoking external commands

> * `:1,$!sort`
> * `:'m,'n!sort`