# lsdet

Command line tool to display detailed file listings including size of directories and multiple layers of inner-directories.

For help use `lsdet help`.

By default the tool displays one layer of subdirectories and their sizes:
```
C:\Users\Owner\Desktop>lsdet
34 GB  .
    34 GB  Phone Transfer
    176 MB temp
    35 MB  Minecraft Server
    6 MB   HyperRogue
    3 kB   lsdet
```

Using the flags provided you can display both files and directories:
```
C:\Users\Owner\Desktop>lsdet only_dirs=false
34 GB  .
    34 GB  Phone Transfer
    176 MB temp
    35 MB  Minecraft Server
    6 MB   HyperRogue
    1 MB   hah_tg_edit.jpg
    3 kB   lsdet
    450 B  desktop.ini
    222 B  Factorio.url
    0 B    test.txt
```

You can display more layers of subdirectories:
```
C:\Users\Owner\Desktop>lsdet max_depth=2
34 GB  .
    34 GB  Phone Transfer
        16 GB  Movies
        7 GB   Camera
        7 GB   Australia
        1 GB   Old Phone
        915 MB Australia 2
        7 MB   ToDrive
        4 MB   OpenCellSim
        3 MB   Photo editor
        0 B    Contacts
    176 MB temp
        176 MB temp
    35 MB  Minecraft Server
        5 MB   world
        5 kB   logs
    6 MB   HyperRogue
    3 kB   lsdet
```

You can display detailed byte counts:
```
C:\Users\Owner\Desktop>lsdet detailed_bytes=true
34499205791 B .
    34279464254 B Phone Transfer
    176910856 B temp
    35375475 B Minecraft Server
    6081641 B HyperRogue
    3443 B lsdet
```