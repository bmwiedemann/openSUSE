#
# spec file for package lua-lualdap
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


%define flavor @BUILD_FLAVOR@%{nil}
%define mod_name lualdap
Version:        1.3.0
Release:        0
Summary:        Lua binding to OpenLDAP
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/lualdap/lualdap
Source0:        %{mod_name}-%{version}.tar.xz
BuildRequires:  %{flavor}-devel
BuildRequires:  lua-macros
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
Requires:       %{flavor}
%{lua_provides}
%if "%{flavor}" == ""
Name:           lua-lualdap
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-lualdap
%endif

%description
LuaLDAP is a simple interface from Lua to an LDAP client, in fact it is a bind to OpenLDAP client or ADSI

%prep
%autosetup -n %{mod_name}-%{version}

%build
make %{?_make_output_sync} %{?_smp_mflags} CFLAGS="%{optflags} -std=c99" LUA_LIBDIR=%{_libdir} LDAP_LIBDIR=%{_libdir} \
LBER_LIBDIR=%{_libdir} \
%{nil}

%install
%make_install INST_LIBDIR=%{lua_archdir}

%files
%license docs/license.md
%{lua_archdir}/lualdap.so

%changelog
