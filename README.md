# Void Package Lookup

# Install
Install requests package and put the vpl file inside your desired bin file.

## Introduction

The Void Package Lookup is a command-line tool designed to retrieve information from Void Linux package templates hosted on the official [Void Package Github](https://github.com/void-linux/void-packages) page

## Arguments
- `-s, --search <package-name>`: This will prompt you to use a search parameter, "version" for example.
- `-p, --package <package-name>`: Retrieves the full template file.
- `-m, --makedepends <package-name>`: Returns the makedepends.
- `-c, --checksum <package-name>`: Returns the package checksum.
- `-v, --version <package-name>`: Returns the package version number.
- `-d, --distfiles <package-name>`: Returns the package distfiles.
- `-k, --keywords <package-name>`: Prints common keywords to use with the `-s, --search` argument.
