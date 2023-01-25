#
# spec file for package lua-ldbus
#
# Copyright (c) 2023 SUSE LLC
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
%define mod_name ldbus
Version:        0.0+git20190816.9e176fe
Release:        0
Summary:        Lua bindings to dbus
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/daurnimator/ldbus/
Source:         lua-ldbus-%{version}.tar.xz
Patch0:         lua54.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  lua-macros
Requires:       %{flavor}
%if 0%{?suse_version} < 1330
BuildRequires:  dbus-1-devel
%else
BuildRequires:  pkgconfig(dbus-1)
%endif
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
ldbus is a C binding to dbus for Lua.

%prep
%autosetup -n lua-ldbus-%{version} -p1

%if "%{flavor}" != "lua53"
sed -i -e "s/lua5.3/lua%{lua_version}/" src/Makefile
%endif

%build
%if 0%{?suse_version} < 1330
export CFLAGS="-I/usr/include/lua%{lua_version} -I/usr/include/dbus-1.0 -I/usr/lib64/dbus-1.0/include"
%if "%{flavor}" != "lua53"
export CFLAGS="$CFLAGS -Ivendor/compat-5.3"
%endif
%endif
cd src
make %{?_make_output_sync} %{?_smp_mflags}

%install
cd src
%make_install LUA_LIBDIR='$(DESTDIR)%{lua_archdir}'

%files
%license LICENSE
%{lua_archdir}/ldbus.so

%changelog
