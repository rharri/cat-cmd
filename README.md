## Description
A Python implementation of the GNU Core Utility `cat` command line program. 
This implementation is partial and currently only supports two options,
`-n` and `-b`.

## Requirements
- Python >=3.12

## Examples
```
$ python3 -m cat_cmd cat_cmd/data/file1 cat_cmd/data/file2 
     This is file 1
     
     This is file 1
     This is file 1
     This is file 2
     
     This is file 2
     This is file 2
```
```
$ python3 -m cat_cmd -n cat_cmd/data/file1 cat_cmd/data/file2
     1  This is file 1
     2  
     3  This is file 1
     4  This is file 1
     1  This is file 2
     2  
     3  This is file 2
     4  This is file 2
```
