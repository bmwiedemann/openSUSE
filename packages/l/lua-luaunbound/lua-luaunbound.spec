#
# spec file for package lua-luaunbound
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
%define mod_name luaunbound
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
Version:        1.0.0
Release:        0
License:        MIT
Group:          Development/Languages/Other
Summary:        This is a binding to libunbound for Lua
URL:            https://www.zash.se/luaunbound.html
Source0:        https://code.zash.se/dl/luaunbound/%{mod_name}-%{version}.tar.gz
Source1:        https://code.zash.se/dl/luaunbound/%{mod_name}-%{version}.tar.gz.asc
Source2:        lua-%{mod_name}.keyring
Patch0:         makefile.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  libunbound-devel
%lua_provides

%description
This is a binding to libunbound for Lua

%prep
%autosetup -n %{mod_name}-%{version} -p1

%build
%make_build CC=cc LUA_PC=lua LDLIBS="%(pkgconf --libs lua) -lunbound" MYCFLAGS="%{optflags}"

%install
%make_install LUA_LIBDIR=%{lua_archdir}

%files
%license LICENSE
%doc README.markdown
%{lua_archdir}/lunbound.so

%changelog
