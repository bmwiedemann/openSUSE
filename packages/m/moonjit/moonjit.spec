#
# spec file for package moonjit
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


%define lua_suffix 5_1
%define lib_suffix 2
Name:           moonjit
Version:        2.2.0
Release:        0
Summary:        JIT compiler for Lua language
License:        MIT
URL:            https://github.com/moonjit/moonjit
Source0:        https://github.com/moonjit/moonjit/archive/%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM moonjit105-string_gsub.patch gh#moonjit/moonjit#105 mcepl@suse.com
# fix string_gsub
Patch0:         moonjit105-string_gsub.patch
BuildRequires:  pkgconfig
Conflicts:      luajit
Provides:       lua51-luajit
Provides:       luajit = 2.1.0
Obsoletes:      lua51-luajit

%description
A Just-In-Time Compiler for Lua language

%package -n libluajit-%{lua_suffix}-%{lib_suffix}
Summary:        Library for JIT Lua compiler

%description -n libluajit-%{lua_suffix}-%{lib_suffix}
Libraries to use JIT Lua compiler

%package devel
Summary:        Devel files for LuaJIT
Requires:       %{name} = %{version}
Requires:       libluajit-%{lua_suffix}-%{lib_suffix} = %{version}
Conflicts:      luajit-devel
Provides:       luajit-devel = %{version}

%description devel
Devel files for luajit package

%prep
%setup -q -n moonjit-%{version}
%autopatch -p1

# Fix variables
sed -i "s,PREFIX= %{_prefix}/local,PREFIX= %{_prefix}," Makefile

%build
export CFLAGS="%{optflags} -DLUAJIT_ENABLE_LUA52COMPAT"
make %{?_smp_mflags} \
	Q= \
	DYNAMIC_CC="cc -fPIC" \
	LDCONFIG="true" \
	TARGET_AR="ar rcus" \
	TARGET_STRIP=: \
	MULTILIB=%{_lib}

%install
make DESTDIR=%{buildroot} install \
	INSTALL_LIB="%{buildroot}/%{_libdir}" \
	DYNAMIC_CC="cc -fPIC" \
	LDCONFIG="true" \
	TARGET_AR="ar rcus" \
	TARGET_STRIP=: \
	MULTILIB=%{_lib}
# remove static lib, not needed
rm %{buildroot}/%{_libdir}/*.a

# Beta version make install does not do this
ln -sf moonjit-%{version} %{buildroot}/%{_bindir}/moonjit
ln -sf moonjit-%{version} %{buildroot}/%{_bindir}/luajit

%check
%ifarch %arm ppc ppc64 ppc64le
make %{?_smp_mflags} check || { echo -e "WARNING: ignore check error for\narm*: https://github.com/moonjit/moonjit/issues/9\nppc*: https://github.com/moonjit/moonjit/issues/40"; }
%else
make %{?_smp_mflags} check
%endif

%post -n libluajit-%{lua_suffix}-%{lib_suffix} -p /sbin/ldconfig
%postun -n libluajit-%{lua_suffix}-%{lib_suffix} -p /sbin/ldconfig

%files
%{_bindir}/luajit
%{_bindir}/moonjit
%{_bindir}/moonjit-%{version}
%{_mandir}/man1/luajit.1%{?ext_man}
%{_datadir}/moonjit-%{version}/

%files -n libluajit-%{lua_suffix}-%{lib_suffix}
%{_libdir}/libluajit-5.1.so.*

%files devel
%{_includedir}/moonjit-2.2/
%{_libdir}/libluajit-5.1.so
%{_libdir}/pkgconfig/luajit.pc

%changelog
