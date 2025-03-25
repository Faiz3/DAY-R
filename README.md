# DAY-R
```can't coding```

### How?

1. copy the resource.car file to the DAY-R folder.
2. Run the command `python3 main.py` on the terminal.
```
python3 main.py
```
### Menu?

1. unpack - extract the resource.car file to the resource folder
2. decompile - decompile .lu to .lua
3. pack - repack the extracted file, so resource.car

`Note:
luac.exe to compile .lua extension to .lu
`

### Manual?

unpack:
1. create a folder to store the files to be extracted
2. run the following command
```
corona-archiver.exe -u resource.car folder_name
```

pack:
```
corona-archiver.exe -p folder_name
```

decompile from .lu to .lua:
```
java -jar file_name.lu > file_name.lua
```

compile .lua to .lu:
```
luac.exe -o output_name.lu file_name.lua
```
![script](https://github.com/Faiz3/DAY-R/blob/main/Screenshot%202025-03-25%20063534.png)
