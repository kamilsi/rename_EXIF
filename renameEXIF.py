import os
import exifread
import re


path = "Z:/"

dir_list = os.scandir(path)

for entry in dir_list:
    if entry.is_dir():
        # print(entry.path)
        if re.match(r'^\d{4}.\d{2}.\d{2}', entry.name):
            # print("Seems already OK")
            if re.match(r'^\d{4}-\d{2}-\d{2}', entry.name):
                print(entry.path)
                print(path + entry.name.replace("-", " "))
                os.rename(entry.path,
                          path + entry.name.replace("-", " "))
            continue
        file_list = os.scandir(entry.path)
        for subentry in file_list:
            if subentry.name.endswith(('jpg', 'JPG', 'jpeg', 'JPEG')) and subentry.is_file():
                f = open(subentry.path, 'rb')
                tags = exifread.process_file(f, stop_tag='EXIF DateTimeOriginal')
                f.close()
                if 'EXIF DateTimeOriginal' in tags:
                    EXIF_date = str(tags['EXIF DateTimeOriginal']).split(" ")[0].split(":")
                    print(path + EXIF_date[0] + ' ' + EXIF_date[1] +  ' ' + EXIF_date[2] + ' ' + entry.name)
                    os.rename(entry.path,
                              path + EXIF_date[0] + ' ' + EXIF_date[1] + ' ' + EXIF_date[2] + ' ' + entry.name)
                    break
                else:
                    continue

print(dir_list)