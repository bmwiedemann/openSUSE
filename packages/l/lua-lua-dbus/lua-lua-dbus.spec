#
# spec file for package lua-lua-dbus
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
%define mod_name lua-dbus
Version:        0.0+git20170818.8fe38d0
Release:        0
Summary:        Convenient dbus api for lua
License:        MIT
Group:          Development/Libraries/Other
Url:            https://github.com/antlarr/lua-dbus/
Source:         lua-dbus-%{version}.tar.xz
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-ldbus
BuildRequires:  pkgconfig(dbus-1)
Requires:       %{flavor}
Requires:       %{flavor}-ldbus
%if "%{flavor}" == "lua53"
Provides:       lua-%{mod_name} = %{version}
Obsoletes:      lua-%{mod_name} < %{version}
%endif
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
lua-dbus is a convenient lua api for dbus

%prep
%setup -q -n lua-dbus-%{version}

%build
:

%install
mkdir -p %{buildroot}%{lua_noarchdir}/lua-dbus
cp -Ra awesome  init.lua  interface.lua %{buildroot}%{lua_noarchdir}/lua-dbus/

%files
%doc LICENSE
%{lua_noarchdir}/lua-dbus

%changelog
