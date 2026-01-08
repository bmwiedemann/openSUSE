#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%bcond_without test
%define name_ext -test
%define debug_package %{nil}
%else
%bcond_with test
%define name_ext %{nil}
%endif
%define major_version 5.5
%define libname liblua5_5-5
Name:           lua55%{name_ext}
Version:        5.5.0
Release:        0
Summary:        Small Embeddable Language with Procedural Syntax
License:        MIT
Group:          Development/Languages/Other
URL:            https://www.lua.org
Source:         https://www.lua.org/ftp/lua-%{version}.tar.gz
Source1:        https://www.lua.org/tests/lua-%{version}-tests.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-SUSE tweak the buildsystem to produce what is needed for SUSE
Patch0:         lua-build-system.patch
# PATCH-FIX-UPSTREAM attrib_test.patch https://is.gd/6DYPgG mcepl@suse.com
# Fix failing test
Patch1:         attrib_test.patch
Patch2:         files_test.patch
Patch3:         main_test.patch
Patch6:         shared_link.patch
# PATCH-FIX-UPSTREAM inspect errno only after failure
Patch8:         execresult.patch
# PATCH-FIX-UPSTREAM libdir-luaconf.patch mcepl@suse.com
# Make the build system controlled only by the command line arguments
# (no need to modify src/luaconf.h "manually")
Patch9:         libdir-luaconf.patch
# PATCH-FIX-UPSTREAM 32bit-check.patch mcepl@suse.com
# fix 32-bit integer overflow in str_rep function
Patch10:         32bit-check.patch
BuildRequires:  lua-interpreter
Requires:       alts
Requires:       lua-interpreter
Provides:       lua = %{version}
Provides:       Lua(API) = %{major_version}
%if %{with test}
BuildRequires:  lua55
BuildRequires:  lua55-devel
%else
BuildRequires:  libtool
BuildRequires:  lua-macros
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
%endif

%description
Lua is a programming language originally designed for extending
applications, but is also frequently used as a general-purpose,
stand-alone language.

Lua combines procedural syntax (similar to Pascal) with
data description constructs based on associative arrays and extensible
semantics. Lua is dynamically typed, interpreted from byte codes, and
has automatic memory management, making it suitable for configuration,
scripting, and rapid prototyping. Lua is implemented as a small library
of C functions, written in ANSI C.

%package devel
Summary:        Development files for lua
License:        MIT
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{name} = %{version}
Requires:       lua-macros
Conflicts:      lua-devel
Provides:       lua-devel = %{version}
Provides:       Lua(devel) = %{major_version}
Provides:       pkgconfig(lua) = %{version}

%description devel
Lua is a programming language originally designed for extending
applications, but is also frequently used as a general-purpose,
stand-alone language.

This package contains files needed for embedding lua into your
application.

%package -n %{libname}
Summary:        The Lua integration library
License:        MIT
Group:          System/Libraries
Provides:       liblua5_5 = %{version}-%{release}
Obsoletes:      liblua5_5 < %{version}-%{release}
Provides:       %{name}-libs = %{version}
Obsoletes:      %{name}-libs < %{version}
# Compat as libtool changes the soname
%ifarch aarch64 x86_64 ppc64 ppc64le s390x riscv64
Provides:       liblua.so.5.5()(64bit)
%else
Provides:       liblua.so.5.5
%endif

%description -n %{libname}
Lua is a programming language originally designed for extending
applications, but is also frequently used as a general-purpose,
stand-alone language.

Lua combines procedural syntax (similar to Pascal) with
data description constructs based on associative arrays and extensible
semantics. Lua is dynamically typed, interpreted from byte codes, and
has automatic memory management, making it suitable for configuration,
scripting, and rapid prototyping. Lua is implemented as a small library
of C functions, written in ANSI C.

%package doc
Summary:        Documentation for Lua, a small embeddable language
License:        MIT
Group:          Documentation/HTML
BuildArch:      noarch
%if 0%{?suse_version} > 1315
Supplements:    (lua55 and patterns-base-documentation)
%endif

%description doc
Lua is a programming language originally designed for extending
applications, but is also frequently used as a general-purpose,
stand-alone language.

Lua combines procedural syntax (similar to Pascal) with
data description constructs based on associative arrays and extensible
semantics. Lua is dynamically typed, interpreted from byte codes, and
has automatic memory management, making it suitable for configuration,
scripting, and rapid prototyping. Lua is implemented as a small library
of C functions, written in ANSI C.

%prep
%setup -q -n lua-5.5.0 -a1
mv lua-5.5.0-tests testes
%autopatch -p1

%if %{without test}
# manpage
cat doc/lua.1  | sed 's/TH LUA 1/TH LUA%{major_version} 1/' > doc/lua%{major_version}.1
cat doc/luac.1 | sed 's/TH LUAC 1/TH LUAC%{major_version} 1/' > doc/luac%{major_version}.1
%endif

%build
%if %{without test}
MYCFLAGS="%{optflags} -std=gnu99 -D_GNU_SOURCE -fPIC -DLUA_COMPAT_MODULE" 
MYCFLAGS="${MYCFLAGS} -DLUA_CDIR=\"%{_libdir}/lua/5.5/\""
export MYCFLAGS
%make_build linux -C src \
    CC="cc" LIBDIR="%{_libdir}" \
    LDFLAGS="-lm" \
    MYCFLAGS="${MYCFLAGS}"\
    V=%{major_version} \
    LIBTOOL="libtool --quiet"
%endif

%install
%if %{without test}
%make_install \
    LIBTOOL="libtool --quiet" \
    INSTALL_TOP="%{buildroot}%{_prefix}" \
    INSTALL_LIB="%{buildroot}%{_libdir}" \
    INSTALL_MAN="%{buildroot}%{_mandir}/man1"

find %{buildroot} -type f -name "*.la" -delete -print

# create pkg-config file
cat > lua%{major_version}.pc <<-EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/lua%{major_version}
INSTALL_LMOD=%{_datadir}/lua/%{major_version}
INSTALL_CMOD=%{_libdir}/lua/%{major_version}

Name:           Lua %{major_version}
Description: An Extensible Extension Language
Version:        %{version}
Libs: -llua%{major_version} -lm
Cflags: -I\${includedir}
EOF
install -D -m 644 lua%{major_version}.pc %{buildroot}%{_libdir}/pkgconfig/lua%{major_version}.pc

# alternatives - create configuration file
mkdir -p %{buildroot}%{_datadir}/libalternatives/lua
cat > %{buildroot}%{_datadir}/libalternatives/lua/55.conf <<EOF
binary=%{_bindir}/lua5.5
man=lua5.5
EOF
mkdir -p %{buildroot}%{_datadir}/libalternatives/luac
cat > %{buildroot}%{_datadir}/libalternatives/luac/55.conf <<EOF
binary=%{_bindir}/luac5.5
man=luac5.5
EOF

# Compat link with older unprefixed library and with soname 0 from deb/etc
ln -s %{_libdir}/liblua%{major_version}.so.%{major_version}.0 %{buildroot}%{_libdir}/liblua%{major_version}.so.%{major_version}
ln -s %{_libdir}/liblua%{major_version}.so.%{major_version}.0 %{buildroot}%{_libdir}/liblua%{major_version}.so.0
ln -s %{_libdir}/liblua%{major_version}.so.%{major_version}.0 %{buildroot}%{_libdir}/liblua.so.%{major_version}

# We don’t create alternatives for -devel content, just conflict those
ln -s %{_libdir}/liblua%{major_version}.so %{buildroot}%{_libdir}/liblua.so
ln -s %{_libdir}/pkgconfig/lua%{major_version}.pc %{buildroot}%{_libdir}/pkgconfig/lua.pc
%endif

%check
%if %{with test}
cd testes
pushd libs
%make_build all LUA_DIR=%{_includedir}/lua%{major_version}
cp *.so ..
popd
LD_LIBRARY_PATH=%{_libdir} %{_bindir}/lua%{major_version} all.lua
%endif

%if %{without test}
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%if %{without test}
%files
%doc README
%dir %{_libdir}/lua
%dir %{_libdir}/lua/%{major_version}
%dir %{_datadir}/lua
%dir %{_datadir}/lua/%{major_version}
%{_bindir}/lua%{major_version}
%{_bindir}/luac%{major_version}
%{_mandir}/man1/lua%{major_version}.1%{?ext_man}
%{_mandir}/man1/luac%{major_version}.1%{?ext_man}
%{_datadir}/libalternatives/lua/55.conf
%{_datadir}/libalternatives/luac/55.conf

%files -n %{libname}
%{_libdir}/liblua%{major_version}.so.*
%{_libdir}/liblua.so.*

%files devel
%dir %{_includedir}/lua%{major_version}
%{_includedir}/lua%{major_version}/lauxlib.h
%{_includedir}/lua%{major_version}/lua.h
%{_includedir}/lua%{major_version}/lua.hpp
%{_includedir}/lua%{major_version}/luaconf.h
%{_includedir}/lua%{major_version}/lualib.h
%{_libdir}/liblua%{major_version}.so
%{_libdir}/pkgconfig/lua%{major_version}.pc
%{_libdir}/liblua.so
%{_libdir}/pkgconfig/lua.pc

%files doc
%doc doc/*

%endif

%changelog
