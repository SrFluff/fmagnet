import zipfile
def read(zipF,readF):
    with zipfile.ZipFile(zipF,"r") as archive:
        cont = archive.read(readF)
        data = cont.decode()
        return data.split("\n")[0:-1]
