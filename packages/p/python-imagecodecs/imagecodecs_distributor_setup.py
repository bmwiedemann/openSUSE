# openSUSE extension setup to build python-imagecodecs

import os
import subprocess

def customize_build(EXTENSIONS, OPTIONS):

    print(f"Building with custom OpenSUSE config ({__file__})")

    includedir = os.getenv("INCDIR",'') + '/'

    del EXTENSIONS['apng']     # png-apng library not available
    del EXTENSIONS['brunsli']  # graphics/brunsli not in Factory
    del EXTENSIONS['jetraw']   # jetraw library not available
    del EXTENSIONS['lerc']     # LERC library not available
    del EXTENSIONS['lz4f']     # requires static linking
    del EXTENSIONS['lzo']      # lzokay not available
    del EXTENSIONS['mozjpeg']  # Win32 only
    del EXTENSIONS['pcodec']   # not available in Factory
    del EXTENSIONS['sperr']    # not available in Factory
    del EXTENSIONS['jpegxs']   # jxs not available in Factory
    del EXTENSIONS['sz3']      # SZ3c not available in Factory
    del EXTENSIONS['ultrahdr'] # uhdr not available in Factory
    
    EXTENSIONS['avif']['libraries'] = [
        'avif',
        'aom',
        'dav1d',
        'rav1e',
        'sharpyuv',
        'SvtAv1Enc',
    ]
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
    # gh#gohlke/imagecodecs#111
    EXTENSIONS['jpeg8']['sources'] = []
