# ChangeCase

## Overview

This plugin adds additional case modifications to Sublime Text 2. Note that this plugin modifies the case of text delimited by whitespace.

## Installation
Note with either method, you may need to restart Sublime Text 2 for the plugin to load.

### Package Control
Installation through [package control](http://wbond.net/sublime_packages/package_control) is recommended. It will handle updating your packages as they become available. To install, do the following.

* In the Command Palette, enter `Package Control: Add Repository`
* Enter the following URL into the input box: `https://github.com/skuroda/ChangeCase`
* In the Command Palette, enter `Package Control: Install Package`
* Search for `ChangeCase`

### Manual
Clone or copy this repository into the packages directory. Ensure it is placed in a folder named `ChangeCase`. By default, the Packages directories are located at:

* OS X: ~/Library/Application Support/Sublime Text 2/Packages/
* Windows: %APPDATA%/Roaming/Sublime Text 2/Packages/
* Linux: ~/.config/sublime-text-2/Packages/

## Usage
By default all commands are accessible through the command palette. All commands appear as `ChangeCase: <Command>`

### Commands
#### Title Case
The title case command will capitilize the first character of each word that does not appear in the ignore list. In addition, both parts of hyphenated word will be capitalized (ex. `hello-world` will become `Hello-World`).

## Settings
`title_case_ignore`:

An array containing words to ignore in the title case command.

