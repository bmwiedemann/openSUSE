#
# spec file for package lua-BitOp
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
%define mod_name    BitOp
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
Version:        1.0.2
Release:        0
Summary:        Lua Bit Operations Module
License:        MIT
Group:          Development/Libraries/Other
URL:            https://bitop.luajit.org/index.html
Source:         http://bitop.luajit.org/download/LuaBitOp-%{version}.tar.gz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
BuildRequires:  gcc
Requires:       %{flavor}
%lua_provides
Obsoletes:      %{name}-doc < %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}

%description
Lua BitOp is a C extension module for Lua 5.1/5.2 which adds bitwise operations
on numbers.

%prep
%setup -q -n LuaBitOp-%{version}

%build
export CFLAGS="%{optflags} -I%{lua_incdir}"
make %{?_make_output_sync} %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{lua_archdir}
install bit.so %{buildroot}%{lua_archdir}

%files
%dir %{lua_archdir}
%{lua_archdir}/*
%doc README

%changelog
