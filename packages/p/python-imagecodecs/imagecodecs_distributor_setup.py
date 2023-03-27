# openSUSE extension setup to build python-imagecodecs

import os
import subprocess
import sys

def customize_build(EXTENSIONS, OPTIONS):

    includedir = os.getenv("INCDIR",'') + '/'

    del EXTENSIONS['apng']    # png-apng library not available
    del EXTENSIONS['brunsli'] # graphics/brunsli not in Factory
    del EXTENSIONS['jetraw']  # jetraw library not available
    del EXTENSIONS['jpeg8']   # jpeg8 / libjegturbo 2.1.91 is beta and not available
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
    else:
        EXTENSIONS['avif']['libraries'].extend([
            'SvtAv1Enc',
            'SvtAv1Dec',
        ])

    openjpeg_inc = subprocess.check_output(
        ['pkgconf', '--variable=includedir', 'libopenjp2'],
        text=True,
        ).strip()
    EXTENSIONS['jpeg2k']['include_dirs'].append(openjpeg_inc)
    EXTENSIONS['jpegxr']['include_dirs'].append(includedir +  'jxrlib')
    EXTENSIONS['jpegxl']['libraries'] = ['jxl', 'jxl_threads']
    EXTENSIONS['rcomp']['include_dirs'].append(includedir +   'cfitsio')
    EXTENSIONS['zopfli']['include_dirs'].append(includedir +  'zopfli')
    EXTENSIONS['lzham']['libraries'] = ['lzhamdll']
    