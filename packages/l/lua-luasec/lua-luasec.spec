#
# spec file for package lua-luasec
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define flavor @BUILD_FLAVOR@
%define mod_name luasec
Version:        0.6
Release:        0
Summary:        A Lua binding for OpenSSL
License:        MIT
Group:          Productivity/Networking/Other
Url:            https://github.com/brunoos/luasec
Source:         https://github.com/brunoos/luasec/archive/%{mod_name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM build with openssl 1.1.0 (taken from Fedora)
Patch0:         lua-sec-0.6-openssl_110.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-luasocket
BuildRequires:  libopenssl-devel
Requires:       %{flavor}
Requires:       %{flavor}-luasocket
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
It is a binding for OpenSSL library to provide TLS/SSL communication.
It takes an already established TCP connection and creates a secure
session between the peers.

%prep
%setup -q -n luasec-luasec-%{version}
%patch0 -p1

%build
make %{?_smp_mflags} linux \
  CFLAGS="%{optflags} -fPIC -I%{lua_incdir} -I. -DWITH_LUASOCKET -DLUASOCKET_DEBUG -DLUA_COMPAT_APIINTCASTS"

%install
%make_install LUAPATH=%{lua_noarchdir} LUACPATH=%{lua_archdir}

%files
%doc CHANGELOG LICENSE README.md
%{lua_archdir}/ssl.so
%{lua_noarchdir}/ssl.lua
%{lua_noarchdir}/ssl/

%changelog
