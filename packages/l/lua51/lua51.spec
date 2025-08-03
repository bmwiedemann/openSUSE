#
# spec file for package lua51
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


%define major_version 5.1
%define libname liblua5_1-5
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           lua51
Version:        5.1.5
Release:        0
Summary:        Small Embeddable Language with Procedural Syntax
License:        MIT
Group:          Development/Languages/Other
URL:            https://www.lua.org
Source0:        https://www.lua.org/ftp/lua-%{version}.tar.gz
Source1:        https://www.lua.org/tests/lua%{major_version}-tests.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-SUSE tweak the buildsystem to produce what is needed for SUSE
Patch0:         lua-build-system.patch
# Yes, Lua is from Brasil, we need pt_BR locale
BuildRequires:  glibc-locale
BuildRequires:  libtool
BuildRequires:  lua-macros
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
Conflicts:      lua
Provides:       lua = %{version}
Obsoletes:      lua < %{version}
Provides:       Lua(API) = %{major_version}
%if %{with libalternatives}
BuildRequires:  alts
BuildRequires:  lua-interpreter
Requires:       alts
Requires:       lua-interpreter
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
# Compat as libtool changes the soname
Group:          System/Libraries
Provides:       liblua5_1 = %{version}-%{release}
Obsoletes:      liblua5_1 < %{version}-%{release}
Provides:       %{name}-libs = %{version}
Obsoletes:      %{name}-libs < %{version}
%ifarch aarch64 x86_64 ppc64 ppc64le s390x riscv64
Provides:       liblua.so.5.1()(64bit)
%else
Provides:       liblua.so.5.1
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
Group:          Documentation/HTML
BuildArch:      noarch
%if 0%{?suse_version} > 1315
Supplements:    (lua51 and patterns-base-documentation)
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
%setup -q -n lua-%{version} -a1
mv lua%{major_version}-tests testes
%autopatch -p1

# manpage
cat doc/lua.1  | sed 's/TH LUA 1/TH LUA%{major_version} 1/' > doc/lua%{major_version}.1
cat doc/luac.1 | sed 's/TH LUAC 1/TH LUAC%{major_version} 1/' > doc/luac%{major_version}.1

%build
%global _lto_cflags %{nil}
sed -i -e "s@lib/lua/@%{_lib}/lua/@g" src/luaconf.h
%make_build all -C src \
    CC="cc" \
    MYCFLAGS="%{optflags} -std=gnu99 -D_GNU_SOURCE -fPIC -DLUA_USE_LINUX -DLUA_COMPAT_MODULE" \
    MYLIBS="-Wl,-E -ldl -lreadline -lhistory -lncurses" \
    V=%{major_version} \
    LIBTOOL="libtool --quiet"

%install
%make_install \
    LIBTOOL="libtool --quiet" \
    V=%{major_version} \
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

%if %{with libalternatives}
# alternatives - create configuration file
mkdir -p %{buildroot}%{_datadir}/libalternatives/lua
cat > %{buildroot}%{_datadir}/libalternatives/lua/51.conf <<EOF
binary=%{_bindir}/lua5.1
man=lua5.1
EOF
mkdir -p %{buildroot}%{_datadir}/libalternatives/luac
cat > %{buildroot}%{_datadir}/libalternatives/luac/51.conf <<EOF
binary=%{_bindir}/luac5.1
man=luac5.1
EOF
%else
# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for file in lua luac ; do
    touch "%{buildroot}%{_sysconfdir}/alternatives/${file}"
    ln -sf "%{_sysconfdir}/alternatives/${file}" "%{buildroot}%{_bindir}/${file}"
    touch "%{buildroot}%{_sysconfdir}/alternatives/${file}.1%{ext_man}"
    ln -sf "%{_sysconfdir}/alternatives/${file}.1%{ext_man}" "%{buildroot}%{_mandir}/man1/${file}.1%{ext_man}"
done
%endif

# Compat link with older unprefixed library and with soname 0 from deb/etc
chmod +x %{buildroot}%{_libdir}/*
ln -s %{_libdir}/liblua%{major_version}.so.%{major_version}.0 %{buildroot}%{_libdir}/liblua%{major_version}.so.%{major_version}
ln -s %{_libdir}/liblua%{major_version}.so.%{major_version}.0 %{buildroot}%{_libdir}/liblua%{major_version}.so.0
ln -s %{_libdir}/liblua%{major_version}.so.%{major_version}.0 %{buildroot}%{_libdir}/liblua.so.%{major_version}

# We don’t create alternatives for -devel content, just conflict those
ln -s %{_libdir}/liblua%{major_version}.so %{buildroot}%{_libdir}/liblua.so
ln -s %{_libdir}/pkgconfig/lua%{major_version}.pc %{buildroot}%{_libdir}/pkgconfig/lua.pc

%check
# WARNING: this whole check section is incredibly interdependent and brittle, don't change anything
# unless you really thought through what you would be doing.
# The distributed binary of the Lua interpreter is (correctly) build without LUA_USE_APICHECK option,
# we have to build a special interpreter just for the testing.
mkdir -p build-test
cp -r src build-test/
cp Makefile build-test/
pushd build-test
%make_build clean -C src
%make_build all -C src \
    CC="cc" \
    MYCFLAGS="%{optflags} -std=gnu99 -D_GNU_SOURCE -fPIC -DLUA_USE_LINUX -DLUA_COMPAT_MODULE -DLUA_USE_APICHECK" \
    MYLIBS="-Wl,-E -ldl -lreadline -lhistory -lncurses" \
    V=%{major_version} \
    LIBTOOL="libtool --quiet"
popd
cd testes
pushd libs
%make_build all CFLAGS="-fPIC -std=gnu99 -D_GNU_SOURCE -I../../build-test/src"
cp -- *.so ..
popd
# Yes, Lua is from Brasil
export LANG=pt_BR.utf8
export LD_LIBRARY_PATH=../build-test/src/.libs
# I haven't found a way how to run FULL all.lua test suite, so we are just running
# what we can for checking the sanity of the build.
for testFile in api.lua attrib.lua calls.lua closure.lua \
    code.lua constructs.lua db.lua errors.lua events.lua files.lua \
    gc.lua checktable.lua literals.lua locals.lua math.lua nextvar.lua \
    pm.lua sort.lua strings.lua vararg.lua verybig.lua
do
../build-test/src/.libs/lua%{major_version} $testFile
done

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%if %{without libalternatives}
%post
%{_sbindir}/update-alternatives --install                                                 \
            %{_bindir}/lua            lua       %{_bindir}/lua%{major_version}         51 \
    --slave %{_bindir}/luac           luac      %{_bindir}/luac%{major_version}           \
    --slave %{_mandir}/man1/lua.1%{ext_man}  lua.1%{ext_man}  %{_mandir}/man1/lua%{major_version}.1%{ext_man}  \
    --slave %{_mandir}/man1/luac.1%{ext_man} luac.1%{ext_man} %{_mandir}/man1/luac%{major_version}.1%{ext_man}

%postun
if [ "$1" = 0 ] ; then
    %{_sbindir}/update-alternatives --remove lua %{_bindir}/lua%{major_version}
fi
%endif

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
%if %{with libalternatives}
%{_datadir}/libalternatives/lua/51.conf
%{_datadir}/libalternatives/luac/51.conf
%else
# alternatives
%{_bindir}/lua
%{_bindir}/luac
%{_mandir}/man1/lua.1%{?ext_man}
%{_mandir}/man1/luac.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/lua
%ghost %{_sysconfdir}/alternatives/luac
%ghost %{_sysconfdir}/alternatives/lua.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/luac.1%{ext_man}
%endif

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

%changelog
