#
# spec file for package lua-compat-5.3
#
# Copyright (c) 2022 SUSE LLC
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
%define mod_name lua-compat-5.3
# bit32 (dropped in 5.4) is the native Lua 5.2 bit manipulation library, in the version
# from Lua 5.3; it is compatible with Lua 5.1, 5.2 and 5.3.
%if "%{lua_version}" >= "5.4" || "%{lua_version}" < "5.2"
%bcond_with bit32
%else
%bcond_without bit32
%endif
%define mversion 0.10
Version:        %{mversion}
Release:        0
Summary:        Lua-5.3-style APIs for Lua 5.2 and 5.1
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/keplerproject/lua-compat-5.3
Source:         https://github.com/keplerproject/lua-compat-5.3/archive/v%{version}.tar.gz#$/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  lua-macros
BuildRequires:  pkgconfig
Requires:       %{flavor}
%lua_provides -e
%if %{without bit32}
Requires:       %{flavor}-bit32
%endif
%if "%{flavor}" == ""
Name:           lua-compat-5.3
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-compat-5.3
%endif

%description
This package provides terminal operations for Lua

%if %{without bit32}
%package -n %{flavor}-bit32
Version:        5.3.5.1
Release:        0
Summary:        Lua bit manipulation library
Group:          Development/Libraries/Other
%lua_provides -n lua-bit32

%description -n %{flavor}-bit32
bit32 is the native Lua 5.2 bit manipulation library, in the version
from Lua 5.3; it is compatible with Lua 5.1, 5.2 and 5.3.
%endif

%prep
%autosetup -n %{mod_name}-%{mversion}

%build
export CC="${COMPILER:-gcc}" DEF="" SRC="" CFLAGS="-Wall -Wextra $(pkg-config --cflags lua%{lua_version}) -Ic-api -O2 -fPIC"
if [ "x${EXTERNAL:-}" = xtrue ]; then
    export DEF="-DCOMPAT53_PREFIX=compat53" SRC="c-api/compat-5.3.c"
fi
gcc ${CFLAGS} -Iinclude ${DEF} -shared -o utf8.so lutf8lib.c
gcc ${CFLAGS} -Iinclude ${DEF} -shared -o table.so ltablib.c
gcc ${CFLAGS} -Iinclude ${DEF} -shared -o string.so lstrlib.c

%if %{without bit32}
${CC} ${CFLAGS} -Iinclude -DLUA_COMPAT_BITLIB -shared -o bit32.so lbitlib.c
%endif

%install
mkdir -p %{buildroot}%{lua_archdir}/compat53
install -Dm0644 utf8.so %{buildroot}%{lua_archdir}/compat53
install -Dm0644 table.so %{buildroot}%{lua_archdir}/compat53
install -Dm0644 string.so %{buildroot}%{lua_archdir}/compat53
mkdir -p %{buildroot}%{lua_noarchdir}/compat53
install -Dm0644 compat53/* %{buildroot}%{lua_noarchdir}/compat53
mkdir -p %{buildroot}%{lua_incdir}/c-api
install -Dm0644 c-api/* %{buildroot}%{lua_incdir}/c-api
install -Dm0644 lprefix.h %{buildroot}%{lua_incdir}

%if %{without bit32}
install -v -m 0644 -D -p -t %{buildroot}%{lua_archdir} bit32.so
%endif

%files
%license LICENSE
%doc README.md
%{lua_archdir}/compat53
%{lua_noarchdir}/compat53
%dir %{lua_incdir}
%{lua_incdir}/*

%if %{without bit32}
%files -n %{flavor}-bit32
%{lua_archdir}/bit32.so
%endif

%changelog
