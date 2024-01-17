#
# spec file for package lua-lgi
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2012 Adam Mizerski <adam@mizerski.pl>
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
%define mod_name lgi
Version:        0.9.2
Release:        0
Summary:        Lua bindings to GObject libraries
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/pavouk/lgi
Source0:        https://github.com/pavouk/%{mod_name}/archive/%{version}.tar.gz#/%{mod_name}-%{version}.tar.gz
Patch:          lua54.patch
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.10.8
BuildRequires:  pkgconfig(libffi)
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
Dynamic Lua binding to any library which is introspectable
using gobject-introspection. Allows using GObject-based libraries
directly from Lua.

%package doc
Summary:        Lua bindings to GObject libraries - documentation and samples
Group:          Documentation/Other

%description doc
Dynamic Lua binding to any library which is introspectable
using gobject-introspection. Allows using GObject-based libraries
directly from Lua.

%prep
%autosetup -n %{mod_name}-%{version} -p1

%build
make %{?_smp_mflags} V=1 \
  LUA_CFLAGS=" -I%{lua_incdir}" \
  COPTFLAGS="%{optflags}" \

%install
%make_install \
  PREFIX=%{_prefix} \
  LUA_LIBDIR=%{lua_archdir} \
  LUA_SHAREDIR=%{lua_noarchdir}

%files
%if 0%{?suse_version} >= 1500
%license LICENSE
%else
%doc LICENSE
%endif
%doc README.md
%{lua_archdir}/%{mod_name}/
%{lua_noarchdir}/%{mod_name}.lua
%{lua_noarchdir}/%{mod_name}/

%files doc
%doc docs samples tools

%changelog
