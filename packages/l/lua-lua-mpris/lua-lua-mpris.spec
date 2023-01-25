#
# spec file for package lua-lua-mpris
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
%define mod_name lua-mpris
Version:        0.0+git20191025.2b12542
Release:        0
Summary:        MPRIS api for lua
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/antlarr/lua-mpris/
Source:         lua-mpris-%{version}.tar.xz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-lua-dbus
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
Requires:       %{flavor}
Requires:       %{flavor}-lua-dbus
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
MPRIS api for lua

%prep
%setup -q -n lua-mpris-%{version}

%build

%install
mkdir -p %{buildroot}%{lua_noarchdir}/lua-mpris
cp -Ra applet.lua client.lua init.lua %{buildroot}%{lua_noarchdir}/lua-mpris/

%files
%license LICENSE
%{lua_noarchdir}/lua-mpris

%changelog
