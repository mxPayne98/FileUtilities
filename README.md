# File Utilities

## Rename File Extension

To rename extension of files in directory from source extension to destination extension run the `convert_extension.py` script.
 ### Usage:
 
```
python ./convert_extenstion.py [options] path [source_extension] [destination_extension] 
```

The program accepts the following 2 option flags:
 - `--all` Rename all files in provided path (Do not provide `source_extension`)
 - `--remove` Remove extension from all files matching `source_extension`
 
 ### Examples:
 
 - Rename all '.txt' files inside dir 'folderA' to '.csv'
```
python ./convert_extenstion.py ./folderA txt csv
```
- Rename all files with any extension inside dir 'folderA' to '.txt'
```
python ./convert_extenstion.py --all ./folderA txt
```
- Remove extension from all '.txt' files inside dir 'folderA'
```
python ./convert_extenstion.py --remove ./folderA txt
```
---
## Convert .xls to .pdf

To convert all .xls files in a directory to .pdf run the `xls_2_pdf.py` script.

**NOTE:** Requires `win32com` package.
 ### Usage:
 
```
python ./xls_2_pdf.py.py [options] path
```

The program accepts the following option flags:
 - `--landscape` Change orientation to landscape (default is potrait)

### Examples:

```
python ./xls_2_pdf.py.py --landscape ./
python ./xls_2_pdf.py.py ./
```