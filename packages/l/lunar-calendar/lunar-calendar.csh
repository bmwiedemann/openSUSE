if ( -f "/usr/lib64/gtk-3.0/modules/liblunar-calendar-module.so" ) then
    if ( ! $?GTK3_MODULES ) set GTK3_MODULES=""
    if ( $?GTK3_MODULES ) setenv GTK3_MODULES "$GTK3_MODULES\:"
    setenv GTK3_MODULES "${GTK3_MODULES}lunar-calendar-module"
endif
