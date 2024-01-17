#
# spec file for package lua-luaevent
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
%define mod_name luaevent
Version:        0.4.6
Release:        0
Summary:        A binding of libevent to Lua
License:        MIT
Group:          System/Libraries
URL:            https://github.com/harningt/luaevent
Source:         https://github.com/harningt/luaevent/archive/v%{version}.tar.gz#/%{mod_name}-%{version}.tar.gz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
BuildRequires:  libevent-devel >= 1.4
Requires:       %{flavor}
Requires:       %{flavor}-luasocket
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
Provides:       %{flavor}-event = %{version}
Obsoletes:      %{flavor}-event < %{version}
%endif

%description
This is a binding of libevent to Lua. It will serve as a drop-in
replacement for copas, and eventually support more features
(async DNS, HTTP, RPC...).

%prep
%setup -q -n %{mod_name}-%{version}
sed -i \
    -e 's:-Wall -fpic:%{optflags} -fPIC:' \
    Makefile

%build
make %{?_make_output_sync} all \
    LUA_INC_DIR=%{lua_incdir}

%install
%make_install \
    LUA_INC_DIR=%{lua_incdir} \
    INSTALL_DIR_BIN=%{lua_archdir} \
    INSTALL_DIR_LUA=%{lua_noarchdir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc CHANGELOG README
%dir %{lua_archdir}/luaevent
%{lua_archdir}/luaevent/core.so
%{lua_noarchdir}/luaevent.lua

%changelog
