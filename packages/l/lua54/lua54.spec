#
# spec file for package lua54
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

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define name_ext -test
%define debug_package %{nil}
%else
%define name_ext %{nil}
%endif
%define major_version 5.4
%define libname liblua5_4-5

Name:           lua54%{name_ext}
Version:        5.4.4
Release:        0
Summary:        Small Embeddable Language with Procedural Syntax
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
URL:            http://www.lua.org
Source:         http://www.lua.org/ftp/lua-%{version}.tar.gz
Source1:        http://www.lua.org/tests/lua-%{version}-tests.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-SUSE tweak the buildsystem to produce what is needed for SUSE
Patch0:         lua-build-system.patch
# PATCH-FIX-UPSTREAM attrib_test.patch https://is.gd/6DYPgG mcepl@suse.com
# Fix failing test
Patch1:         attrib_test.patch
Patch2:         files_test.patch
Patch3:         main_test.patch
Patch6:         shared_link.patch
# PATCH-FIX-UPSTREAM luabugsX.patch https://www.lua.org/bugs.html#5.4.4-X
Patch7:         luabugs1.patch
Patch8:         luabugs2.patch
Patch9:         luabugs3.patch
Patch10:        luabugs4.patch
Patch11:        luabugs5.patch
Patch12:        luabugs6.patch
Patch13:        luabugs7.patch
Patch14:        luabugs8.patch
Patch15:        luabugs9.patch
#
%if "%{flavor}" == "test"
BuildRequires:  lua54
%else
BuildRequires:  libtool
BuildRequires:  lua-macros
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       lua = %{version}
Obsoletes:      lua < %{version}
Provides:       Lua(API) = %{major_version}

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
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
# Compat as libtool changes the soname
%ifarch aarch64 x86_64 ppc64 ppc64le s390x riscv64
Provides:       liblua.so.5.4()(64bit)
%else
Provides:       liblua.so.5.4
%endif
Provides:       liblua5_4 = %{version}-%{release}
Obsoletes:      liblua5_4 < %{version}-%{release}
Provides:       %{name}-libs = %{version}
Obsoletes:      %{name}-libs < %{version}

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
Supplements:    (lua54 and patterns-base-documentation)

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
%setup -q -n lua-%{version} -a1
mv lua-%{version}-tests testes
%autopatch -p1

# manpage
%if "%{flavor}" != "test"
cat doc/lua.1  | sed 's/TH LUA 1/TH LUA%{major_version} 1/' > doc/lua%{major_version}.1
cat doc/luac.1 | sed 's/TH LUAC 1/TH LUAC%{major_version} 1/' > doc/luac%{major_version}.1

%build
sed -i -e "s@lib/lua/@%{_lib}/lua/@g" src/luaconf.h
make linux-readline %{_smp_mflags} VERBOSE=1 -C src \
    CC="cc" \
    MYCFLAGS="%{optflags} -std=gnu99 -D_GNU_SOURCE -fPIC -DLUA_COMPAT_MODULE" \
    V=%{major_version} \
    LIBTOOL="libtool --quiet"

%install
%make_install \
    LIBTOOL="libtool --quiet" \
    INSTALL_TOP="%{buildroot}%{_prefix}" \
    INSTALL_LIB="%{buildroot}%{_libdir}"

find %{buildroot} -type f -name "*.la" -delete -print

# create pkg-config file
cat > lua%{major_version}.pc <<-EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_prefix}/include/lua%{major_version}
INSTALL_LMOD=%{_datadir}/lua/%{major_version}
INSTALL_CMOD=%{_libdir}/lua/%{major_version}

Name: Lua %{major_version}
Description: An Extensible Extension Language
Version: %{version}
Libs: -llua%{major_version} -lm
Cflags: -I\${includedir}
EOF
install -D -m 644 lua%{major_version}.pc %{buildroot}%{_libdir}/pkgconfig/lua%{major_version}.pc

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for file in lua luac ; do
    touch "%{buildroot}%{_sysconfdir}/alternatives/${file}"
    ln -sf "%{_sysconfdir}/alternatives/${file}" "%{buildroot}%{_bindir}/${file}"
    touch "%{buildroot}%{_sysconfdir}/alternatives/${file}.1%{ext_man}"
    ln -sf "%{_sysconfdir}/alternatives/${file}.1%{ext_man}" "%{buildroot}%{_mandir}/man1/${file}.1%{ext_man}"
done

# Compat link with older unprefixed library and with soname 0 from deb/etc
ln -s %{_libdir}/liblua%{major_version}.so.%{major_version}.0 %{buildroot}%{_libdir}/liblua%{major_version}.so.%{major_version}
ln -s %{_libdir}/liblua%{major_version}.so.%{major_version}.0 %{buildroot}%{_libdir}/liblua%{major_version}.so.0
ln -s %{_libdir}/liblua%{major_version}.so.%{major_version}.0 %{buildroot}%{_libdir}/liblua.so.%{major_version}
# Library devel alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/liblua.so
ln -sf %{_sysconfdir}/alternatives/liblua.so %{buildroot}%{_libdir}/liblua.so
touch %{buildroot}%{_sysconfdir}/alternatives/lua.pc
ln -sf %{_sysconfdir}/alternatives/lua.pc %{buildroot}%{_libdir}/pkgconfig/lua.pc
%else
%check
cd testes
LD_LIBRARY_PATH=%{_libdir} %{_bindir}/lua%{major_version} all.lua
%endif

%if "%{flavor}" != "test"
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post
%{_sbindir}/update-alternatives --install                                                 \
            %{_bindir}/lua            lua       %{_bindir}/lua%{major_version}         54 \
    --slave %{_bindir}/luac           luac      %{_bindir}/luac%{major_version}           \
    --slave %{_mandir}/man1/lua.1%{ext_man}  lua.1%{ext_man}  %{_mandir}/man1/lua%{major_version}.1%{ext_man}  \
    --slave %{_mandir}/man1/luac.1%{ext_man} luac.1%{ext_man} %{_mandir}/man1/luac%{major_version}.1%{ext_man}

%postun
if [ "$1" = 0 ] ; then
    %{_sbindir}/update-alternatives --remove lua %{_bindir}/lua%{major_version}
fi

%post devel
%{_sbindir}/update-alternatives --install                                                     \
            %{_libdir}/liblua.so        liblua.so %{_libdir}/liblua%{major_version}.so     54 \
    --slave %{_libdir}/pkgconfig/lua.pc lua.pc    %{_libdir}/pkgconfig/lua%{major_version}.pc

%postun devel
if [ "$1" = 0 ] ; then
    %{_sbindir}/update-alternatives --remove liblua.so %{_libdir}/liblua%{major_version}.so
fi

%files
%dir %{_libdir}/lua
%dir %{_libdir}/lua/%{major_version}
%dir %{_datadir}/lua
%dir %{_datadir}/lua/%{major_version}
%{_bindir}/lua%{major_version}
%{_bindir}/luac%{major_version}
%{_mandir}/man1/lua%{major_version}.1%{ext_man}
%{_mandir}/man1/luac%{major_version}.1%{ext_man}
# alternatives
%{_bindir}/lua
%{_bindir}/luac
%{_mandir}/man1/lua.1%{ext_man}
%{_mandir}/man1/luac.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/lua
%ghost %{_sysconfdir}/alternatives/luac
%ghost %{_sysconfdir}/alternatives/lua.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/luac.1%{ext_man}

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
# alternatives
%{_libdir}/liblua.so
%{_libdir}/pkgconfig/lua.pc
%ghost %{_sysconfdir}/alternatives/liblua.so
%ghost %{_sysconfdir}/alternatives/lua.pc

%files doc
%doc doc/*

%endif
%changelog
