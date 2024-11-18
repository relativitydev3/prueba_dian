
import hashlib # hash SHA-384 




InvoiceAuthorization= 18760000001
StartDate='19-01-2019'
EndDate='19-01-2030'
Prefix='SETP'
From=990000000
To=995000000
ProviderID='nit de la empresa'
SoftwareID='e3a8f8f7-f15b-45cd-be14-a9ca652fe569'
pin=12345
texto = f'{SoftwareID}{pin}'
hash_obj = hashlib.sha384(texto.encode())
SoftwareSecurityCode=hash_obj.hexdigest()
QRCode='''NroFactura=SETP990000002
								NitFacturador=800197268
								NitAdquiriente=900108281
								FechaFactura=2019-06-20
								ValorTotalFactura=14024.07
								CUFE=941cf36af62dbbc06f105d2a80e9bfe683a90e84960eae4d351cc3afbe8f848c26c39bac4fbc80fa254824c6369ea694
								URL=https://catalogo-vpfe-hab.dian.gov.co/Document/FindDocument?documentKey=941cf36af62dbbc06f105d2a80e9bfe683a90e84960eae4d351cc3afbe8f848c26c39bac4fbc80fa254824c6369ea694&amp;partitionKey=co|06|94&amp;emissionDate=20190620'''
    
