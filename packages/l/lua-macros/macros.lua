# RPM macros for Lua

# The major.minor version of Lua
%lua_version %{lua:
local f = io.popen("lua -e 'print(_VERSION)'")
local output = f:read("*a")
f:close()
local ver = output:match("Lua (%d%.%d)")
print(ver)
}
%lua_version_nodots %{lua:
  local ver = rpm.expand("%{lua_version}")
  local nodots = ver:gsub("%.", "")
  print(nodots)
}
# compiled modules should go here
%lua_archdir %{lua:
  local handle = io.popen("pkgconf --variable=INSTALL_CMOD lua 2>/dev/null")
  local result = handle:read("*a")
  handle:close()
  result = result:gsub("^%s*(.-)%s*$", "%1")
  print(result)
}
# pure Lua modules should go here
%lua_noarchdir %{lua:
local output = ""
local f = io.popen("pkgconf --variable=INSTALL_LMOD lua 2>/dev/null")
if f ~= nil then
    output = f:read("*a"):gsub("^%s*(.-)%s*$", "%1")
    f:close()
end
if output:len() > 0 then
    print(output)
    return
end
print(rpm.expand("%{_datadir}/lua/%{lua_version}"))
}
# lua includes folder
%lua_incdir %{lua:
  local handle = io.popen("pkgconf --variable=includedir lua 2>/dev/null")
  local result = handle:read("*a")
  handle:close()
  result = result:gsub("^%s*(.-)%s*$", "%1")
  print(result)
}
%lua_version_default %{lua:
local result = 5.4
local ver = rpm.expand("%{?suse_version}")
if #ver > 0 then
    ver = tonumber(ver)
    if ver < 1500 then
        result = 5.1
    elseif ver < 1600 then
        result = 5.3
    end
end
print(result)
}
# Define a conditional that evaluates true when building for the default Lua version
%lua_version_default_nodots %{lua:
  local ver = rpm.expand("%{lua_version_default}")
  local nodots = ver:gsub("%.", "")
  print(nodots)
}
# Lua default version
# This REQUIRES macro %{mod_name} to be defined.
# -e: Exclude lua prefix
# -n: Specify name
%lua_provides(en:) %{lua:
local mod_name = rpm.expand("%{?mod_name}")
if mod_name == "" then
    print("-- Error: %{mod_name} is not defined!")
    return
end
print([[
%if "%{lua_version_nodots}" == "%{lua_version_default_nodots}"
%if 0%{?-n:1}
Provides: %{-n*} = %{version}-%{release}
Obsoletes: %{-n*} < %{version}-%{release}
%else
%if 0%{?-e:1}
Provides: %{mod_name} = %{version}-%{release}
Obsoletes: %{mod_name} < %{version}-%{release}
%else
Provides: lua-%{mod_name} = %{version}-%{release}
Obsoletes: lua-%{mod_name} < %{version}-%{release}
%endif
%endif
%endif
]])
}

# LuaRocks
%luarocks_build \
luarocks --lua-version "%{lua_version}" make --deps-mode none --pack-binary-rock

%luarocks_treedir %{_prefix}/lib/luarocks/rocks-%{lua_version}

%luarocks_install \
  %{_rpmconfigdir}/install-lua-rock.sh "%{lua_version}" "%{buildroot}%{_prefix}" "%{buildroot}%{luarocks_treedir}/%{mod_name}"
