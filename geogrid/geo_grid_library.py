# --------------------------------------------------------
#    geo_grid_library - geogrid operation functions
#
#    begin                : 14 Feb 2016
#    copyright            : (c) 2016 by Konstantin Puzankov
#    email                : konst555@mail.ru
#
#   GEOGRID is free software and is offered without guarantee
#   or warranty. You can redistribute it and/or modify it 
#   under the terms of version 2 of the GNU General Public 
#   License (GPL v2) as published by the Free Software 
#   Foundation (www.gnu.org).
# --------------------------------------------------------

import io
import csv
import sys
import time
import math
import urllib
import os.path
import operator
import tempfile

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from math import *

# --------------------------------------------------------
#    GEOGRID Functions
# --------------------------------------------------------


# --------------------------------------------------------
#    make_geogrid - Grid shapefiles creation
# --------------------------------------------------------

def make_geogrid(qgis, savename, dLon, dLat, MinLon, MinLat, MaxLon, MaxLat,
                       n_brdminuts, n_subgrd, n_brdtik, n_lblminuts, addlayer):
  if len(savename) <= 0:
    return "No output filename given"

  # Выходные файлы
  outFeatures  = savename
  # убрать расширение если есть
  if (outFeatures[-4] == "." ) : outFeatures = outFeatures[:-4]
  out_grd = outFeatures + "_grd.shp"
  out_brd = outFeatures + "_brd.shp"
  out_tik = outFeatures + "_tik.shp"
  out_lbl = outFeatures + "_lbl.shp"


                                            
  #==== Используемая координатная система ====== географическая на WGS84
  crsWGS = QgsCoordinateReferenceSystem(4326)
#  crsWGS = QgsCoordinateReferenceSystem()
#  crsWGS.createFromProj4("+proj=longlat +datum=WGS84 +no_defs")

  #=========================================================
  #=================== Построение сетки ====================
  #=========================================================
  
  # Cell size
  cW = float(dLon)
  cH = float(dLat)

  # Выравнивание на первую линию
  minX = float( (int((MinLon+180)/cW)+1)*cW - 180 )  
  minY = float( (int((MinLat+90 )/cH)+1)*cH - 90  )
  maxX = float(MaxLon)
  maxY = float(MaxLat)  
  
  # SubStep
  ssX = float(n_subgrd)
  ssY = float(n_subgrd)
  
#  QMessageBox.information(None, "Info"," minX="+unicode(minX)+" minY="+unicode(minY)+
#                                       " maxX="+unicode(maxX)+" maxY="+unicode(maxY)+
#                                       " cW="+unicode(cW)+" cH="+unicode(cH) )
  try:
      fields = QgsFields()
      fields.append(QgsField("Line_XY", QVariant.Int, "int", 24, 16, "Line_XY"))
      fields.append(QgsField("Line_d", QVariant.Int, "int", 24, 16, "Line_d"))
      fields.append(QgsField("Line_m", QVariant.Int, "int", 24, 16, "Line_m"))
      fields.append(QgsField("nswe", QVariant.String, "text", 2, 0, "nswe"))

      if QFile(out_grd).exists():
        if not QgsVectorFileWriter.deleteShapeFile(out_grd):
          return "Failure deleting existing shapefile: " + out_grd

      shapetype = QGis.WKBLineString

      outfile = QgsVectorFileWriter(out_grd, "utf-8", fields, shapetype, crsWGS);

      if (outfile.hasError() != QgsVectorFileWriter.NoError):
          return "Failure creating output shapefile: " + unicode(outfile.errorMessage())

#          QMessageBox.information(None, "Info"," 1") 
#          QMessageBox.information(None, "Info"," 21") 
#          QMessageBox.information(None, "Info"," 3") 
#          QMessageBox.information(None, "Info"," 4") 
#          QMessageBox.information(None, "Info"," 2  "+ unicode(( (maxY-minY)/(cH/ssY) )) ) 

      #================================================== 
      #=============== Make Longitude lines, by X =======
      #================================================== 
      for i in range( int( (maxX-minX)/cW ) +1 ):
          polyline = []
          #== Дополнительная точка до рамки
          if ( minY > (MinLat + 0.001) ):
              polyline.append(QgsPoint(float(minX+cW*i),float( MinLat)))

          for j in range( int( (maxY-minY)/(cH/ssY) ) ):
              polyline.append(QgsPoint( (minX+cW*i), (minY+(cH/ssY)* j)    )) 
              polyline.append(QgsPoint( (minX+cW*i), (minY+(cH/ssY)*(j+1)) ))

          #== Дополнительная точка до рамки
          if ( MaxLat > (minY+(cH/ssY)*(j+1)) ):
              polyline.append(QgsPoint( float(minX+cW*i), float(MaxLat)) )

          feature = QgsFeature()
          feature.setGeometry(QgsGeometry.fromPolyline(polyline))
          pX  = minX+cW*i 
          pXd = int(abs(pX))
          pXm = int( (abs(pX)-pXd + 0.00001)*60 )
          pX_ew = "E"
          if (pX<0) : pX_ew = "W"

          feature.setAttributes([ 0, pXd, pXm, pX_ew ])
          outfile.addFeature(feature)

      #================================================== 
      #=============== Make Latitude lines, by Y =======
      #================================================== 
      for j in range( int( (maxY-minY)/cH ) +1 ): 
          polyline = []
          #== Дополнительная точка до рамки
          if ( minX > (MinLon + 0.001) ):
              polyline.append(QgsPoint(MinLon, (minY+cH*j)))

          for i in range( int( (maxX-minX)/(cW/ssX) ) ): 
              polyline.append(QgsPoint( (minX+(cW/ssX)* i ),   (minY+cH*j) ))
              polyline.append(QgsPoint( (minX+(cW/ssX)*(i+1)), (minY+cH*j) ))

          #== Дополнительная точка до рамки
          if ( MaxLon > (minX+(cW/ssX)*(i+1)) ):
              polyline.append(QgsPoint( MaxLon, (minY+cH*j) ))

          feature = QgsFeature()
          feature.setGeometry(QgsGeometry.fromPolyline(polyline))

          pY  = minY+cH*j 
          pYd = int(abs(pY))
          pYm = int( (abs(pY)-pYd + 0.00001)*60 )
          pY_ns = "N"
          if (pY<0) : pY_ns = "S"

          feature.setAttributes([ 1, pYd, pYm, pY_ns ])
          outfile.addFeature(feature)
  
  except Exception as e:
      return e.message
  # Закрытие файла и удаление ссылки на него
  del outfile


  #=========================================================
  #=================== Построение рамки ====================
  #=========================================================

  # Cell size
  cW = float(n_brdminuts)/60.0
  cH = float(n_brdminuts)/60.0
 
  # Рамка по всей области с точностью до минут
  # Выравнивание 
  minX = float( (int((MinLon+180)/cW)+1)*cW - 180 )  
  minY = float( (int((MinLat+90 )/cH)+1)*cH - 90  )
  maxX = float(MaxLon)
  maxY = float(MaxLat)  

  # SubStep
  ssX = 1.0
  ssY = 1.0
  
  #=============== Make List of coordinates (ID, X, Y) ========
  coordsList = []

  # Xmin - by Y - side 1
  Last_ID = 1  
  odd_id = 0
  #== Дополнительная точка 
  if ( minY > MinLat ):
      coordsList.append([Last_ID, MinLon, MinLat, odd_id])
  for j in range( int( (maxY-minY)*(60.0/n_brdminuts) )+1 ):
      coordsList.append([Last_ID, MinLon, (minY+(cH/ssY)* j ), odd_id])
      if odd_id == 0 : odd_id = 1
      else : odd_id = 0 
  #== Дополнительная точка 
  if ( minX > MinLon ):
      coordsList.append([Last_ID, MinLon, MaxLat, odd_id])
  odd_id1 = odd_id
          
  # Ymax - by X -side 2
  Last_ID = 2
  odd_id = 0
#        #== Дополнительная точка 
#        if ( minX > MinLon ):
#            coordsList.append([Last_ID, MinLon, MaxLat, odd_id])
  for i in range( int( (maxX-minX)*(60.0/n_brdminuts) )+1 ):
      coordsList.append([Last_ID, (minX+(cW/ssX)* i ), MaxLat, odd_id])
      if odd_id == 0 : odd_id = 1
      else : odd_id = 0 
  #== Дополнительная точка 
  if ( (minX+(cW/ssX)* i) < MaxLon ):
      coordsList.append([Last_ID, MaxLon, MaxLat, odd_id])
  odd_id2 = odd_id
  
  # Xmax - by Y - side 3
  Last_ID = 3
  odd_id = odd_id1
  for j in range( int( (maxY-minY)*(60.0/n_brdminuts) ), -1,-1 ):
      coordsList.append([Last_ID, MaxLon, (minY+(cH/ssY)* j ), odd_id])
      if odd_id == 0 : odd_id = 1
      else : odd_id = 0 
  #== Дополнительная точка 
  if ( minY > MinLat ):
      coordsList.append([Last_ID, MaxLon, MinLat, odd_id])
          
  # Ymin - by X -side 4
  Last_ID = 4
  odd_id = odd_id2
  for i in range( int( (maxX-minX)*(60.0/n_brdminuts) ), -1,-1 ):
      coordsList.append([Last_ID, (minX+(cW/ssX)* i ), MinLat, odd_id])
      if odd_id == 0 : odd_id = 1
      else : odd_id = 0 
  #== Дополнительная точка 
  if ( minX > MinLon ):
      coordsList.append([Last_ID, MinLon, MinLat, odd_id])


  #============== Создание и запись shape ============
  try:
      fields = QgsFields()
      fields.append(QgsField("sideID", QVariant.Int, "int", 24, 16, "sideID"))
      fields.append(QgsField("odd", QVariant.Int, "int", 24, 16, "odd"))

      if QFile(out_brd).exists():
        if not QgsVectorFileWriter.deleteShapeFile(out_brd):
          return "Failure deleting existing shapefile: " + out_brd

      shapetype = QGis.WKBLineString

      outfile = QgsVectorFileWriter(out_brd, "utf-8", fields, shapetype, crsWGS);

      if (outfile.hasError() != QgsVectorFileWriter.NoError):
          return "Failure creating output shapefile: " + unicode(outfile.errorMessage())


      # Initialize a variable for keeping track of a feature's ID.
      for i in range(len(coordsList)-1): 
          side_ID =coordsList[i+1][0]
          odd_id =coordsList[i+1][3]

          polyline = []
          polyline.append(QgsPoint(coordsList[i][1], coordsList[i][2]))
          polyline.append(QgsPoint(coordsList[i+1][1], coordsList[i+1][2]))
          feature = QgsFeature()
          feature.setGeometry(QgsGeometry.fromPolyline(polyline))
          feature.setAttributes([ side_ID, odd_id ])
          outfile.addFeature(feature)


      # ================ Угловые точки ==============
      coordsList = []
      minX = MinLon  
      minY = MinLat
      maxX = MaxLon
      maxY = MaxLat  

      coordsList.append([11, minX+(cW/ssX), minY, 2])
      coordsList.append([11, minX, minY, 2])
      coordsList.append([11, minX, minY+(cH/ssY), 2])

      coordsList.append([22, minX, maxY-(cH/ssY), 2])
      coordsList.append([22, minX, maxY, 2])
      coordsList.append([22, minX+(cW/ssX), maxY, 2])

      coordsList.append([33, maxX-(cW/ssX), maxY, 2])
      coordsList.append([33, maxX, maxY, 2])
      coordsList.append([33, maxX, maxY-(cH/ssY), 2])

      coordsList.append([44, maxX, minY+(cH/ssY), 2])
      coordsList.append([44, maxX, minY, 2])
      coordsList.append([44, maxX-(cW/ssX), minY, 2])

      # Initialize a variable for keeping track of a feature's ID.
      for j in range(4):
          i = j*3 
          side_ID =coordsList[i][0]
          odd_id =coordsList[i][3]  
          
          polyline = []
          polyline.append(QgsPoint(coordsList[i][1], coordsList[i][2]))
          polyline.append(QgsPoint(coordsList[i+1][1], coordsList[i+1][2]))
          polyline.append(QgsPoint(coordsList[i+2][1], coordsList[i+2][2]))
          feature = QgsFeature()
          feature.setGeometry(QgsGeometry.fromPolyline(polyline))
          feature.setAttributes([ side_ID, odd_id ])
          outfile.addFeature(feature)

  except Exception as e:
      return e.message
  # Закрытие файла и удаление ссылки на него
  del outfile

  #=========================================================
  #=================== Построение тиков ====================
  #=========================================================

  # Рамка и тики по всей области с точностью до минут
  minX = float(MinLon)  
  minY = float(MinLat)
  maxX = float(MaxLon)
  maxY = float(MaxLat)  
  

  
  # ================== Первый набор тиков ==============
  # === с заданным шагом от 1 минуты 
  # SubStep
  ssX = 1.0
  ssY = 1.0

  # Cell size
  cW = float(n_brdtik)/(60.0*ssX) 
  cH = float(n_brdtik)/(60.0*ssY) 

  # Выравнивание 
  minX = float( (int((MinLon+180)/cW)+1)*cW - 180 )  
  minY = float( (int((MinLat+90 )/cH)+1)*cH - 90 )
  
  #=============== Make List of coordinates (ID, X, Y) ========
  coordsList = []

  # Xmin - by Y - side 1
  Last_ID = 1  
  for j in range( int( (maxY-minY)/cH )+1 ):
      coordsList.append([Last_ID, MinLon, (minY+cH*j)])
          
  # Ymax - by X -side 2
  Last_ID = 2
  for i in range( int( (maxX-minX)/cW )+1 ):
      coordsList.append([Last_ID, (minX+cW*i), maxY])
  
  # Xmax - by Y - side 3
  Last_ID = 3
  for j in range( int( (maxY-minY)/cH ), -1,-1 ):
      coordsList.append([Last_ID, maxX, (minY+cH*j)])
          
  # Ymin - by X -side 4
  Last_ID = 4
  for i in range( int( (maxX-minX)/cW ), -1,-1 ):
      coordsList.append([Last_ID, (minX+cW*i), MinLat])

  # ================== Второй набор тиков ==============
  # === В соответствии с разбиением рамки
  #=============== Make List of coordinates (ID, X, Y) ========
  # SubStep
  ssX = 1.0
  ssY = 1.0

  # Cell size
  cW = float( n_brdminuts/(60.0*ssX) )
  cH = float( n_brdminuts/(60.0*ssY) )

  # Выравнивание 
  minX = float( (int((MinLon+180)/cW)+1)*cW - 180 )  
  minY = float( (int((MinLat+90 )/cH)+1)*cH - 90 )

  # Xmin - by Y - side 1
  Last_ID = 11  
  for j in range( int( (maxY-minY)/cH )+1 ):
      coordsList.append([Last_ID, MinLon, (minY+cH*j)])
          
  # Ymax - by X -side 2
  Last_ID = 21
  for i in range( int( (maxX-minX)/cW )+1 ):
      coordsList.append([Last_ID, (minX+cW*i), maxY])
  
  # Xmax - by Y - side 3
  Last_ID = 31
  for j in range( int( (maxY-minY)/cH ), -1,-1 ):
      coordsList.append([Last_ID, maxX, (minY+cH*j)])
          
  # Ymin - by X -side 4
  Last_ID = 41
  for i in range( int( (maxX-minX)/cW ), -1,-1 ):
      coordsList.append([Last_ID, (minX+cW*i), MinLat])

  # ================== третий набор тиков  ==============
  # ===  1/2 деления разбиением рамки
  #=============== Make List of coordinates (ID, X, Y) ========
  # SubStep
  ssX = 2.0
  ssY = 2.0

  # Cell size
  cW = float( n_brdminuts/(60.0*ssX) )
  cH = float( n_brdminuts/(60.0*ssY) )

  # Выравнивание 
  minX = float( (int((MinLon+180)/cW)+1)*cW - 180 )  
  minY = float( (int((MinLat+90 )/cH)+1)*cH - 90  ) 

  # Xmin - by Y - side 1
  Last_ID = 12  
  for j in range( int( (maxY-minY)/cH )+1 ):
      coordsList.append([Last_ID, MinLon, (minY+cH*j)])
          
  # Ymax - by X -side 2
  Last_ID = 22
  for i in range( int( (maxX-minX)/cW )+1 ):
      coordsList.append([Last_ID, (minX+cW*i), maxY])
  
  # Xmax - by Y - side 3
  Last_ID = 32
  for j in range( int( (maxY-minY)/cH ), -1,-1 ):
      coordsList.append([Last_ID, maxX, (minY+cH*j)])
          
  # Ymin - by X -side 4
  Last_ID = 42
  for i in range( int( (maxX-minX)/cW ), -1,-1 ):
      coordsList.append([Last_ID, (minX+cW*i), MinLat])

  
  #============== Создание и запись shape ============
  try:
      fields = QgsFields()
      fields.append(QgsField("tikID", QVariant.Int, "int", 24, 16, "tikID"))


      if QFile(out_tik).exists():
        if not QgsVectorFileWriter.deleteShapeFile(out_tik):
          return "Failure deleting existing shapefile: " + out_tik

      shapetype = QGis.WKBMultiPoint

      outfile = QgsVectorFileWriter(out_tik, "utf-8", fields, shapetype, crsWGS);

      if (outfile.hasError() != QgsVectorFileWriter.NoError):
          return "Failure creating output shapefile: " + unicode(outfile.errorMessage())

      # Initialize a variable for keeping track of a feature's ID.
      multipoint = []
      for i in range(len(coordsList)-1): 
          side_ID =coordsList[i][0] 

          multipoint.append(QgsPoint(coordsList[i][1], coordsList[i][2]))

          if (side_ID != coordsList[i+1][0]) :
              feature = QgsFeature()
              feature.setGeometry(QgsGeometry.fromMultiPoint(multipoint))
              feature.setAttributes([ side_ID ])
              outfile.addFeature(feature)
              multipoint = []

      # Add the last feature
      multipoint.append(QgsPoint(coordsList[len(coordsList)-1][1], coordsList[len(coordsList)-1][2]))
      feature = QgsFeature()
      feature.setGeometry(QgsGeometry.fromMultiPoint(multipoint))
      feature.setAttributes([ side_ID ])
      outfile.addFeature(feature)
      multipoint = []

  except Exception as e:
      return e.message
  # Закрытие файла и удаление ссылки на него
  del outfile

  # =================================================
  # ==   Построение надписей   ======================
  # =================================================

  #=============== Make List of coordinates (ID, X, Y) ========
  # SubStep
  ssX = 1.0
  ssY = 1.0

  # Cell size
  cW = float(n_lblminuts)/(60.0*ssX)
  cH = float(n_lblminuts)/(60.0*ssY)

  # Выравнивание 
  minX = (int((MinLon+180)/cW)+1)*cW - 180.0  
  minY = (int((MinLat+90 )/cH)+1)*cH - 90.0
  maxX = float(MaxLon)
  maxY = float(MaxLat)  

  coordsList = []
  # Xmin - by Y - side 1
  Last_ID = 1  
  for j in range( int( (maxY-minY)/cH )+1 ):
      pY  = minY+cH*j
      pYd = int(abs(pY))
      pYm = int( (abs(pY)-pYd + 0.00001)*60 )
      pY_ns = "N"
      if (pY<0) : pY_ns = "S"            
      coordsList.append([Last_ID, MinLon, (minY+cH*j), pYd, pYm, pY_ns])
          
  # Ymax - by X -side 2
  Last_ID = 2
  for i in range( int( (maxX-minX)/cW )+1 ):
      pX  = minX+cW*i
      pXd = int(abs(pX))
      pXm = int( (abs(pX)-pXd + 0.00001)*60 )
      pX_ew = "E"
      if (pX<0) : pX_ew = "W"            
      coordsList.append([Last_ID, (minX+cW*i), maxY, pXd, pXm, pX_ew])
  
  # Xmax - by Y - side 3
  Last_ID = 3
  for j in range( int( (maxY-minY)/cH ), -1,-1 ):
      pY  = minY+cH*j
      pYd = int(abs(pY))
      pYm = int( (abs(pY)-pYd + 0.00001)*60 )
      pY_ns = "N"
      if (pY<0) : pY_ns = "S"            
      coordsList.append([Last_ID, maxX, (minY+cH*j), pYd, pYm, pY_ns])
          
  # Ymin - by X -side 4
  Last_ID = 4
  for i in range( int( (maxX-minX)/cW ), -1,-1 ):
      pX  = minX+cW*i
      pXd = int(abs(pX))
      pXm = int( (abs(pX)-pXd + 0.00001)*60 )
      pX_ew = "E"
      if (pX<0) : pX_ew = "W"            
      coordsList.append([Last_ID, (minX+cW*i), MinLat, pXd, pXm, pX_ew])


  #============== Создание и запись shape ============
  try:
      fields = QgsFields()
      fields.append(QgsField("sideID", QVariant.Int, "int", 24, 16, "sideID"))
      fields.append(QgsField("lbl_d", QVariant.Int, "int", 24, 16, "lbl_d"))
      fields.append(QgsField("lbl_m", QVariant.Int, "int", 24, 16, "lbl_m"))
      fields.append(QgsField("nswe", QVariant.String, "text", 2, 0, "nswe"))

      if QFile(out_lbl).exists():
        if not QgsVectorFileWriter.deleteShapeFile(out_lbl):
          return "Failure deleting existing shapefile: " + out_lbl

      shapetype = QGis.WKBPoint

      outfile = QgsVectorFileWriter(out_lbl, "utf-8", fields, shapetype, crsWGS);

      if (outfile.hasError() != QgsVectorFileWriter.NoError):
          return "Failure creating output shapefile: " + unicode(outfile.errorMessage())

      # Initialize a variable for keeping track of a feature's ID.
      for i in range(len(coordsList)): 
          side_ID =coordsList[i][0] 
          pd = coordsList[i][3]
          pm = coordsList[i][4]
          pnswe =  coordsList[i][5]
          feature = QgsFeature()
          feature.setGeometry(QgsGeometry.fromPoint(QgsPoint(coordsList[i][1], coordsList[i][2])))
          feature.setAttributes([ side_ID, pd, pm, pnswe ])
          outfile.addFeature(feature)

  except Exception as e:
      return e.message
  # Закрытие файла и удаление ссылки на него
  del outfile

  #===========================================
  #============== Append to work project =====
  #===========================================
  if addlayer:
    Vlayer_grd = qgis.addVectorLayer(out_grd, os.path.basename(out_grd), "ogr")
    if not Vlayer_grd:
      return "Can not load " + unicode(out_grd)
    Vlayer_brd = qgis.addVectorLayer(out_brd, os.path.basename(out_brd), "ogr")
    if not Vlayer_brd:
      return "Can not load " + unicode(out_brd)
    Vlayer_tik = qgis.addVectorLayer(out_tik, os.path.basename(out_tik), "ogr")
    if not Vlayer_tik:
      return "Can not load " + unicode(out_tik)
    Vlayer_lbl = qgis.addVectorLayer(out_lbl, os.path.basename(out_lbl), "ogr")
    if not Vlayer_lbl:
      return "Can not load " + unicode(out_lbl)
    
    style_path = os.path.join( os.path.dirname(__file__), "base_grd.qml" )
    (errorMsg, result) = Vlayer_grd.loadNamedStyle( style_path )
    style_path = os.path.join( os.path.dirname(__file__), "base_brd.qml" )
    (errorMsg, result) = Vlayer_brd.loadNamedStyle( style_path )
    style_path = os.path.join( os.path.dirname(__file__), "base_tik.qml" )
    (errorMsg, result) = Vlayer_tik.loadNamedStyle( style_path )
    style_path = os.path.join( os.path.dirname(__file__), "base_lbl.qml" )
    (errorMsg, result) = Vlayer_lbl.loadNamedStyle( style_path )

    
  qgis_completion_message(qgis, unicode(outFeatures) + "[ _grd,_brd,_tik,_lbl ].shp features grid shapefiles created")

  return None



#======== Local Utils ============
def qgis_status_message(qgis, message):
  qgis.mainWindow().statusBar().showMessage(message)

def qgis_completion_message(qgis, message):
  qgis_status_message(qgis, message)
  qgis.messageBar().pushMessage(message, 0, 3)


