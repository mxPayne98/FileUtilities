# File Utilities

## Rename File Extension

To rename extension of files in directory from source extension to destination extension run the the `convert_extension.py` script.
 ### Usage:
 
```
python ./rename_extension.py [options] path [source_extension] [destination_extension] 
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
