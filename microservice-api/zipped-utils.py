
import zipfile
import ssl
import certifi
from urllib.request import urlopen
def myCompressFileLocal():
    #TODO -> el primer parametro va la ruta del archivo en local
    myZip = zipfile.ZipFile('myZip.zip', 'w')
    myZip.write('myFile.txt', compress_type=zipfile.ZIP_DEFLATED)
    myZip.close()

def myCompressFileWeb():
    #TODO -> ruta donde esta alojado el archivo
    request = "https://docs.aws.amazon.com/es_es/whitepapers/latest/aws-overview/aws-overview.pdf"
    #se agrega certificado para acceder al archivo en la nuhe
    response = urlopen(request, context=ssl.create_default_context(cafile=certifi.where()))
    # TODO -> el primer parametro va la ruta del archivo en local
    myZip = zipfile.ZipFile('myZip.zip', 'w')
    #TODO -> el nombre debe llevar la misma extension del archivo sino deja un archivo plano en bytecode
    myZip.writestr("aws-overview.pdf",response.read(), compress_type=zipfile.ZIP_DEFLATED)
    myZip.close()