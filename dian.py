import hashlib # hash SHA-384 

# Número Resolución
InvoiceAuthorization= 18760000001

# Fecha desde
StartDate='19-01-2019'

# Fecha hasta
EndDate='19-01-2030'

# Prefijo de la autorización de
# numeración de facturación
# dado por el SIE de
# Numeración
Prefix='SETP'

# Rango desde *
# consecutivo de factura
# por cada factura tiene que aumental dinamicamente 
# dinamico---
From=990000000

# Rango hasta *
To=995000000


# nit de la empresa
ProviderID='nit de la empresa'

# id Identificación esta en Información del software de la dian 
# Identificador del software
# habilitado para la emisión de
# facturas
SoftwareID='e3a8f8f7-f15b-45cd-be14-a9ca652fe569'

# pin del software
pin=12345


# SoftwareSecurityCode ------------------------------------------
# Huella del software que autorizó la
# DIAN al Obligado a Facturar
# Electrónicamente o al Proveedor
# Tecnológico para crearlo se ecrita en formato SHA-384  los campo de pin y SoftwareID
SoftwareSecurityCode=hashlib.sha384(f'{SoftwareID}{pin}'.encode()).hexdigest()
# SoftwareSecurityCode ------------------------------------------

# NIT de la DIAN 
AuthorizationProviderID=800197268


# es el QR
QRCode=f'''NroFactura={From}
								NitFacturador={CompanyNit}
								NitAdquiriente={ClientNit}
								FechaFactura={IssueDate}
								ValorTotalFactura={LineExtensionAmount}
								CUFE=941cf36af62dbbc06f105d2a80e9bfe683a90e84960eae4d351cc3afbe8f848c26c39bac4fbc80fa254824c6369ea694
								URL=https://catalogo-vpfe-hab.dian.gov.co/Document/FindDocument?documentKey=941cf36af62dbbc06f105d2a80e9bfe683a90e84960eae4d351cc3afbe8f848c26c39bac4fbc80fa254824c6369ea694&amp;partitionKey=co|06|94&amp;emissionDate=20190620'''

# Indicador del tipo de operación 
# La tabla 13.1.5.1 Tipos de operación, se encuentra en la Caja de Herramientas
# Direcion “Caja_de_herramientas_Factura_Electronica_Validacion_Previa.zip\Anexo Tecnico\Tablas Referenciadas\13.1.5.1”, en formato Excel “.xlsx”
CustomizationID=10

# Versión del Formato: Indicar versión del documento.
# en el 2024 es=  DIAN 2.1
ProfileID='DIAN 2.1'

# La tabla 13.1.1. Ambiente de Destino del Documento cbc ProfileExecutionID y cbc UUID @schemeID, se encuentra en la Caja de Herramientas “Caja_de_herramientas_Factura_Electronica_Validacion_Previa.zip\Anexo Tecnico\Tablas Referenciadas”, en formato Excel“.xlsx” 
# Código que describe el ambiente de destino donde será procesada la validación previa de este documento electrónico
# 1 para producion.
# 2 para pruevas 
ProfileExecutionID=2

# Número de documento
#Incluye prefijo + consecutivo de factura autorizados por la DIAN
iD=f'{Prefix}{From}'

# CUFE: Código Único de
# Facturación Electrónica
# Elemento que verifica la
# integridad de la información
# recibida
# Ejemplo: CUFE de una factura-e de venta: SHA384 ...
# 11.2 Generación de CUFE  ...
uUID=hashlib.sha384(f'{d}{d}{d}'.encode()).hexdigest()

# Fecha de emisión de la factura. Está relacionada con las fechas del DueDate considerando zona horaria
# de Colombia (-5).
# Validación de fecha calendario. La fecha de emisión debe estar en un rango apropiado con respecto a la
# fecha calendario. 
# dinamico---
IssueDate='2019-06-20'

# Hora de emisión: hora de emisión de la factura.
# dinamico---
IssueTime='09:15:23-05:00'

# La tabla 13.1.3 Tipo de Documento, se encuentra en la Caja de Herramientas
# “Caja_de_herramientas_Factura_Electronica_Validacion_Previa.zip\Anexo Tecnico\Tablas Referenciadas”, en formato Excel “.xlsx”
# Referencia a otros documentos.
# Tipo de Factura:
# 01	Factura electrónica de Venta
# 02	Factura electrónica de venta -exportación
# 03	Instrumento electrónico de transmisión – tipo 03
# 04	Factura electrónica de Venta - tipo 04
# 91	Nota Crédito
# 92	Nota Débito
# 96	Eventos (ApplicationResponse)
InvoiceTypeCode='01'

# Información adicional: Texto
# libre, relativo al documento 
#  es opcional
Note='Opcional'

# Divisa de la Factura: Divisa
# aplicable a toda la factura
DocumentCurrencyCode='COP'

# numero de cantidad de producto de la factura.
# Número o cantidad de elementos InvoiceLine de la factura 
# dinamico---
LineCountNumeric=1


# ----------------------------------------------------------
# es el periodo en el que se esta facturando seria el inicio del mes y el fin del mes.
# Fecha de inicio de la autorización de la numeración
InvoicePeriodStartDate ='2019-05-01'
# Fecha final de la autorización de la numeración
InvoicePeriodEndDate='2019-05-30'
# -------------------------------------------------------------


# -------------------------------apartir de aqui ya va la informacion del etabresi,miento y del cliente. ---------------------------------------


# Identificador de tipo de organización jurídica de la organización o persona
# La tabla 13.2.3. Tipo de organización jurídica (Personas Natural y Juridica) cbc AdditionalAccountID, se encuentra en la Caja de Herramientas
# “Caja_de_herramientas_Factura_Electronica_Validacion_Previa.zip\Anexo Tecnico\Tablas Referenciadas”, en formato Excel “.xlsx” 
# Código	Significado
# 1	Persona Jurídica y asimiladas
# 2	Persona Natural y asimiladas
# nota 
# AdditionalAccountID=2

# Nombre comercial del emisor
# Nombre Tienda
ConpanyName='Oasis'

# esta etiqueta no viene en el xml toca ponerlo.
# Corresponde al código de actividad económica CIIU 
# codigo de actuvidad economico que aparece en el rut de la empresa
# Para informar varios códigos, se separan por ; Ejemplo 7020;5140
IndustryClasificationCode='5440'

# Código ''postal'' del municipio
ConpanyPostCode='51686'

# Nombre de la ciudad
ConpanyCity='Bogotá, D.c. '

# Nombre del Departamento
CountrySubentity='Bogotá'

# Código del Departament
# La tabla de 13.4.2 Departamentos ISO 3166-2CO CountrySubentity, CountrySubentityCode, se encuentra en la Caja de Herramientas
# “Caja_de_herramientas_Factura_Electronica_Validacion_Previa.zip\Anexo Tecnico\Tablas Referenciadas”, en formato Excel “.xlsx”.
CountrySubentityCode=11

# Direcion del lugar
CompatyAddress='Av. #97 - 13'

# nombre legar en el rut
# Nombre o Razón Social del emisor
RegistrationName='Oasis'

# nit de la empresa .
# NIT del emisor
CompanyNit='800197268'

# Tipo de Identificador Fiscal de la empresa.
# La tabla 13.2.1 Documento de identificación (Tipo de Identificador Fiscal), se encuentra en la Caja de Herramientas
# “Caja_de_herramientas_Factura_Electronica_Validacion_Previa.zip\Anexo Tecnico\Tablas Referenciadas”, en formato Excel “.xlsx”
# Código	Significado
# 11	Registro civil 
# 12	Tarjeta de identidad 
# 13	Cédula de ciudadanía 
# 21	Tarjeta de extranjería **
# 22	Cédula de extranjería **
# 31	NIT
# 41	Pasaporte 
# 42	Documento de identificación extranjero** 
# 47	PEP (Permiso Especial de Permanencia)
# 48	PPT (Permiso Protección Temporal)
# 50	NIT de otro país***
# 91	NUIP *
customerIdCode=31


# Obligaciones o responsabilidades del contribuyente; incluye el régimen al que pertenece el emisor
# Para el campo: cbc:TaxLevelCode La tabla 13.2.6.1 Responsabilidades fiscales, se encuentra en la Caja de Herramientas
# “Caja_de_herramientas_Factura_Electronica_Validacion_Previa.zip\Anexo Tecnico\Tablas Referenciadas”, en formato Excel “.xlsx”
# Código	Significado
# O-13	Gran contribuyente
# O-15	Autorretenedor
# O-23	Agente de retención IVA
# O-47	Régimen simple de tributación
# R-99-PN	No aplica – Otros *
TaxLevelCode='R-99-PN'

# Código del municipio
# La tabla de 13.4.3 Municipios-CityName, se encuentra en la Caja de Herramientas
# “Caja_de_herramientas_Factura_Electronica_Validacion_Previa.zip\Anexo Tecnico\Tablas Referenciadas”, en formato Excel “.xlsx” 
CityCode='11001'

# Identificador del tributo 
# Para el grupo PartyTaxScheme La tabla de 13.2.6.2. Para el grupo PartyTaxScheme, se encuentra en la Caja de Herramientas
# “Caja_de_herramientas_Factura_Electronica_Validacion_Previa.zip\Anexo Tecnico\Tablas Referenciadas”, en formato Excel “.xlsx” 
# Código	Significado
# 01	IVA
# 04	INC
# ZA	IVA e INC
# ZZ 	No aplica *
TaxSchemeID='01'
TaxSchemeName='IVA'



# -------------------------------------- Informacion del cliente ----------------------------------------------


# Identificador de tipo de persona
# La tabla 13.2.3. Tipo de organización jurídica (Personas Natural y Juridica) cbc AdditionalAccountID, se encuentra en la Caja de Herramientas
# “Caja_de_herramientas_Factura_Electronica_Validacion_Previa.zip\Anexo Tecnico\Tablas Referenciadas”, en formato Excel “.xlsx”
# Código	Significado
# 1	Persona Jurídica y asimiladas
# 2	Persona Natural y asimiladas
# dinamico ---
# toca tener los cliente ya creado en la base de datos con esos codigo
AdditionalAccountID=1

# Grupo con información sobre el nombre del adquiriente 
PartyName='OPTICAS GMO COLOMBIA S A S'

# Código del municipio 
# La tabla de 13.4.3 Municipios-CityName, se encuentra en la Caja de Herramientas
# “Caja_de_herramientas_Factura_Electronica_Validacion_Previa.zip\Anexo Tecnico\Tablas Referenciadas”, en formato Excel “.xlsx”
clientAddress='11001'

# Nombre de la ciudad 
# opcional
clientCity='Bogotá, D.c. '

# Nombre del Departamento
# opcional
clientDepar='Bogotá'

# Código del Departamento
# opcional
ClientCodeDepar='11'

# Elemento de texto libre, que el emisor puede utilizar para poner todas las informaciones de la dirección del adquiriente
ClientAddressLine='CARRERA 8 No 20-14/40'

# Nombre o Razón Social del adquiriente es como aparece en el rut 
ClientRegistrationName='OPTICAS GMO COLOMBIA S A S'

# nit del cliente 
ClientNit='900108281'
# -------------------------------------- /Fin Informacion del cliente ----------------------------------------------



# ---------------  Grupo de campos para información relacionadas con el pago de la factura.-----------------------------

# Formas de pago
# La tabla de 13.3.4.1. Formas de Pago cbc PaymentMeans ID, se encuentra en la Caja de Herramientas
# “Caja_de_herramientas_Factura_Electronica_Validacion_Previa.zip\Anexo Tecnico\Tablas Referenciadas”, en formato Excel “.xlsx”
# Código	Significado
# 1	Contado
# 2	Crédito
PaymentMeansID=1

# Código correspondiente al medio de pago
# Definición de los atributos del elemento, La tabla 13.3.4.2 Medios de Pago PaymentMeansCode, se encuentra en la Caja de Herramientas
# “Caja_de_herramientas_Factura_Electronica_Validacion_Previa.zip\AnexoTecnico\Tablas Referenciadas”, en formato Excel “.xlsx”.
PaymentMeansCode=10



# Valor del tributo 
# valor de la factura ante del iva
# Suma de todos los elementos ../cac:TaxTotal/TaxSubtotal/
TaxAmountToal=12600.06

# Grupo de información que definen los valores del tributo
# precio de cada pproducto.
TaxAmount=[12600.06]

# total de la sumatoria de los productos
# Total Valor Bruto antes de tributos: Total valor bruto, suma de los valores brutos de las líneas de la factura.
LineExtensionAmount=12600.06


# ----------------------------------------------- datos del producto------------------------------------------

# Número de Línea 
# numero del producto
# dinamico --
InvoiceLineID=1

# Cantidad del producto o servicio
InvoicedQuantity=[1.000000]

# Válida la Unidad de Medida de la cantidad del artículo solicitado Ver lista de valores posibles en 0  Notificación si el valor del atributo no se  encuentra en la columna “Unid”
# La tabla 13.3.6 Unidades de Cantidad @unitCode, se encuentra en la Caja de Herramientas
# “Caja_de_herramientas_Factura_Electronica_Validacion_Previa.zip\Anexo Tecnico\Tablas Referenciadas”, en formato Excel “.xlsx”
InvoicedQuantityunitCode='EA'

# Valida Valor total de la línea.
# El Valor Total de la línea es igual al
# producto de Cantidad x Precio Unidad
# menos Descuentos más Recargos
# que apliquen para la línea.
LineExtensionAmountProduc=12600.06

# Grupo de información que describen las
# características del artículo o servicio 
# nombre
DescriptionProduc=['AV OASYS -2.25 (8.4) LENTE DE CONTATO']

# Código del vendedor correspondiente al
# artículo debe ser informado
SellersItemIdentificationID='AOHV84-225'


# Valor del artículo o servicio
PriceAmount=[18900.00]

# La cantidad real sobre la cual el precio aplica 
BaseQuantity=1.000000



