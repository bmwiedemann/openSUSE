#
# spec file for package lua-zlib
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
%define mod_name zlib
Version:        1.1
Release:        0
Summary:        Simple streaming interface to zlib for Lua
License:        MIT OR X11
Group:          Productivity/Archiving/Compression
Url:            https://github.com/brimworks/lua-zlib
Source:         https://github.com/brimworks/lua-zlib/archive/v%{version}.tar.gz#/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  zlib-devel
Requires:       %{flavor}
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
lua-zlib is a simple streaming interface to zlib for Lua.

%prep
%setup -q -n lua-zlib-%{version}

%build
make %{?_smp_mflags} linux \
  INCDIR="-I%{lua_incdir}" \
  LUAPATH="%{lua_noardir}" \
  LUACPATH="%{lua_archdir}" \
  CFLAGS="%{optflags} -fPIC"

%install
mkdir -p %{buildroot}/%{lua_archdir}
%make_install LUACPATH="%{buildroot}%{lua_archdir}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README
%{lua_archdir}/zlib.so

%changelog
