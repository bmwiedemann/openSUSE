#
# spec file for package lua53
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


%define major_version 5.3
%define libname liblua5_3-5
Name:           lua53
Version:        5.3.6
Release:        0
Summary:        Small Embeddable Language with Procedural Syntax
License:        MIT
Group:          Development/Languages/Other
Url:            http://www.lua.org
Source:         http://www.lua.org/ftp/lua-%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-SUSE tweak the buildsystem to produce what is needed for SUSE
Patch0:         lua-build-system.patch
# PATCH-FIX-UPSTREAM https://www.lua.org/bugs.html#5.3.6
#Patch1:        upstream-bugs.patch
# PATCH-FIX-UPSTREAM https://www.lua.org/bugs.html#5.4.0
#Patch2:        upstream-bugs-backport-lua54.patch
BuildRequires:  libtool
BuildRequires:  lua-macros
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
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
# Compat as libtool changes the soname
Group:          System/Libraries
%ifarch aarch64 x86_64 ppc64 ppc64le s390x riscv64
Provides:       liblua.so.5.3()(64bit)
%else
Provides:       liblua.so.5.3
%endif
Provides:       liblua5_3 = %{version}-%{release}
Obsoletes:      liblua5_3 < %{version}-%{release}
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
Group:          Documentation/HTML
BuildArch:      noarch

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
%setup -q -n lua-%{version}
%autopatch -p1

# manpage
cat doc/lua.1  | sed 's/TH LUA 1/TH LUA%{major_version} 1/' > doc/lua%{major_version}.1
cat doc/luac.1 | sed 's/TH LUAC 1/TH LUAC%{major_version} 1/' > doc/luac%{major_version}.1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
sed -i -e "s@lib/lua/@%{_lib}/lua/@g" src/luaconf.h
export LIBTOOL="libtool --quiet"
make %{?_smp_mflags} -C src \
    CC="cc" \
    MYCFLAGS="%{optflags} -std=gnu99 -D_GNU_SOURCE -fPIC -DLUA_USE_LINUX -DLUA_COMPAT_MODULE" \
    MYLIBS="-Wl,-E -ldl -lreadline -lhistory -lncurses" \
    V=%{major_version} \
    all

%install
make install \
    V=%{major_version} \
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
install -D -m 644 lua%{major_version}.pc %{buildroot}/%{_libdir}/pkgconfig/lua%{major_version}.pc

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

%check
cd src
LD_LIBRARY_PATH=`pwd` ./lua%{major_version} -e 'print(0)' > /dev/null

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post
%{_sbindir}/update-alternatives --install                                                 \
            %{_bindir}/lua            lua       %{_bindir}/lua%{major_version}         53 \
    --slave %{_bindir}/luac           luac      %{_bindir}/luac%{major_version}           \
    --slave %{_mandir}/man1/lua.1%{ext_man}  lua.1%{ext_man}  %{_mandir}/man1/lua%{major_version}.1%{ext_man}  \
    --slave %{_mandir}/man1/luac.1%{ext_man} luac.1%{ext_man} %{_mandir}/man1/luac%{major_version}.1%{ext_man}

%postun
if [ "$1" = 0 ] ; then
    %{_sbindir}/update-alternatives --remove lua %{_bindir}/lua%{major_version}
fi

%post devel
%{_sbindir}/update-alternatives --install                                                     \
            %{_libdir}/liblua.so        liblua.so %{_libdir}/liblua%{major_version}.so     53 \
    --slave %{_libdir}/pkgconfig/lua.pc lua.pc    %{_libdir}/pkgconfig/lua%{major_version}.pc

%postun devel
if [ "$1" = 0 ] ; then
    %{_sbindir}/update-alternatives --remove liblua.so %{_libdir}/liblua%{major_version}.so
fi

%files
%doc README
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
%{_libdir}/liblua%{major_version}.a
%{_libdir}/liblua%{major_version}.so
%{_libdir}/pkgconfig/lua%{major_version}.pc
# alternatives
%{_libdir}/liblua.so
%{_libdir}/pkgconfig/lua.pc
%ghost %{_sysconfdir}/alternatives/liblua.so
%ghost %{_sysconfdir}/alternatives/lua.pc

%files doc
%doc doc/*

%changelog
