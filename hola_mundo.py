from qgis.core import import *

QgsApplication.setPrefixPath("/path/to/qgis/installation", True)

qgs = QgsApplication([], False)

qgs.initQgis()

qgs.exitQgis()
