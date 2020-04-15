import pyeccodes.accessors as _


def load(h):

    h.add(_.Unsigned('Ni', 2))
    h.alias('numberOfPointsAlongAParallel', 'Ni')
    h.alias('Nx', 'Ni')
    h.add(_.Unsigned('Nj', 2))
    h.alias('numberOfPointsAlongAMeridian', 'Nj')
    h.alias('Ny', 'Nj')
    h.add(_.Signed('latitudeOfFirstGridPoint', 3))
    h.add(_.Scale('latitudeOfFirstGridPointInDegrees', _.Get('latitudeOfFirstGridPoint'), _.Get('oneConstant'), _.Get('grib1divider'), _.Get('truncateDegrees')))
    h.alias('geography.latitudeOfFirstGridPointInDegrees', 'latitudeOfFirstGridPointInDegrees')
    h.alias('La1', 'latitudeOfFirstGridPoint')
    h.add(_.Signed('longitudeOfFirstGridPoint', 3))
    h.add(_.Scale('longitudeOfFirstGridPointInDegrees', _.Get('longitudeOfFirstGridPoint'), _.Get('oneConstant'), _.Get('grib1divider'), _.Get('truncateDegrees')))
    h.alias('geography.longitudeOfFirstGridPointInDegrees', 'longitudeOfFirstGridPointInDegrees')
    h.alias('Lo1', 'longitudeOfFirstGridPoint')
    h.add(_.Codeflag('resolutionAndComponentFlags', 1, "grib1/7.table"))
    h.add(_.Bit('ijDirectionIncrementGiven', _.Get('resolutionAndComponentFlags'), 7))
    h.alias('iDirectionIncrementGiven', 'ijDirectionIncrementGiven')
    h.alias('jDirectionIncrementGiven', 'ijDirectionIncrementGiven')
    h.alias('DiGiven', 'ijDirectionIncrementGiven')
    h.alias('DjGiven', 'ijDirectionIncrementGiven')
    h.add(_.Bit('earthIsOblate', _.Get('resolutionAndComponentFlags'), 6))

    if h.get_l('earthIsOblate'):
        h.add(_.Transient('earthMajorAxis', 6.37816e+06))
        h.add(_.Transient('earthMinorAxis', 6.35678e+06))
        h.alias('earthMajorAxisInMetres', 'earthMajorAxis')
        h.alias('earthMinorAxisInMetres', 'earthMinorAxis')

    h.add(_.Bit('resolutionAndComponentFlags3', _.Get('resolutionAndComponentFlags'), 5))
    h.add(_.Bit('resolutionAndComponentFlags4', _.Get('resolutionAndComponentFlags'), 4))
    h.add(_.Bit('uvRelativeToGrid', _.Get('resolutionAndComponentFlags'), 3))
    h.add(_.Bit('resolutionAndComponentFlags6', _.Get('resolutionAndComponentFlags'), 2))
    h.add(_.Bit('resolutionAndComponentFlags7', _.Get('resolutionAndComponentFlags'), 1))
    h.add(_.Bit('resolutionAndComponentFlags8', _.Get('resolutionAndComponentFlags'), 0))
    h.add(_.Signed('latitudeOfLastGridPoint', 3))
    h.add(_.Scale('latitudeOfLastGridPointInDegrees', _.Get('latitudeOfLastGridPoint'), _.Get('oneConstant'), _.Get('grib1divider'), _.Get('truncateDegrees')))
    h.alias('geography.latitudeOfLastGridPointInDegrees', 'latitudeOfLastGridPointInDegrees')
    h.alias('La2', 'latitudeOfLastGridPoint')
    h.add(_.Signed('longitudeOfLastGridPoint', 3))
    h.add(_.Scale('longitudeOfLastGridPointInDegrees', _.Get('longitudeOfLastGridPoint'), _.Get('oneConstant'), _.Get('grib1divider'), _.Get('truncateDegrees')))
    h.alias('geography.longitudeOfLastGridPointInDegrees', 'longitudeOfLastGridPointInDegrees')
    h.alias('Lo2', 'longitudeOfLastGridPoint')
    h.alias('yFirst', 'latitudeOfFirstGridPointInDegrees')
    h.alias('yLast', 'latitudeOfLastGridPointInDegrees')
    h.alias('xFirst', 'longitudeOfFirstGridPointInDegrees')
    h.alias('xLast', 'longitudeOfLastGridPointInDegrees')
    h.alias('latitudeFirstInDegrees', 'latitudeOfFirstGridPointInDegrees')
    h.alias('longitudeFirstInDegrees', 'longitudeOfFirstGridPointInDegrees')
    h.alias('latitudeLastInDegrees', 'latitudeOfLastGridPointInDegrees')
    h.alias('longitudeLastInDegrees', 'longitudeOfLastGridPointInDegrees')
    h.add(_.Unsigned('iDirectionIncrement', 2))
    h.add(_.Unsigned('jDirectionIncrement', 2))
    h.alias('Dj', 'jDirectionIncrement')
    h.alias('Dy', 'jDirectionIncrement')
    h.alias('Di', 'iDirectionIncrement')
    h.alias('Dx', 'iDirectionIncrement')
    h.add(_.Codeflag('scanningMode', 1, "grib1/8.table"))
    h.add(_.Bit('iScansNegatively', _.Get('scanningMode'), 7))
    h.add(_.Bit('jScansPositively', _.Get('scanningMode'), 6))
    h.add(_.Bit('jPointsAreConsecutive', _.Get('scanningMode'), 5))
    h.add(_.Constant('alternativeRowScanning', 0))
    h.add(_.Transient('iScansPositively', _.Not(_.Get('iScansNegatively'))))
    h.alias('geography.iScansNegatively', 'iScansNegatively')
    h.alias('geography.jScansPositively', 'jScansPositively')
    h.alias('geography.jPointsAreConsecutive', 'jPointsAreConsecutive')
    h.add(_.Bit('scanningMode4', _.Get('scanningMode'), 4))
    h.add(_.Bit('scanningMode5', _.Get('scanningMode'), 3))
    h.add(_.Bit('scanningMode6', _.Get('scanningMode'), 2))
    h.add(_.Bit('scanningMode7', _.Get('scanningMode'), 1))
    h.add(_.Bit('scanningMode8', _.Get('scanningMode'), 0))
    h.add(_.Change_scanning_direction('swapScanningX', _.Get('values'), _.Get('Ni'), _.Get('Nj'), _.Get('iScansNegatively'), _.Get('jScansPositively'), _.Get('xFirst'), _.Get('xLast'), _.Get('x')))
    h.alias('swapScanningLon', 'swapScanningX')
    h.add(_.Change_scanning_direction('swapScanningY', _.Get('values'), _.Get('Ni'), _.Get('Nj'), _.Get('iScansNegatively'), _.Get('jScansPositively'), _.Get('yFirst'), _.Get('yLast'), _.Get('y')))
    h.alias('swapScanningLat', 'swapScanningY')

    if h.get_l('jPointsAreConsecutive'):
        h.alias('numberOfRows', 'Ni')
        h.alias('numberOfColumns', 'Nj')
    else:
        h.alias('numberOfRows', 'Nj')
        h.alias('numberOfColumns', 'Ni')

    h.add(_.Latlon_increment('jDirectionIncrementInDegrees', _.Get('ijDirectionIncrementGiven'), _.Get('jDirectionIncrement'), _.Get('jScansPositively'), _.Get('latitudeOfFirstGridPointInDegrees'), _.Get('latitudeOfLastGridPointInDegrees'), _.Get('numberOfPointsAlongAMeridian'), _.Get('oneConstant'), _.Get('grib1divider'), 0))
    h.alias('geography.jDirectionIncrementInDegrees', 'jDirectionIncrementInDegrees')
    h.alias('DjInDegrees', 'jDirectionIncrementInDegrees')
    h.alias('DyInDegrees', 'jDirectionIncrementInDegrees')
    h.add(_.Latlon_increment('iDirectionIncrementInDegrees', _.Get('ijDirectionIncrementGiven'), _.Get('iDirectionIncrement'), _.Get('iScansPositively'), _.Get('longitudeOfFirstGridPointInDegrees'), _.Get('longitudeOfLastGridPointInDegrees'), _.Get('Ni'), _.Get('oneConstant'), _.Get('grib1divider'), 1))
    h.alias('geography.iDirectionIncrementInDegrees', 'iDirectionIncrementInDegrees')
    h.alias('DiInDegrees', 'iDirectionIncrementInDegrees')
    h.alias('DxInDegrees', 'iDirectionIncrementInDegrees')
    h.add(_.Number_of_points('numberOfDataPoints', _.Get('Ni'), _.Get('Nj'), _.Get('PLPresent'), _.Get('pl')))
    h.alias('numberOfPoints', 'numberOfDataPoints')
    h.add(_.Number_of_values('numberOfValues', _.Get('values'), _.Get('bitsPerValue'), _.Get('numberOfDataPoints'), _.Get('bitmapPresent'), _.Get('bitmap'), _.Get('numberOfCodedValues')))

    if h._missing('Ni'):
        h.add(_.Iterator('ITERATOR', _.Get('latlon_reduced'), _.Get('numberOfPoints'), _.Get('missingValue'), _.Get('values'), _.Get('latitudeFirstInDegrees'), _.Get('longitudeFirstInDegrees'), _.Get('latitudeLastInDegrees'), _.Get('longitudeLastInDegrees'), _.Get('Nj'), _.Get('DjInDegrees'), _.Get('pl')))
        h.add(_.Nearest('NEAREST', _.Get('latlon_reduced'), _.Get('values'), _.Get('radius'), _.Get('Nj'), _.Get('pl'), _.Get('longitudeFirstInDegrees'), _.Get('longitudeLastInDegrees')))
    else:
        h.add(_.Transient('iteratorDisableUnrotate', 0))
        h.add(_.Iterator('ITERATOR', _.Get('latlon'), _.Get('numberOfPoints'), _.Get('missingValue'), _.Get('values'), _.Get('longitudeFirstInDegrees'), _.Get('DiInDegrees'), _.Get('Ni'), _.Get('Nj'), _.Get('iScansNegatively'), _.Get('latitudeFirstInDegrees'), _.Get('DjInDegrees'), _.Get('jScansPositively'), _.Get('jPointsAreConsecutive'), _.Get('isRotatedGrid'), _.Get('angleOfRotation'), _.Get('latitudeOfSouthernPoleInDegrees'), _.Get('longitudeOfSouthernPoleInDegrees')))
        h.add(_.Nearest('NEAREST', _.Get('regular'), _.Get('values'), _.Get('radius'), _.Get('Ni'), _.Get('Nj')))

    h.add(_.Latlonvalues('latLonValues', _.Get('values')))
    h.alias('latitudeLongitudeValues', 'latLonValues')
    h.add(_.Latitudes('latitudes', _.Get('values'), 0))
    h.add(_.Longitudes('longitudes', _.Get('values'), 0))
    h.add(_.Latitudes('distinctLatitudes', _.Get('values'), 1))
    h.add(_.Longitudes('distinctLongitudes', _.Get('values'), 1))
