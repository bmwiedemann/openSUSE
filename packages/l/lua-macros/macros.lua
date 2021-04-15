# RPM macros for Lua

# The major.minor version of Lua
%lua_version %(lua -e 'print(_VERSION)' | cut -d ' ' -f 2)
%lua_version_nodots %(perl -e "print %{lua_version}*10")

# compiled modules should go here
%lua_archdir %{_libdir}/lua/%{lua_version}

# pure Lua modules should go here
%lua_noarchdir %{_datadir}/lua/%{lua_version}

# lua includes folder
%lua_incdir %{_includedir}/lua%{lua_version}

# Lua default version
# -e: Exclude lua prefix
%lua_provides(e) \
%if "%{flavor}" == "lua54" \
%if 0%{?-e:1} \
Provides: %{mod_name} = %{version}-%{release} \
Obsoletes: %{mod_name} < %{version}-%{release} \
%else \
Provides: lua-%{mod_name} = %{version}-%{release} \
Obsoletes: lua-%{mod_name} < %{version}-%{release} \
%endif \
%endif \
%{nil}
