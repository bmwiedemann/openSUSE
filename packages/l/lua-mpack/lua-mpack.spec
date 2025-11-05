#
# spec file for package lua-mpack
#
# Copyright (c) 2024 SUSE LLC
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
%define libmpack_version 1.0.5
%define mod_name mpack
Version:        1.0.13
Release:        0
Summary:        Implementation of MessagePack for Lua 5.1
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/libmpack/libmpack-lua
Source:         https://github.com/libmpack/libmpack-lua/archive/refs/tags/%{version}.tar.gz#/%{mod_name}-%{version}.tar.gz
# libmpack source is necessary to build lua-mpack, need to package mpack to Factory
Source1:        https://github.com/libmpack/libmpack/archive/refs/tags/%{libmpack_version}.tar.gz#/libmpack-%{libmpack_version}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  lua-macros
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
mpack is a binary serialization/RPC library that implements both the msgpack
and msgpack-rpc specifications.

%prep
%autosetup -p1 -n libmpack-lua-%{version}

( mkdir -p "mpack-src" && cd "mpack-src"
tar --extract --strip-components=1 --file %{SOURCE1} )

# Fix lua directory.
sed -i 's|LUA_CMOD_INSTALLDIR :=.*|LUA_CMOD_INSTALLDIR := $(shell echo "%{lua_archdir}")|g' Makefile

%build
make %{?_make_output_sync} %{?_smp_mflags} \
    USE_SYSTEM_LUA=yes \
    USE_SYSTEM_MPACK=no \
    LUA_IMPL="lua" \
    CFLAGS="%{optflags} -fPIC %(pkgconf --cflags --libs lua)"

%install
%make_install USE_SYSTEM_LUA=yes \
    LUA_CMOD_INSTALLDIR="%{lua_archdir}"

%files
%doc mpack-src/LICENSE-MIT README.md
%{lua_archdir}/mpack.so

%changelog
