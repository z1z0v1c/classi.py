# **sorti.py** - a file organizer🚀
#### Video Demo:  <URL HERE>
#### Description: 

**sorti.py** is a lightweight Python script designed to automate the organization of files within a specified directory. By categorizing files based on their extensions, it streamlines the process of maintaining a tidy file system.

#### Features:

- **Automated File Organization**: Sorts files into folders based on their extensions.
- **Customizable Configuration**: Easily define sorting rules via a `config.ini` file.
- **Cross-Platform Compatibility**: Runs seamlessly on Windows, macOS, and Linux.
- **Simple and Lightweight**: Minimal dependencies for quick setup and execution.

#### Getting Started:

#### Prerequisites

- Python 3.8 or higher

#### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/z1z0v1c/sorti.py.git
   cd sorti.py
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

#### Usage instructions:

Run the script from the project's root directory using the following command:

```bash
python project.py
```

The script will read the `config.ini` file and organize files in the current directory accordingly.

Also, additional command line options can be provided. Below is the full list:

```
--input, -i               Path to the input directory
--output, -o              Path to the output directory
--recursive, -r           Recursively organize subdirectories
--delete-duplicates, -d   Delete duplicate files
```

To run the unit tests from the test file run the following command:

```bash
pytest test_project.py
```

#### Configuration:

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


####  Project File Structure:

```plaintext
sorti.py/
├── config.ini           # Configuration file for sorting rules
├── project.py           # Main script for file organization
├── README.md            # Project documentation
├── requirements.txt     # List of dependencies
└── test_project.py      # Test cases for the script
```

*Happy organizing!*
