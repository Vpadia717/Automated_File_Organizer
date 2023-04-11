# File Sorter

This Python script is designed to help you quickly and easily organize files in a directory based on their file type. The `organize_junk` function takes no arguments and works by scanning the current directory for files and then moving them to their respective subdirectories based on their file type.

### Usage

To use this script, simply place it in the directory you wish to organize and run it using Python 3. You can do this by opening a terminal or command prompt window, navigating to the directory, and running the following command:

```Python
python main.py
```

The script will then scan the directory for files and move them to the appropriate subdirectory based on their file type. If a subdirectory for a particular file type does not exist, the script will create it.

### Supported File Types

This script supports the following file types:

* HTML
* Images (JPEG, JPG, TIFF, GIF, BMP, PNG, BPG, SVG, HEIF, PSD)
* Videos (AVI, FLV, WMV, MOV, MP4, WEBM, VOB, MNG, QT, MPG, MPEG, 3GP)
* Documents (OXPS, EPUB, PAGES, DOCX, DOC, FDF, ODS, ODT, PWI, XSN, XPS, DOTX, DOCM, DOX, RVG, RTF, RTFD, WPD, XLS, XLSX, PPT, PPTX)
* Archives (A, AR, CPIO, ISO, TAR, GZ, RZ, 7Z, DMG, RAR, XAR, ZIP)
* Audio (AAC, AA, DVF, M4A, M4B, M4P, MP3, MSV, OGG, OGA, RAW, VOX, WAV, WMA)
* Text (TXT, IN, OUT)
* PDF
* Python (PY, IPYNB)
* XML
* Executables (EXE)
* Shell Scripts (SH)
* C (C, CPP)

### Customization

If you would like to add or remove file types or directories, you can do so by editing the `DIRECTORIES` dictionary at the top of the `organize_junk` script. Simply add or remove file extensions and directory names as desired.

### Contributing
Contributions to File Sorter are welcome. If you find any bugs or have suggestions for new features, please submit an issue on the project's GitHub repository. Pull requests are also welcome.

### License
`File Sorter` is licensed under the [MIT license](https://github.com/Vpadia717/File_Sorter/LICENSE). See the LICENSE file for details.
