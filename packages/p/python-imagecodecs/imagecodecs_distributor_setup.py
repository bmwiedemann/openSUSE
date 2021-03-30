# openSUSE extension setup to build python-imagecodecs

import os
import subprocess
import sys

def customize_build(EXTENSIONS, OPTIONS):

    includedir = os.getenv("INCDIR",'') + '/'

    del EXTENSIONS['jpeg12']  # jpeg12 requires custom build
    del EXTENSIONS['lerc']    # LERC library not available
    del EXTENSIONS['lz4f']    # requires static linking
    del EXTENSIONS['jpegxl']  # Brunsli library not available
    
    EXTENSIONS['avif']['libraries'] = [
        'avif',
        'aom',
        'dav1d',
        'rav1e',
    ]

    # no zfp on 32-bit platforms
    if sys.maxsize < 2**63 - 1:
        del EXTENSIONS['zfp']
    
    
    openjpeg_inc = subprocess.check_output(
        ['pkgconf', '--variable=includedir', 'libopenjp2'],
        text=True,
        ).strip()
    EXTENSIONS['jpeg2k']['include_dirs'].append(openjpeg_inc)

    EXTENSIONS['jpegxr']['include_dirs'].append(includedir +  'jxrlib')
    EXTENSIONS['zopfli']['include_dirs'].append(includedir +  'zopfli')
