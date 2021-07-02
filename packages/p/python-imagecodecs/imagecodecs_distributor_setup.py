# openSUSE extension setup to build python-imagecodecs

import os
import subprocess
import sys

def customize_build(EXTENSIONS, OPTIONS):

    includedir = os.getenv("INCDIR",'') + '/'

    del EXTENSIONS['jpeg12']  # jpeg12 requires custom build
    del EXTENSIONS['lerc']    # LERC library not available
    del EXTENSIONS['lz4f']    # requires static linking
    del EXTENSIONS['jpegxl']  # jpeg-xl library not available
    del EXTENSIONS['brunsli']  # Brunsli library not available
    
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
    
    
    openjpeg_inc = subprocess.check_output(
        ['pkgconf', '--variable=includedir', 'libopenjp2'],
        text=True,
        ).strip()
    EXTENSIONS['jpeg2k']['include_dirs'].append(openjpeg_inc)
    EXTENSIONS['jpegxr']['include_dirs'].append(includedir +  'jxrlib')
    EXTENSIONS['rcomp']['include_dirs'].append(includedir +   'cfitsio')
    EXTENSIONS['zopfli']['include_dirs'].append(includedir +  'zopfli')
