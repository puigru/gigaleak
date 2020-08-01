# Gigaleak documentation

This repository aims to document every file found in the leaks of July 24th and 25th, 2020, commonly known as the "gigaleak".

The file structure of this repository mirrors that of the leaked archives. However, files instead contain metadata in YAML format.

This can then be built into a JSON file listing all of the files and their description in a tree-like fashion which can be useful when learning about these files.

## Contributing

Going through all these files is a very time-consuming task, so any contributions are welcome.

### Windows

Windows places [many restrictions](https://docs.microsoft.com/en-us/windows/win32/fileio/naming-a-file#naming-conventions) on allowed filenames. These archives often do not abide by these restrictions, so this repository cannot be checked out as-is.

I strongly recommend using the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to avoid running into issues.

If you must, you can clone the repository as such:

* `git clone -n https://github.com/XXLuigiMario/gigaleak.git`

Make sure you have Python installed and the `pyyaml` package:

* `pip install -U pyyaml`

Download the [latest release](https://github.com/XXLuigiMario/gigaleak/releases/latest) to the repository folder, then:

* `git config core.sparseCheckout true`
* `(echo /* & echo !other.7z) >.git\info\sparse-checkout`
* `git checkout`
* `python expand.py build.json .`
* `echo /* >.git\info\sparse-checkout`
* `git read-tree HEAD`

Or alternatively:

*Note: This will not check out the rest of the repository.*

* `git checkout HEAD expand.py`
* `python expand.py build.json .`
* `git reset`

Despite errors, this should leave the repository in a usable state. If you check `git status`, you will see that any files which did not follow the aforementioned naming convention are marked as deleted.

Be mindful of only including modified files when staging your changes!

## Building

Clone the repository and then run:

* `pip install pyyaml`
* `./build.py other.7z build.json`
