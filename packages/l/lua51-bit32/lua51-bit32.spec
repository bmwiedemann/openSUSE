#
# spec file for package lua51-bit32
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define flavor lua51
%define flavor_dec $(c=%{flavor}; echo ${c:0:-1}.${c: -1})
%define mod_name bit32
Name:           %{flavor}-%{mod_name}
Version:        5.3.0
Release:        0
Summary:        Backport of Lua bit manipulation library introduced in 5.2
License:        MIT
Group:          Development/Languages/Other
URL:            https://luarocks.org/modules/siffiejoe/bit32
Source0:        https://github.com/keplerproject/lua-compat-5.2/archive/bitlib-%{version}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  libtool
Requires:       %{flavor}

%description
bit32 is the native Lua 5.2 bit manipulation library, in the version
from Lua 5.3; it is compatible with Lua 5.1, 5.2 and 5.3.

%prep
%setup -q -n lua-compat-5.2-bitlib-%{version}

%build
gcc %{optflags} -I/usr/include -I./c-api \
    $(pkg-config --cflags --libs %{flavor_dec}) \
    lbitlib.c -shared -fPIC -o bit32.so


%install
install -d %{buildroot}%{lua_archdir}
install -p bit32.so %{buildroot}%{lua_archdir}/


%files
%license LICENSE
%doc README.md
%{lua_archdir}/bit32.so

%changelog
