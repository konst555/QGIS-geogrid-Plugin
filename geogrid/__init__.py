# -*- coding: utf-8 -*-
"""
/***************************************************************************
 geogrid
                                 A QGIS plugin
 Lat-Lon grid
                             -------------------
        begin                : 2016-02-14
        copyright            : (C) 2016 by Konstantin Puzankov
        email                : konst555@mail.ru
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load geogrid class from file geogrid.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .geo_grid import geogrid
    return geogrid(iface)
