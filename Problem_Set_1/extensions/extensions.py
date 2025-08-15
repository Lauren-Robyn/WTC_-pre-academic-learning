def main():
    file_name = input("File name: ").lower().strip(" ")
    extension_type = get_extensions(file_name)
    print(extension_type)

def get_extensions(file_name):
    if "." in file_name:
        extension = "." + file_name.rsplit(".",1)[-1]
    else:
        extension ="" 
    match extension: 
        case ".gif":
            return "image/gif"
        case ".jpg"|".jpeg":
            return "image/jpeg"
        case ".png":
            return "image/png"
        case ".pdf":
            return "application/pdf"
        case ".zip":
            return "application/zip"
        case ".txt" :
            return "text/plain"
        case _:
            return "application/octet-stream"
        
main()
    
     