# SourceFilesToSinglePDF

![Version](https://img.shields.io/badge/version-v1.0.0--beta-blue)
![Status](https://img.shields.io/badge/status-beta-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green)

## Introduction
SourceFilesToSinglePDF is a Python tool that allows you to convert files from various extensions into a single PDF document. It provides a convenient way to compile multiple source code files (e.g., Python, HTML, CSS) into a PDF for easy sharing or printing. The tool automatically generates a table of contents with page numbers, making it simple to navigate through the compiled PDF.
Here is an illustrative [sample](https://github.com/Vilnante/SourceFilesToSinglePDF/files/11645248/SourceFilesToSinglePDF.pdf).

## Key Features
- Converts files with extensions like `.py`, `.html`, and `.css` into a single PDF document.
- Generates a table of contents with page numbers for easy navigation.
- Supports multiple files and directories.
- Provides customization options for parameters like folder paths and output file names.

## Supported file formats

Non-exhaustive list of supported extensions: `.py`, `.txt`, `.csv`, `.json`, `.xml`, `.html`, `.css`, `.md`, `.log`, `.yaml`, `.ini`, `.cfg`, `.bat`, `.sh`, `.sql`, `.php`, `.java`, `.cpp`, `.c`, `.h`, `.js`, `.jsx`, `.ts`, `.tsx`, `.rb`, `.pl`, `.r`, `.go`, `.swift`, `.vb`.

## Use Cases

SourceFilesToSinglePDF can be useful in various scenarios, including:
- Sharing code examples or documentation in a single PDF file.
- Creating project reports or documentation that include code snippets.
- Archiving multiple files in a standardized format for easy reference.
- Simplifying the process of printing or distributing code files with proper formatting.
- Investigating and resolving file-related issues either through independent search or with the aid of ChatGPT.

## Installation

### Requirements
Before using SourceFilesToSinglePDF, make sure you have the following requirements:

- Python 3.x installed on your system.

### Steps

To use SourceFilesToSinglePDF, follow these steps:

1. Clone or download the repository from GitHub: [SourceFilesToSinglePDF]([link_to_repository](https://github.com/Vilnante/SourceFilesToSinglePDF/)).
2. Ensure that you have Python 3.x installed on your system.
3. Install the required dependencies by running `pip install reportlab PyPDF2`.
4. Open a terminal or command prompt and navigate to the downloaded repository folder.


## Usage
1. Open the `config_and_launch.py` file in a text editor or in an IDE.
2. Modify the following parameters according to your requirements:
   - `extensions`: Add or remove file extensions as needed.
   - `folder_path`: Set the path to the folder containing the files you want to convert.
   - `output_path`: Specify the desired output path for the generated PDF.
   
   Several examples in the file will help you changing these parameters properly.

   
   Several examples in the file will help you changing these parameters properly.
3. Save the `config_and_launch.py` file.
4. If you are using a terminal, execute the script by running `python config_and_launch.py` after having choosed the SourceFilesToSinglePDF's folder directory with `cd`. Otherwise, if you are using an IDE such as Visual Studio Code or Pyzo, execute the file `config_and_launch.py` **as a script** (usually with the shortcut `CTRL+F5`).
5. Wait for the process to complete. The generated PDF will be saved at the specified `output_path`.

## Example

### Example of extensions and paths
Suppose you have a folder named `code_samples` containing multiple Python files (`example1.py`, `example2.py`) and an HTML file (`index.html`). You want to compile these files into a single PDF.

In the `config_and_launch.py` file, set the `folder_path` to the absolute path of the `code_samples` folder on your system. You can also customize the `output_path` if desired.

```python
extensions = ['.py', '.html']
folder_path = r'/path/to/code_samples'
output_path = r'/path/to/output.pdf'
```

### Some Generated PDF Files

Here are some examples of files generated with this tool:

- [SourceFilesToSinglePDF version b1.0.0 itself](https://github.com/Vilnante/SourceFilesToSinglePDF/files/11645248/SourceFilesToSinglePDF.pdf)
- [Pyzo](https://github.com/Vilnante/SourceFilesToSinglePDF/files/11645249/Pyzo.pdf) (Python editor files. You can find the repository [here](https://github.com/pyzo/pyzo))
- [Better Trade Screen](https://github.com/Vilnante/SourceFilesToSinglePDF/files/11645277/ModCivVI.pdf) (a Sid Meier's Civilization VI mod by astor. You can find it [here](https://steamcommunity.com/sharedfiles/filedetails/?id=873246701))

## Limitations
- SourceFilesToSinglePDF currently supports a predefined set of file extensions. You can modify the `extensions` list in `config_and_launch.py` to add or remove supported extensions.
- The tool relies on the `reportlab` and `PyPDF2` libraries, which should be installed prior to usage.

## Contribution
Contributions to the SourceFilesToSinglePDF are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/Vilnante/SourceFilesToSinglePDF/).

## License
This addon is licensed under the [MIT License](LICENSE).
