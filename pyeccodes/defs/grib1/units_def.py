import pyeccodes.accessors as _


def load(h):

    def wrapped(h):

        table2Version = h.get_l('table2Version')
        indicatorOfParameter = h.get_l('indicatorOfParameter')
        indicatorOfTypeOfLevel = h.get_l('indicatorOfTypeOfLevel')
        level = h.get_l('level')

        if table2Version == 1 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 71:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 65:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 85:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'kg m**-3'

        if table2Version == 1 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 87:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 127:
            return '~'

        if table2Version == 1 and indicatorOfParameter == 126:
            return 'J'

        if table2Version == 1 and indicatorOfParameter == 125:
            return 'N m**-2'

        if table2Version == 1 and indicatorOfParameter == 124:
            return 'N m**-2'

        if table2Version == 1 and indicatorOfParameter == 120:
            return 'W m**-3 sr**-1'

        if table2Version == 1 and indicatorOfParameter == 119:
            return 'W m**-1 sr**-1'

        if table2Version == 1 and indicatorOfParameter == 117:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 116:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 115:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 114:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 113:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 112:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 111:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 110:
            return 's'

        if table2Version == 1 and indicatorOfParameter == 109:
            return 'Degree true'

        if table2Version == 1 and indicatorOfParameter == 108:
            return 's'

        if table2Version == 1 and indicatorOfParameter == 107:
            return 'Degree true'

        if table2Version == 1 and indicatorOfParameter == 106:
            return 's'

        if table2Version == 1 and indicatorOfParameter == 105:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 104:
            return 'Degree true'

        if table2Version == 1 and indicatorOfParameter == 103:
            return 's'

        if table2Version == 1 and indicatorOfParameter == 102:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 101:
            return 'Degree true'

        if table2Version == 1 and indicatorOfParameter == 100:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 99:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 98:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 97:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 96:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 95:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 94:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 93:
            return 'Degree true'

        if table2Version == 1 and indicatorOfParameter == 92:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 91:
            return '(0 - 1)'

        if table2Version == 1 and indicatorOfParameter == 89:
            return 'kg m**-3'

        if table2Version == 1 and indicatorOfParameter == 88:
            return 'kg kg**-1'

        if table2Version == 1 and indicatorOfParameter == 86:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 82:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 80:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 77:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 70:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 69:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 68:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 67:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 64:
            return 'kg m**-2 s**-1'

        if table2Version == 1 and indicatorOfParameter == 63:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 60:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 59:
            return 'kg m**-2 s**-1'

        if table2Version == 1 and indicatorOfParameter == 56:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 55:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 54:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 53:
            return 'kg kg**-1'

        if table2Version == 1 and indicatorOfParameter == 50:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 49:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 48:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 47:
            return 'Degree true'

        if table2Version == 1 and indicatorOfParameter == 46:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 45:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 42:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 41:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 38:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 37:
            return 'm**2 s**-2'

        if table2Version == 1 and indicatorOfParameter == 31:
            return 'Degree true'

        if table2Version == 1 and indicatorOfParameter == 30:
            return '~'

        if table2Version == 1 and indicatorOfParameter == 29:
            return '~'

        if table2Version == 1 and indicatorOfParameter == 28:
            return '~'

        if table2Version == 1 and indicatorOfParameter == 27:
            return 'gpm'

        if table2Version == 1 and indicatorOfParameter == 26:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 25:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 24:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 23:
            return '~'

        if table2Version == 1 and indicatorOfParameter == 22:
            return '~'

        if table2Version == 1 and indicatorOfParameter == 21:
            return '~'

        if table2Version == 1 and indicatorOfParameter == 20:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 19:
            return 'K m**-1'

        if table2Version == 1 and indicatorOfParameter == 18:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 17:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 16:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 15:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 14:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 9:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 8:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 5:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 3:
            return 'Pa s**-1'

        if table2Version == 1 and indicatorOfParameter == 84:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 76:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 78:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 123:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 122:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 121:
            return 'W m**-2'

        if table2Version == 1 and indicatorOfParameter == 79:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 75:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 74:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 73:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 72:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 66:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 62:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 10:
            return 'kg m**-2'

        if table2Version == 1 and indicatorOfParameter == 90:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 118:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 57:
            return 'm of water equivalent'

        if table2Version == 1 and indicatorOfParameter == 83:
            return 'm'

        if table2Version == 1 and indicatorOfParameter == 81:
            return '(0 - 1)'

        if table2Version == 1 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 52:
            return '%'

        if table2Version == 1 and indicatorOfParameter == 7:
            return 'gpm'

        if table2Version == 1 and indicatorOfParameter == 44:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 2:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 43:
            return 's**-1'

        if table2Version == 1 and indicatorOfParameter == 39:
            return 'Pa s**-1'

        if table2Version == 1 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 51:
            return 'kg kg**-1'

        if table2Version == 1 and indicatorOfParameter == 34:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 33:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 11:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 6:
            return 'm**2 s**-2'

        if table2Version == 1 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 4:
            return 'K m**2 kg**-1 s**-1'

        if table2Version == 1 and indicatorOfParameter == 1:
            return 'Pa'

        if table2Version == 1 and indicatorOfParameter == 32:
            return 'm s**-1'

        if table2Version == 1 and indicatorOfParameter == 13:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 36:
            return 'm**2 s**-1'

        if table2Version == 1 and indicatorOfParameter == 35:
            return 'm**2 s**-1'

        if table2Version == 2 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 71:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 65:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 85:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 86:
            return 'kg m**-3'

        if table2Version == 2 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 87:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 127:
            return '~'

        if table2Version == 2 and indicatorOfParameter == 126:
            return 'J'

        if table2Version == 2 and indicatorOfParameter == 125:
            return 'N m**-2'

        if table2Version == 2 and indicatorOfParameter == 124:
            return 'N m**-2'

        if table2Version == 2 and indicatorOfParameter == 120:
            return 'W m**-3 sr**-1'

        if table2Version == 2 and indicatorOfParameter == 119:
            return 'W m**-1 sr**-1'

        if table2Version == 2 and indicatorOfParameter == 117:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 116:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 115:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 114:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 113:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 112:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 111:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 110:
            return 's'

        if table2Version == 2 and indicatorOfParameter == 109:
            return 'Degree true'

        if table2Version == 2 and indicatorOfParameter == 108:
            return 's'

        if table2Version == 2 and indicatorOfParameter == 107:
            return 'Degree true'

        if table2Version == 2 and indicatorOfParameter == 106:
            return 's'

        if table2Version == 2 and indicatorOfParameter == 105:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 104:
            return 'Degree true'

        if table2Version == 2 and indicatorOfParameter == 103:
            return 's'

        if table2Version == 2 and indicatorOfParameter == 102:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 101:
            return 'Degree true'

        if table2Version == 2 and indicatorOfParameter == 100:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 99:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 98:
            return 's**-1'

        if table2Version == 2 and indicatorOfParameter == 97:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 96:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 95:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 94:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 93:
            return 'Degree true'

        if table2Version == 2 and indicatorOfParameter == 92:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 91:
            return '(0 - 1)'

        if table2Version == 2 and indicatorOfParameter == 89:
            return 'kg m**-3'

        if table2Version == 2 and indicatorOfParameter == 88:
            return 'kg kg**-1'

        if table2Version == 2 and indicatorOfParameter == 86:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 82:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 80:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 77:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 70:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 69:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 68:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 67:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 64:
            return 'kg m**-2 s**-1'

        if table2Version == 2 and indicatorOfParameter == 63:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 60:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 59:
            return 'kg m**-2 s**-1'

        if table2Version == 2 and indicatorOfParameter == 56:
            return 'Pa'

        if table2Version == 2 and indicatorOfParameter == 55:
            return 'Pa'

        if table2Version == 2 and indicatorOfParameter == 54:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 53:
            return 'kg kg**-1'

        if table2Version == 2 and indicatorOfParameter == 50:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 49:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 48:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 47:
            return 'Degree true'

        if table2Version == 2 and indicatorOfParameter == 46:
            return 's**-1'

        if table2Version == 2 and indicatorOfParameter == 45:
            return 's**-1'

        if table2Version == 2 and indicatorOfParameter == 42:
            return 's**-1'

        if table2Version == 2 and indicatorOfParameter == 41:
            return 's**-1'

        if table2Version == 2 and indicatorOfParameter == 38:
            return 's**-1'

        if table2Version == 2 and indicatorOfParameter == 37:
            return 'm**2 s**-2'

        if table2Version == 2 and indicatorOfParameter == 31:
            return 'Degree true'

        if table2Version == 2 and indicatorOfParameter == 30:
            return '~'

        if table2Version == 2 and indicatorOfParameter == 29:
            return '~'

        if table2Version == 2 and indicatorOfParameter == 28:
            return '~'

        if table2Version == 2 and indicatorOfParameter == 27:
            return 'gpm'

        if table2Version == 2 and indicatorOfParameter == 26:
            return 'Pa'

        if table2Version == 2 and indicatorOfParameter == 25:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 24:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 23:
            return '~'

        if table2Version == 2 and indicatorOfParameter == 22:
            return '~'

        if table2Version == 2 and indicatorOfParameter == 21:
            return '~'

        if table2Version == 2 and indicatorOfParameter == 20:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 19:
            return 'K m**-1'

        if table2Version == 2 and indicatorOfParameter == 18:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 17:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 16:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 15:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 14:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 9:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 8:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 5:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 3:
            return 'Pa s**-1'

        if table2Version == 2 and indicatorOfParameter == 84:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 76:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 78:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 123:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 122:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 121:
            return 'W m**-2'

        if table2Version == 2 and indicatorOfParameter == 79:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 75:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 74:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 73:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 72:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 66:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 62:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 10:
            return 'kg m**-2'

        if table2Version == 2 and indicatorOfParameter == 90:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 118:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 57:
            return 'm of water equivalent'

        if table2Version == 2 and indicatorOfParameter == 83:
            return 'm'

        if table2Version == 2 and indicatorOfParameter == 81:
            return '(0 - 1)'

        if table2Version == 2 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 52:
            return '%'

        if table2Version == 2 and indicatorOfParameter == 7:
            return 'gpm'

        if table2Version == 2 and indicatorOfParameter == 44:
            return 's**-1'

        if table2Version == 2 and indicatorOfParameter == 2:
            return 'Pa'

        if table2Version == 2 and indicatorOfParameter == 43:
            return 's**-1'

        if table2Version == 2 and indicatorOfParameter == 39:
            return 'Pa s**-1'

        if table2Version == 2 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'Pa'

        if table2Version == 2 and indicatorOfParameter == 51:
            return 'kg kg**-1'

        if table2Version == 2 and indicatorOfParameter == 34:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 33:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 11:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 6:
            return 'm**2 s**-2'

        if table2Version == 2 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 4:
            return 'K m**2 kg**-1 s**-1'

        if table2Version == 2 and indicatorOfParameter == 1:
            return 'Pa'

        if table2Version == 2 and indicatorOfParameter == 32:
            return 'm s**-1'

        if table2Version == 2 and indicatorOfParameter == 13:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 36:
            return 'm**2 s**-1'

        if table2Version == 2 and indicatorOfParameter == 35:
            return 'm**2 s**-1'

        if table2Version == 3 and indicatorOfParameter == 61 and indicatorOfTypeOfLevel == 1 and level == 0:
            return 'kg m**-2'

        if table2Version == 3 and indicatorOfParameter == 71:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 65:
            return 'kg m**-2'

        if table2Version == 3 and indicatorOfParameter == 85:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 86:
            return 'kg m**-3'

        if table2Version == 3 and indicatorOfParameter == 7 and indicatorOfTypeOfLevel == 1:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 87:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 127:
            return '~'

        if table2Version == 3 and indicatorOfParameter == 126:
            return 'J'

        if table2Version == 3 and indicatorOfParameter == 125:
            return 'N m**-2'

        if table2Version == 3 and indicatorOfParameter == 124:
            return 'N m**-2'

        if table2Version == 3 and indicatorOfParameter == 120:
            return 'W m**-3 sr**-1'

        if table2Version == 3 and indicatorOfParameter == 119:
            return 'W m**-1 sr**-1'

        if table2Version == 3 and indicatorOfParameter == 117:
            return 'W m**-2'

        if table2Version == 3 and indicatorOfParameter == 116:
            return 'W m**-2'

        if table2Version == 3 and indicatorOfParameter == 115:
            return 'W m**-2'

        if table2Version == 3 and indicatorOfParameter == 114:
            return 'W m**-2'

        if table2Version == 3 and indicatorOfParameter == 113:
            return 'W m**-2'

        if table2Version == 3 and indicatorOfParameter == 112:
            return 'W m**-2'

        if table2Version == 3 and indicatorOfParameter == 111:
            return 'W m**-2'

        if table2Version == 3 and indicatorOfParameter == 110:
            return 's'

        if table2Version == 3 and indicatorOfParameter == 109:
            return 'Degree true'

        if table2Version == 3 and indicatorOfParameter == 108:
            return 's'

        if table2Version == 3 and indicatorOfParameter == 107:
            return 'Degree true'

        if table2Version == 3 and indicatorOfParameter == 106:
            return 's'

        if table2Version == 3 and indicatorOfParameter == 105:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 104:
            return 'Degree true'

        if table2Version == 3 and indicatorOfParameter == 103:
            return 's'

        if table2Version == 3 and indicatorOfParameter == 102:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 101:
            return 'Degree true'

        if table2Version == 3 and indicatorOfParameter == 100:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 99:
            return 'kg m**-2'

        if table2Version == 3 and indicatorOfParameter == 98:
            return 's**-1'

        if table2Version == 3 and indicatorOfParameter == 97:
            return 'm s**-1'

        if table2Version == 3 and indicatorOfParameter == 96:
            return 'm s**-1'

        if table2Version == 3 and indicatorOfParameter == 95:
            return 'm s**-1'

        if table2Version == 3 and indicatorOfParameter == 94:
            return 'm s**-1'

        if table2Version == 3 and indicatorOfParameter == 93:
            return 'Degree true'

        if table2Version == 3 and indicatorOfParameter == 92:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 91:
            return '(0 - 1)'

        if table2Version == 3 and indicatorOfParameter == 89:
            return 'kg m**-3'

        if table2Version == 3 and indicatorOfParameter == 88:
            return 'kg kg**-1'

        if table2Version == 3 and indicatorOfParameter == 86:
            return 'kg m**-2'

        if table2Version == 3 and indicatorOfParameter == 82:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 80:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 77:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 70:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 69:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 68:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 67:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 64:
            return 'kg m**-2 s**-1'

        if table2Version == 3 and indicatorOfParameter == 63:
            return 'kg m**-2'

        if table2Version == 3 and indicatorOfParameter == 60:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 59:
            return 'kg m**-2 s**-1'

        if table2Version == 3 and indicatorOfParameter == 56:
            return 'Pa'

        if table2Version == 3 and indicatorOfParameter == 55:
            return 'Pa'

        if table2Version == 3 and indicatorOfParameter == 54:
            return 'kg m**-2'

        if table2Version == 3 and indicatorOfParameter == 53:
            return 'kg kg**-1'

        if table2Version == 3 and indicatorOfParameter == 50:
            return 'm s**-1'

        if table2Version == 3 and indicatorOfParameter == 49:
            return 'm s**-1'

        if table2Version == 3 and indicatorOfParameter == 48:
            return 'm s**-1'

        if table2Version == 3 and indicatorOfParameter == 47:
            return 'Degree true'

        if table2Version == 3 and indicatorOfParameter == 46:
            return 's**-1'

        if table2Version == 3 and indicatorOfParameter == 45:
            return 's**-1'

        if table2Version == 3 and indicatorOfParameter == 42:
            return 's**-1'

        if table2Version == 3 and indicatorOfParameter == 41:
            return 's**-1'

        if table2Version == 3 and indicatorOfParameter == 38:
            return 's**-1'

        if table2Version == 3 and indicatorOfParameter == 37:
            return 'm**2 s**-2'

        if table2Version == 3 and indicatorOfParameter == 31:
            return 'Degree true'

        if table2Version == 3 and indicatorOfParameter == 30:
            return '~'

        if table2Version == 3 and indicatorOfParameter == 29:
            return '~'

        if table2Version == 3 and indicatorOfParameter == 28:
            return '~'

        if table2Version == 3 and indicatorOfParameter == 27:
            return 'gpm'

        if table2Version == 3 and indicatorOfParameter == 26:
            return 'Pa'

        if table2Version == 3 and indicatorOfParameter == 25:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 24:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 23:
            return '~'

        if table2Version == 3 and indicatorOfParameter == 22:
            return '~'

        if table2Version == 3 and indicatorOfParameter == 21:
            return '~'

        if table2Version == 3 and indicatorOfParameter == 20:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 19:
            return 'K m**-1'

        if table2Version == 3 and indicatorOfParameter == 18:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 17:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 16:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 15:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 14:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 9:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 8:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 5:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 3:
            return 'Pa s**-1'

        if table2Version == 3 and indicatorOfParameter == 12:
            return 'K'

        if table2Version == 2 and indicatorOfParameter == 12:
            return 'K'

        if table2Version == 1 and indicatorOfParameter == 12:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 84:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 76:
            return 'kg m**-2'

        if table2Version == 3 and indicatorOfParameter == 78:
            return 'kg m**-2'

        if table2Version == 3 and indicatorOfParameter == 123:
            return 'W m**-2'

        if table2Version == 3 and indicatorOfParameter == 122:
            return 'W m**-2'

        if table2Version == 3 and indicatorOfParameter == 121:
            return 'W m**-2'

        if table2Version == 3 and indicatorOfParameter == 79:
            return 'kg m**-2'

        if table2Version == 3 and indicatorOfParameter == 75:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 74:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 73:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 72:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 66:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 62:
            return 'kg m**-2'

        if table2Version == 3 and indicatorOfParameter == 10:
            return 'kg m**-2'

        if table2Version == 3 and indicatorOfParameter == 90:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 118:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 57:
            return 'm of water equivalent'

        if table2Version == 3 and indicatorOfParameter == 83:
            return 'm'

        if table2Version == 3 and indicatorOfParameter == 81:
            return '(0 - 1)'

        if table2Version == 3 and indicatorOfParameter == 17 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 11 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 34 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s**-1'

        if table2Version == 3 and indicatorOfParameter == 33 and indicatorOfTypeOfLevel == 105 and level == 10:
            return 'm s**-1'

        if table2Version == 3 and indicatorOfParameter == 52:
            return '%'

        if table2Version == 3 and indicatorOfParameter == 7:
            return 'gpm'

        if table2Version == 3 and indicatorOfParameter == 44:
            return 's**-1'

        if table2Version == 3 and indicatorOfParameter == 2:
            return 'Pa'

        if table2Version == 3 and indicatorOfParameter == 43:
            return 's**-1'

        if table2Version == 3 and indicatorOfParameter == 39:
            return 'Pa s**-1'

        if table2Version == 3 and indicatorOfParameter == 1 and indicatorOfTypeOfLevel == 1:
            return 'Pa'

        if table2Version == 3 and indicatorOfParameter == 51:
            return 'kg kg**-1'

        if table2Version == 3 and indicatorOfParameter == 34:
            return 'm s**-1'

        if table2Version == 3 and indicatorOfParameter == 33:
            return 'm s**-1'

        if table2Version == 3 and indicatorOfParameter == 11:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 6:
            return 'm**2 s**-2'

        if table2Version == 3 and indicatorOfParameter == 16 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 15 and indicatorOfTypeOfLevel == 105 and level == 2:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 4:
            return 'K m**2 kg**-1 s**-1'

        if table2Version == 3 and indicatorOfParameter == 1:
            return 'Pa'

        if table2Version == 3 and indicatorOfParameter == 32:
            return 'm s**-1'

        if table2Version == 3 and indicatorOfParameter == 13:
            return 'K'

        if table2Version == 3 and indicatorOfParameter == 36:
            return 'm**2 s**-1'

        if table2Version == 3 and indicatorOfParameter == 35:
            return 'm**2 s**-1'

    return wrapped
