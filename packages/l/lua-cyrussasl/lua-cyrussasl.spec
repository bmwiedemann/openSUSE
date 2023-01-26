#
# spec file for package lua-cyrussasl
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
%define mod_name cyrussasl
Version:        1.1.0
Release:        0
Summary:        Cyrus SASL library for Lua 5.1+
License:        BSD-3-Clause
URL:            https://github.com/JorjBauer/lua-cyrussasl
Source:         https://github.com/JorjBauer/lua-cyrussasl/archive/refs/tags/v%{version}.tar.gz#$/%{mod_name}-%{version}.tar.gz
BuildRequires:  lua-macros
BuildRequires:  %{flavor}-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  git
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
Provides Lua bindings for Cyrus SASL authentication library.

%prep
%autosetup -n lua-%{mod_name}-%{version}

%build
export cmd='cc %{optflags} -fpic -I%{lua_incdir} -fno-common'
$cmd -DVERSION="\"1.1\"" -c cyrussasl.c -o cyrussasl.o
$cmd -DVERSION="\"1.1\"" -c luaabstract.c -o luaabstract.o
$cmd -DVERSION="\"1.1\"" -c context.c -o context.o
cc -Wl,--no-as-needed -shared -fpic -lsasl2 -o cyrussasl.so cyrussasl.o luaabstract.o context.o

%install
mkdir -p %{buildroot}%{lua_archdir}
cp cyrussasl.so %{buildroot}%{lua_archdir}

%files
%license LICENSE
%doc README
%{lua_archdir}/%{mod_name}.so

%changelog
