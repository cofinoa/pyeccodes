def load(h):
    return ({'abbr': 6, 'code': 6, 'title': '- Total soil moisture', 'units': 'm'},
            {'abbr': 8, 'code': 8, 'title': 'SRO Surface runoff', 'units': 'kg m**-2'},
            {'abbr': 9,
             'code': 9,
             'title': 'SSRO Sub-surface runoff',
             'units': 'kg m**-2'},
            {'abbr': 10,
             'code': 10,
             'title': 'SSWCSDOWN Clear-sky (II) down surface sw flux',
             'units': 'W m**-2'},
            {'abbr': 13,
             'code': 13,
             'title': 'SSWCSUP Clear-sky (II) up surface sw flux',
             'units': 'W m**-2'},
            {'abbr': 25, 'code': 25, 'title': 'VIS15 Visibility at 1.5m', 'units': 'm'},
            {'abbr': 31,
             'code': 31,
             'title': '- Fraction of sea-ice in sea',
             'units': '0 - 1'},
            {'abbr': 34,
             'code': 34,
             'title': '- Open-sea surface temperature',
             'units': 'K'},
            {'abbr': 39,
             'code': 39,
             'title': '- Volumetric soil water layer 1',
             'units': 'm**3 m**-3'},
            {'abbr': 40,
             'code': 40,
             'title': '- Volumetric soil water layer 2',
             'units': 'm**3 m**-3'},
            {'abbr': 41,
             'code': 41,
             'title': '- Volumetric soil water layer 3',
             'units': 'm**3 m**-3'},
            {'abbr': 42,
             'code': 42,
             'title': '- Volumetric soil water layer 4',
             'units': 'm**3 m**-3'},
            {'abbr': 49,
             'code': 49,
             'title': '- 10 metre wind gust in the last 24 hours',
             'units': 'm s**-1'},
            {'abbr': 50,
             'code': 50,
             'title': 'MN15T Minimum temperature at 1.5m since previous post-processing',
             'units': 'K'},
            {'abbr': 51,
             'code': 51,
             'title': 'MX15T Maximum temperature at 1.5m since previous post-processing',
             'units': 'K'},
            {'abbr': 52,
             'code': 52,
             'title': 'RHUM Relative humidity at 1.5m',
             'units': 'kg kg**-1'},
            {'abbr': 55,
             'code': 55,
             'title': '- 1.5m temperature - mean in the last 24 hours',
             'units': 'K'},
            {'abbr': 83,
             'code': 83,
             'title': '- Net primary productivity',
             'units': 'kg C m**-2 s**-1'},
            {'abbr': 85,
             'code': 85,
             'title': '- 10m U wind over land',
             'units': 'm s**-1'},
            {'abbr': 86,
             'code': 86,
             'title': '- 10m V wind over land',
             'units': 'm s**-1'},
            {'abbr': 87,
             'code': 87,
             'title': '- 1.5m temperature over land',
             'units': 'K'},
            {'abbr': 88,
             'code': 88,
             'title': '- 1.5m dewpoint temperature over land',
             'units': 'K'},
            {'abbr': 89,
             'code': 89,
             'title': '- Top incoming solar radiation',
             'units': 'J m**-2'},
            {'abbr': 90,
             'code': 90,
             'title': '- Top outgoing solar radiation',
             'units': 'J m**-2'},
            {'abbr': 94,
             'code': 94,
             'title': '- Mean sea surface temperature',
             'units': 'K'},
            {'abbr': 95,
             'code': 95,
             'title': '- 1.5m specific humidity',
             'units': 'kg kg**-1'},
            {'abbr': 96,
             'code': 96,
             'title': '- 2 metre specific humidity',
             'units': 'kg kg**-1'},
            {'abbr': 97, 'code': 97, 'title': 'SIST Sea-ice Snow Thickness', 'units': 'm'},
            {'abbr': 98, 'code': 98, 'title': 'SIT Sea-ice thickness', 'units': 'm'},
            {'abbr': 99,
             'code': 99,
             'title': '- Liquid water potential temperature',
             'units': 'K'},
            {'abbr': 110,
             'code': 110,
             'title': '- Ocean ice concentration',
             'units': '0 - 1'},
            {'abbr': 111, 'code': 111, 'title': '- Ocean mean ice depth', 'units': 'm'},
            {'abbr': 116,
             'code': 116,
             'title': 'SWRSURF Short wave radiation flux at surface',
             'units': 'J m**-2'},
            {'abbr': 117,
             'code': 117,
             'title': 'SWRTOP Short wave radiation flux at top of atmosphere',
             'units': 'J m**-2'},
            {'abbr': 137,
             'code': 137,
             'title': 'TCWVAP Total column water vapour',
             'units': 'kg m**-2'},
            {'abbr': 139,
             'code': 139,
             'title': '- Soil temperature layer 1',
             'units': 'K'},
            {'abbr': 142,
             'code': 142,
             'title': 'LSRRATE Large scale rainfall rate',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 143,
             'code': 143,
             'title': 'CRFRATE Convective rainfall rate',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 164,
             'code': 164,
             'title': '- Average potential temperature in upper 293.4m',
             'units': 'degrees C'},
            {'abbr': 167, 'code': 167, 'title': '- 1.5m temperature', 'units': 'K'},
            {'abbr': 168,
             'code': 168,
             'title': '- 1.5m dewpoint temperature',
             'units': 'K'},
            {'abbr': 170,
             'code': 170,
             'title': '- Soil temperature layer 2',
             'units': 'K'},
            {'abbr': 172, 'code': 172, 'title': 'LSM Land-sea mask', 'units': '0 - 1'},
            {'abbr': 175,
             'code': 175,
             'title': '- Average salinity in upper 293.4m',
             'units': 'psu'},
            {'abbr': 183,
             'code': 183,
             'title': '- Soil temperature layer 3',
             'units': 'K'},
            {'abbr': 186,
             'code': 186,
             'title': 'VLCA Very low cloud amount',
             'units': '0 - 1'},
            {'abbr': 201,
             'code': 201,
             'title': '- 1.5m temperature - maximum in the last 24 hours',
             'units': 'K'},
            {'abbr': 202,
             'code': 202,
             'title': '- 1.5m temperature - minimum in the last 24 hours',
             'units': 'K'},
            {'abbr': 236,
             'code': 236,
             'title': '- Soil temperature layer 4',
             'units': 'K'},
            {'abbr': 239,
             'code': 239,
             'title': 'CSFRATE Convective snowfall rate',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 240,
             'code': 240,
             'title': 'LSFRATE Large scale snowfall rate',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 248,
             'code': 248,
             'title': 'TCCRO Total cloud amount - random overlap',
             'units': '0 - 1'},
            {'abbr': 249,
             'code': 249,
             'title': 'TCCLWR Total cloud amount in lw radiation',
             'units': '0 - 1'},
            {'abbr': None, 'code': 255, 'title': '- Indicates a missing value'})
