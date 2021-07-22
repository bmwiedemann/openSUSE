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


# These numbers are from readelf -a /usr/lib*/lib*.so* |grep soname (dots replaced by underscores)
%define lib_version 5_1
%define so_version 2
# update-alternatives preferences for this package
%define moonjit_pref 25

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
Requires(post): update-alternatives
Requires(postun):update-alternatives
Requires:       %{name}-%{lib_version}-%{so_version} = %{version}
Conflicts:      luajit

%description
A Just-In-Time Compiler for Lua language

%package -n libluajit-%{lib_version}-%{so_version}
Summary:        Library for JIT Lua compiler
Provides:       %{name}-%{lib_version}-%{so_version} = %{version}

%description -n libluajit-%{lib_version}-%{so_version}
Libraries to use JIT Lua compiler

%package devel
Summary:        Devel files for %{name}
Requires:       %{name} = %{version}
Requires:       %{name}-%{lib_version}-%{so_version} = %{version}
Conflicts:      luajit-devel
Provides:       libuajit-devel = %{version}

%description devel
Devel files for luajit package

%prep
%autosetup -p1

# Fix variables
sed -i "s,PREFIX= %{_prefix}/local,PREFIX= %{_prefix}," Makefile

%build
export CFLAGS="%{optflags} -DLUAJIT_ENABLE_LUA52COMPAT"
%make_build \
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

ln -sf %{_bindir}/moonjit-%{version} %{buildroot}%{_bindir}/moonjit
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
ln -sf %{_sysconfdir}/alternatives/luajit \
    %{buildroot}%{_bindir}/luajit

%post
%{_sbindir}/update-alternatives --force \
    --install %{_bindir}/luajit luajit %{_bindir}/moonjit-%{version} %{moonjit_pref}

%postun
if [ ! -f %{_bindir}/moonjit-%{version} ] ; then
	%{_sbindir}/update-alternatives --remove luajit %{_bindir}/moonjit-%{version}
fi

%check
%ifarch %arm ppc ppc64 ppc64le
make %{?_smp_mflags} check || { echo -e "WARNING: ignore check error for\narm*: https://github.com/moonjit/moonjit/issues/9\nppc*: https://github.com/moonjit/moonjit/issues/40"; }
%else
make %{?_smp_mflags} check
%endif

%post -n libluajit-%{lib_version}-%{so_version} -p /sbin/ldconfig
%postun -n libluajit-%{lib_version}-%{so_version} -p /sbin/ldconfig

%files
%{_bindir}/luajit
%{_bindir}/moonjit
%{_bindir}/moonjit-%{version}
%{_mandir}/man1/luajit.1%{?ext_man}
%{_datadir}/moonjit-%{version}/

%files -n libluajit-%{lib_version}-%{so_version}
%{_libdir}/libluajit-5.1.so.*

%files devel
%{_includedir}/moonjit-2.2/
%{_libdir}/libluajit-5.1.so
%{_libdir}/pkgconfig/luajit.pc

%changelog
