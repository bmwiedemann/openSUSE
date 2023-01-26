#
# spec file
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2009 florian.leparoux@gmail.com
# Copyright (c) 2012 Togan Muftuoglu toganm@opensuse.org
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
%define mod_name    luaexpat
Version:        1.4.1
Release:        0
Summary:        A SAX XML parser based on the Expat library
License:        MIT
Group:          Productivity/Networking/Other
URL:            http://matthewwild.co.uk/projects/luaexpat/
Source:         https://github.com/lunarmodules/luaexpat/archive/%{version}/%{mod_name}-%{version}.tar.gz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
BuildRequires:  libexpat-devel
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
LuaExpat is a SAX XML parser based on the Expat library.

%prep
%setup -q -n %{mod_name}-%{version}

%build
make %{?_smp_mflags} \
    PREFIX="%{_prefix}" \
    LUA_V=%{lua_version} \
    LUA_CDIR="%{lua_archdir}" \
    LUA_INC="-I%{lua_incdir}" \
    CFLAGS="%{optflags}"

%install
%make_install \
    PREFIX="%{_prefix}" \
    LUA_CDIR="%{lua_archdir}" \
    LUA_LDIR="%{lua_noarchdir}"

%files
%defattr(-,root,root)
%license LICENSE
%{lua_archdir}/lxp.so
%{lua_noarchdir}/lxp

%changelog
