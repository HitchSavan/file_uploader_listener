
Tool for listening for the file appearance, automatic SFX packing and uploading to yandex disk.
Using methods from other project "upload_sfx_to_yadisk"

### Settings JSON example

    {
        "default_folder": "/folder_structure", // target folder in ya.disk (upload destination)
        "include_files": [ // files to upload
            "\\file.one",
            "\\file.two"
        ],
        "listen_file_names": [ // part of full file name to listen to
            "filename"
        ],
        "additional_files": [ // files to upload
            "\\file.img",
            "\\folder"
        ]
    }
