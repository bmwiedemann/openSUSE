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
Version:        2.1.0
Release:        0
Summary:        Lua JSON Encoding/Decoding
License:        MIT
URL:            https://www.kyne.com.au/~mark/software/lua-cjson.php
Source0:        http://www.kyne.com.au/~mark/software/download/lua-cjson-%{version}.tar.gz
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

make %{?_make_output_sync} %{?_smp_mflags} \
    CC="gcc" \
    PREFIX="%{_prefix}" \
    LUA_INCLUDE_DIR=%{lua_incdir}

%install
mkdir -p -m 755 \
    %{buildroot}%{lua_archdir} \
    %{buildroot}%{lua_noarchdir}/cjson
install -m755 build/cjson.so %{buildroot}%{lua_archdir}/
install -m644 lua/cjson/util.lua %{buildroot}%{lua_noarchdir}/cjson/

%check
rm -rf build
export CFLAGS="%{optflags}" PREFIX="%{_prefix}" \
    LUA_INCLUDE_DIR="%{lua_incdir}" LUA_CMODULE_DIR="%{lua_archdir}" LUA_MODULE_DIR="%{lua_noarchdir}"
./runtests.sh

%files
%{lua_archdir}/cjson.so
%dir %{lua_noarchdir}/cjson
%{lua_noarchdir}/cjson/util.lua

%changelog
