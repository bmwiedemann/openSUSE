#
# spec file for package lua-mpack
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.0.6
Release:        0
Summary:        Implementation of MessagePack for Lua 5.1
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/libmpack/libmpack-lua
Source:         https://github.com/libmpack/libmpack-lua/archive/%{version}.tar.gz
# libmpack source is necessary to build lua-mpack, next release should build
# fine against system version
# The latest source can be downloaded from: https://github.com/libmpack/libmpack
Source1:        https://github.com/libmpack/libmpack/archive/%{libmpack_version}/libmpack-%{libmpack_version}.tar.gz
# PATCH-FIX-UPSTREAM lua51-mpack-fix-gcc7.patch gh#libmpack/libmpack-lua#3 -- Fix compilation error when using GCC7.
Patch0:         lua51-mpack-fix-gcc7.patch
# PATCH-FIX-UPSTREAM lua51-mpack-fix-compilation.patch gh#libmpack/libmpack-lua#2 -- Fix compilation error when using `USE_SYSTEM_LUA=1`.
Patch1:         lua51-mpack-fix-compilation.patch
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
BuildRequires:  gcc
BuildRequires:  libtool
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
%setup -q -n libmpack-lua-%{version}
%patch0 -p1
%patch1 -p1

# Extract the libmpack source to the right directory.
mkdir -p mpack-src
pushd mpack-src
cp %{SOURCE1} ./
tar --strip-components=1 -xzf libmpack-%{libmpack_version}.tar.gz
popd

# Fix lua directory.
sed -i 's|LUA_CMOD_INSTALLDIR :=.*|LUA_CMOD_INSTALLDIR := $(shell echo "%{lua_archdir}")|g' Makefile

%build
make %{?_make_output_sync} %{?_smp_mflags} \
    USE_SYSTEM_LUA=yes \
    MPACK_LUA_VERSION=%{lua_version} \
    CFLAGS="%{optflags} -fPIC"

%install
%make_install USE_SYSTEM_LUA=yes

%files
%doc mpack-src/LICENSE-MIT README.md
%dir %{lua_archdir}
%{lua_archdir}/*

%changelog
