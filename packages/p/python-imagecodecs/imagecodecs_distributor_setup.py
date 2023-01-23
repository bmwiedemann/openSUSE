# openSUSE extension setup to build python-imagecodecs

import os
import subprocess
import sys

def customize_build(EXTENSIONS, OPTIONS):

    includedir = os.getenv("INCDIR",'') + '/'

    del EXTENSIONS['apng']    # png-apng library not available
    del EXTENSIONS['blosc2']  # blosc2 library not available
    del EXTENSIONS['brunsli'] # graphics/brunsli not in Factory
    del EXTENSIONS['jetraw']  # jetraw library not available
    del EXTENSIONS['jpeg12']  # jpeg12 requires custom build
    del EXTENSIONS['jpegxl']  # jpeg-xl library not available
    del EXTENSIONS['lerc']    # LERC library not available
    del EXTENSIONS['lz4f']    # requires static linking
    del EXTENSIONS['mozjpeg'] # Win32 only
    
    EXTENSIONS['avif']['libraries'] = [
        'avif',
        'aom',
        'dav1d',
        'rav1e',
    ]

    if sys.maxsize < 2**63 - 1:
        # no zfp on 32-bit platforms
        del EXTENSIONS['zfp']
        # avif tests fail on 32-bit
        del EXTENSIONS['avif']
        # spng build fail on 32-bit
        del EXTENSIONS['spng']

    openjpeg_inc = subprocess.check_output(
        ['pkgconf', '--variable=includedir', 'libopenjp2'],
        text=True,
        ).strip()
    EXTENSIONS['jpeg2k']['include_dirs'].append(openjpeg_inc)
    EXTENSIONS['jpegxr']['include_dirs'].append(includedir +  'jxrlib')
    EXTENSIONS['rcomp']['include_dirs'].append(includedir +   'cfitsio')
    EXTENSIONS['zopfli']['include_dirs'].append(includedir +  'zopfli')
    EXTENSIONS['lzham']['libraries'] = ['lzhamdll']
    