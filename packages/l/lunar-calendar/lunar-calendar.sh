if [ -f "/usr/lib64/gtk-3.0/modules/liblunar-calendar-module.so" ]; then
    export GTK3_MODULES="${GTK3_MODULES:+$GTK3_MODULES:}lunar-calendar-module"
fi
