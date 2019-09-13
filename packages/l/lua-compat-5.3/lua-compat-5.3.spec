#
# spec file for package lua-compat-5.3
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define mod_name lua-compat-5.3
Version:        0.7
Release:        0
Summary:        Lua-5.3-style APIs for Lua 5.2 and 5.1
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/keplerproject/lua-compat-5.3
Source:         https://github.com/keplerproject/lua-compat-5.3/archive/v%{version}.tar.gz#$/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  pkgconfig
Requires:       %{flavor}
%if "%{flavor}" == ""
Name:           lua-compat-5.3
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-compat-5.3
%endif

%description
This package provides terminal operations for Lua

%prep
%setup -q -n %{mod_name}-%{version}

%build
export CC="${COMPILER:-gcc}" DEF="" SRC="" CFLAGS="-Wall -Wextra $(pkg-config --cflags lua%{lua_version}) -Ic-api -O2 -fPIC"
if [ "x${EXTERNAL:-}" = xtrue ]; then
    export DEF="-DCOMPAT53_PREFIX=compat53" SRC="c-api/compat-5.3.c"
fi
${CC} ${CFLAGS} -Iinclude ${DEF} -shared -o testmod.so tests/testmod.c ${SRC}
gcc ${CFLAGS} -Iinclude ${DEF} -shared -o compat53.so ltablib.c lutf8lib.c lstrlib.c ${SRC}


%install
install -v -m 0644 -D -p -t %{buildroot}%{lua_incdir}/c-api/ c-api/*
install -v -m 0644 -p -t %{buildroot}%{lua_incdir} lprefix.h

install -v -D -m 0644 -p -t %{buildroot}%{lua_archdir} testmod.so
cp -v -r -p compat53.so %{buildroot}%{lua_archdir}

%files
%license LICENSE
%doc README.md
%{lua_archdir}/*.so
%{lua_incdir}/*

%changelog
