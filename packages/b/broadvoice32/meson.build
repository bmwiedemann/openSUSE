#meson
project('BROADVOICE32', 'c', version : '1.2')
bvinclude = include_directories('bv32', 'bvcommon')
libm = meson.get_compiler('c').find_library('libm')
bv32_source_files = ['bvcommon/a2lsp.c', 'bvcommon/allpole.c', 'bvcommon/allzero.c', 'bvcommon/autocor.c', 'bvcommon/cmtables.c', 'bvcommon/levdur.c', 'bvcommon/lsp2a.c', 'bvcommon/ptdec.c', 'bvcommon/stblchck.c', 'bvcommon/stblzlsp.c', 'bvcommon/utility.c', 'bv32/bitpack.c', 'bv32/coarptch.c', 'bv32/decoder.c', 'bv32/encoder.c', 'bv32/excdec.c', 'bv32/excquan.c', 'bv32/fineptch.c', 'bv32/gaindec.c', 'bv32/gainquan.c', 'bv32/levelest.c', 'bv32/lspdec.c', 'bv32/lspquan.c', 'bv32/plc.c', 'bv32/ptquan.c', 'bv32/tables.c']
broadvoice32_source_files = ['bv32/bv.c', 'bv32/g192.c']
add_global_arguments('-DWMOPS=0', '-DG192BITSTREAM=0', language : 'c')
link_libraries = static_library('bv32', bv32_source_files, include_directories : bvinclude, dependencies : libm, install : get_option('static_libs'))
if get_option('shared_libs')
  link_libraries = shared_library('bv32', bv32_source_files, include_directories : bvinclude, dependencies : libm, install : true)
endif
if get_option('build_tools')
  executable('BroadVoice32', broadvoice32_source_files, include_directories : bvinclude, dependencies : libm, link_with : link_libraries, install : true)
endif
install_headers('bv32/bitpack.h','bv32/bv32.h','bv32/bv32cnst.h','bv32/bv32externs.h','bv32/bv32strct.h','bv32/g192.h', subdir : 'bv32-floatingpoint/bv32')
install_headers('bvcommon/bvcommon.h','bvcommon/typedef.h','bvcommon/utility.h', subdir : 'bv32-floatingpoint/bvcommon')
