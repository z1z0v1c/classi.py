# ***classi.py*** 🐾


**classi.py** is a lightweight Python script for automating file organization within a specified directory. Categorizes files based on their extensions and takes input and output directories as command line arguments.

#### *(Under development)*
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/z1z0v1c/sorti.py/python-package.yml?branch=master)
![GitHub last commit](https://img.shields.io/github/last-commit/z1z0v1c/sorti.py)
![GitHub issues](https://img.shields.io/github/issues/z1z0v1c/sorti.py)
![License](https://img.shields.io/badge/license-Unlicense-blue)


## Features 

- **Automated File Organization**: Sorts files into directories based on their extensions.
- **Customizable Configuration**: Define directory names and file extensions in a `config.ini` file.
- **Cross-Platform Compatibility**: Runs on Windows, macOS, and Linux.
- **Simple and Lightweight**: Minimal dependencies for quick setup and execution.

## Getting Started

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/z1z0v1c/classi.py.git
   cd classi.py
   ```

2. **Create a Virtual Environment (Optional but Recommended)**:

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Unix or MacOS
   ```

3. **Install Dependencies**:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Usage

Run the script from the project's root directory using the following command:

```bash
python project.py
```

The script will read the `config.ini` file and organize files in the current directory accordingly.

Command line arguments:

```
--input, -i               Path to the input directory
--output, -o              Path to the output directory
--recursive, -r           Recursively organize subdirectories
--delete-duplicates, -d   Delete duplicate files
```

To run the unit tests execute the following command:

```bash
pytest test_classi.py
```

## Configuration

The script utilizes a `config.ini` file to determine sorting rules. Below is a sample configuration:

```ini
[Code]
extensions = .py,.go,.c

[Documents]
extensions = .txt,.pdf,.docx

[Pictures]
extensions = .jpg,.png,.svg
```

In this example, files with `.py`, `.go` and `.c` extensions will be moved to the `Code` directory, `.txt`, `.pdf` and `.docx` to `Documents`, and `.jpg`, `.png` and `.svg` to `Pictures`.


## File Structure

```plaintext
classi.py/
├── config.ini           # Configuration file for sorting rules
├── classi.py            # Main script for file organization
├── README.md            # Project documentation
├── requirements.txt     # List of dependencies
└── test_classi.py       # Test cases for the script
```

## Contributing

Contributions are welcome!   Feel free to fork the repository and submit a pull request for improvements or bug fixes. 
For questions or suggestions, please open an [issue](https://github.com/z1z0v1c/sorti.py/issues).

#### *Happy organizing!* 🐾
