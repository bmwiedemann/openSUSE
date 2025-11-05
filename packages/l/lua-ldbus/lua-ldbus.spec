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
Version:        0.0+git20250404.5cc933b
Release:        0
Summary:        Lua bindings to dbus
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/daurnimator/ldbus
Source:         lua-ldbus-%{version}.tar.xz
BuildRequires:  %{flavor}-devel
BuildRequires:  lua-macros
Requires:       %{flavor}
BuildRequires:  pkgconfig(dbus-1)
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

%build
cd src
make %{?_make_output_sync} %{?_smp_mflags} LUA_PKGNAME="lua" LUA_LIBDIR="%{lua_archdir}"

%install
cd src
%make_install LUA_LIBDIR='%{lua_archdir}'

%files
%license LICENSE
%{lua_archdir}/ldbus.so

%changelog
