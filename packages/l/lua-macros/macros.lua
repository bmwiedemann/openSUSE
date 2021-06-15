# RPM macros for Lua

# The major.minor version of Lua
%lua_version %(lua -e 'print(_VERSION)' | cut -d ' ' -f 2)
%lua_version_nodots %(lua -e 'print(math.floor((%{lua_version}*10)))')

# compiled modules should go here
%lua_archdir %{_libdir}/lua/%{lua_version}

# pure Lua modules should go here
%lua_noarchdir %{_datadir}/lua/%{lua_version}

# lua includes folder
%lua_incdir %{_includedir}/lua%{lua_version}

# Lua default version
# -e: Exclude lua prefix
# -n: Specify name
%lua_provides(en:) \
%if "%{flavor}" == "lua54" \
%if 0%{?-n:1} \
Provides: %{-n*} = %{version}-%{release} \
Obsoletes: %{-n*} < %{version}-%{release} \
%else \
%if 0%{?-e:1} \
Provides: %{mod_name} = %{version}-%{release} \
Obsoletes: %{mod_name} < %{version}-%{release} \
%else \
Provides: lua-%{mod_name} = %{version}-%{release} \
Obsoletes: lua-%{mod_name} < %{version}-%{release} \
%endif \
%endif \
%endif \
%{nil}
