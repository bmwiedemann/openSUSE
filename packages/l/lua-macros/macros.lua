# RPM macros for Lua

# The major.minor version of Lua
%lua_version %(lua -e 'print(_VERSION)' | cut -d ' ' -f 2)

# compiled modules should go here
%lua_archdir %{_libdir}/lua/%{lua_version}

# pure Lua modules should go here
%lua_noarchdir %{_datadir}/lua/%{lua_version}

# lua includes folder
%lua_incdir %{_includedir}/lua%{lua_version}
