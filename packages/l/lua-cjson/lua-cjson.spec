#
# spec file for package lua-cjson
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define flavor @BUILD_FLAVOR@
%define mod_name cjson
Version:        2.1.0.16
Release:        0
Summary:        Lua JSON Encoding/Decoding
License:        MIT
URL:            https://github.com/openresty/lua-cjson
Source:         https://github.com/openresty/lua-%{mod_name}/archive/refs/tags/%{version}.tar.gz#/lua-%{mod_name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM test_environment.patch gh#mpx/lua-cjson#75 mcepl@suse.com
# Make it possible for tests to be influenced by the variables
Patch0:         test_environment.patch
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
Requires:       %{flavor}
BuildRequires:  %{flavor}-luarocks
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  perl
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
This is the Lua extension package for JSON encoding/decoding.

%prep
%autosetup -p1 -n lua-%{mod_name}-%{version}

%build
export CFLAGS="%{optflags}"
%cmake \
    -H.. -DCMAKE_C_FLAGS="%{optflags}" \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_COLOR_MAKEFILE=OFF \
    -DBUILD_STATIC_LIBS=OFF -DCMAKE_INSTALL_DO_STRIP=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DLUA_INCLUDE_DIR:PATH="%{lua_incdir}"
find ..

%cmake_build

%install
mkdir -p -m 755 \
    %{buildroot}%{lua_archdir} \
    %{buildroot}%{lua_noarchdir}/cjson
install -m755 build/cjson.so %{buildroot}%{lua_archdir}/
install -m644 lua/cjson/util.lua %{buildroot}%{lua_noarchdir}/cjson/

%check
rm -rf build
export LUA_CPATH="%{buildroot}%{lua_archdir}/?.so;;"
export LUA_PATH="%{buildroot}%{lua_noarchdir}/?.lua;%{buildroot}%{lua_noarchdir}/?/init.lua;;"
# gh#openresty/lua-cjson#120
export SKIP_TESTS="encode_keep_buffer"
( cd tests
perl ./genutf8.pl
lua -e 'print("Testing Lua CJSON version " .. require("cjson")._VERSION)'
# We have GNU/grep, so we don’t have to work around Solaris/grep limitations
./test.lua 2>/dev/null | grep -Ev "$SKIP_TESTS" \
    | grep -E -A 3 'FAIL|Summary' | grep -v 'PASS' | cut -c -150
)

%files
%{lua_archdir}/cjson.so
%dir %{lua_noarchdir}/cjson
%{lua_noarchdir}/cjson/util.lua

%changelog
