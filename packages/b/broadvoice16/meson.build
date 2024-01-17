#meson
project('BROADVOICE16', 'c', version : '1.2')
bvinclude = include_directories('bv16', 'bvcommon')
libm = meson.get_compiler('c').find_library('libm')
bv16_source_files = ['bvcommon/a2lsp.c', 'bvcommon/allpole.c', 'bvcommon/allzero.c', 'bvcommon/autocor.c', 'bvcommon/cmtables.c', 'bvcommon/levdur.c', 'bvcommon/lsp2a.c', 'bvcommon/ptdec.c', 'bvcommon/stblchck.c', 'bvcommon/stblzlsp.c', 'bvcommon/utility.c', 'bv16/bitpack.c', 'bv16/coarptch.c', 'bv16/decoder.c', 'bv16/encoder.c', 'bv16/excdec.c', 'bv16/excquan.c', 'bv16/fineptch.c', 'bv16/gaindec.c', 'bv16/gainquan.c', 'bv16/levelest.c', 'bv16/lspdec.c', 'bv16/lspquan.c', 'bv16/plc.c', 'bv16/postfilt.c', 'bv16/ptquan.c', 'bv16/tables.c']
broadvoice16_source_files = ['bv16/bv.c', 'bv16/g192.c']
add_global_arguments('-DWMOPS=0', '-DG192BITSTREAM=0', language : 'c')
link_libraries = static_library('bv16', bv16_source_files, include_directories : bvinclude, dependencies : libm, install : get_option('static_libs'))
if get_option('shared_libs')
  link_libraries = shared_library('bv16', bv16_source_files, include_directories : bvinclude, dependencies : libm, install : true)
endif
if get_option('build_tools')
  executable('BroadVoice16', broadvoice16_source_files, include_directories : bvinclude, dependencies : libm, link_with : link_libraries, install : true)
endif
install_headers('bv16/bitpack.h','bv16/bv16.h','bv16/bv16cnst.h','bv16/bv16externs.h','bv16/bv16strct.h','bv16/g192.h','bv16/postfilt.h', subdir : 'bv16-floatingpoint/bv16')
install_headers('bvcommon/bvcommon.h','bvcommon/typedef.h','bvcommon/utility.h', subdir : 'bv16-floatingpoint/bvcommon')
