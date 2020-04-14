import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        discipline = h.get('discipline')
        parameterCategory = h.get('parameterCategory')
        parameterNumber = h.get('parameterNumber')
        is_uerra = h.get('is_uerra')
        scaledValueOfFirstFixedSurface = h.get('scaledValueOfFirstFixedSurface')
        scaleFactorOfFirstFixedSurface = h.get('scaleFactorOfFirstFixedSurface')
        typeOfStatisticalProcessing = h.get('typeOfStatisticalProcessing')
        typeOfFirstFixedSurface = h.get('typeOfFirstFixedSurface')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and is_uerra == 1 and scaledValueOfFirstFixedSurface == 15 and scaleFactorOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 2 and typeOfFirstFixedSurface == 103:
            return 'Maximum temperature at 2 metres since previous post-processing'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and scaledValueOfFirstFixedSurface == 15 and scaleFactorOfFirstFixedSurface == 1 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and is_uerra == 1:
            return 'Minimum temperature at 2 metres since previous post-processing'

        indicatorOfUnitForTimeRange = h.get('indicatorOfUnitForTimeRange')
        lengthOfTimeRange = h.get('lengthOfTimeRange')

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and typeOfStatisticalProcessing == 2 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 'Maximum temperature at 2 metres in the last 6 hours'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfStatisticalProcessing == 3 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15 and indicatorOfUnitForTimeRange == 1 and lengthOfTimeRange == 6:
            return 'Minimum temperature at 2 metres in the last 6 hours'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 0 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15:
            return '2 metre temperature'

        if discipline == 0 and parameterCategory == 0 and parameterNumber == 6 and typeOfFirstFixedSurface == 103 and scaleFactorOfFirstFixedSurface == 1 and scaledValueOfFirstFixedSurface == 15:
            return '2 metre dewpoint temperature'

        if discipline == 0 and parameterCategory == 1 and parameterNumber == 1 and scaledValueOfFirstFixedSurface == 15 and scaleFactorOfFirstFixedSurface == 1 and typeOfFirstFixedSurface == 103:
            return 'Surface air relative humidity'

    return wrapped