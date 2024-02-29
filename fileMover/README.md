# File Organizer

This Python script organizes files in the specified downloads folder into separate folders based on their file extensions. It categorizes files into "Programs" and "University" folders depending on whether they are application files or PDF documents.

## Features
- **Folder Creation:** Automatically creates "Programs" and "University" folders if they do not exist in the specified downloads folder.
- **File Categorization:** Moves files with specific extensions (e.g., .exe, .pdf) into their corresponding folders.
- **Customizable:** Users can customize the file extensions and folder names according to their needs by modifying the script.

## Usage
1. **Setup:** Ensure you have Python installed.
2. **Specify Downloads Folder:** Set the `downloads_folder_path` variable to the path of your downloads folder.
3. **Run the Script:** Execute the script, and it will organize the files in the downloads folder accordingly.

## Example
Suppose the downloads folder contains files with various extensions:
- `example.exe`
- `document.pdf`
- `sample.dmg`
- `report.pdf`

After running the script, the files will be organized as follows:
```
Downloads/
|_ Programs/
   |_ example.exe
   |_ sample.dmg
|_ University/
   |_ document.pdf
   |_ report.pdf
```

## Note
- Customize the `application_extensions` and `pdf_extensions` lists to include additional file extensions as needed.
- Ensure proper permissions to move files in the specified downloads folder.

Feel free to modify and adapt this script to suit your file organization requirements!
