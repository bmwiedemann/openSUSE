#
# spec file for package luajit
#
# Copyright (c) 2024 SUSE LLC
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
%define upname LuaJIT
Name:           luajit
Version:        5.1.2.1.0+git.1731601260.fe71d0f
Release:        0
Summary:        JIT compiler for Lua language
License:        MIT
URL:            https://luajit.org/
Source0:        %{upname}-%{version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-OPENSUSE luajit-lua-versioned.patch mcepl@suse.com
# Because we obsolete moonjit with version number higher than %%{version} we have to emulate Epoch
Patch0:         luajit-lua-versioned.patch
# https://salsa.debian.org/lua-team/luajit/-/raw/master/debian/patches/0002-Enable-debugging-symbols-in-the-build.patch
Patch2:         0002-Enable-debugging-symbols-in-the-build.patch
# https://salsa.debian.org/lua-team/luajit/-/raw/master/debian/patches/0003-Get-rid-of-LUAJIT_VERSION_SYM-that-changes-ABI-on-ev.patch
Patch3:         0003-Get-rid-of-LUAJIT_VERSION_SYM-that-changes-ABI-on-ev.patch
# Most recent s390x patches at https://github.com/luajit/luajit/pull/631
Patch4:         luajit-s390x.patch
# PPC64 patches are out of sync
# # https://salsa.debian.org/lua-team/luajit/-/raw/master/debian/patches/0004-Add-ppc64-support-based-on-koriakin-GitHub-patchset.patch
# # Patch again out of sync, gh#LuaJIT/LuaJIT#140
# Patch5:         0004-Add-ppc64-support-based-on-koriakin-GitHub-patchset.patch
# Patch6:         luajit-ppc64-replace-asserts.patch
BuildRequires:  git
BuildRequires:  pkgconfig
Requires:       %{name}-%{lib_version}-%{so_version} = %{version}
Provides:       lua51-luajit = %{version}-%{release}
Obsoletes:      lua51-luajit <= 2.2.0
Provides:       moonjit = %{version}-%{release}
Obsoletes:      moonjit <= 2.2.0
# lj_arch.h:441:2: error: #error "No target architecture defined"
ExcludeArch:    riscv64 ppc64 ppc64le

%description
A Just-In-Time Compiler for Lua language

%package -n libluajit-%{lib_version}-%{so_version}
Summary:        Library for JIT Lua compiler
Provides:       %{name}-%{lib_version}-%{so_version} = %{version}-%{release}

%description -n libluajit-%{lib_version}-%{so_version}
Libraries to use JIT Lua compiler

%package devel
Summary:        Devel files for %{name}
Requires:       %{name} = %{version}
Requires:       luajit-%{lib_version}-%{so_version} = %{version}
Provides:       moonjit-devel = %{version}-%{release}
Obsoletes:      moonjit-devel <= 2.2.0
Provides:       libluajit-devel = %{version}-%{release}

%description devel
Devel files for luajit package

%prep
%autosetup -p1 -n %{upname}-%{version}

# Fix variables
sed -i "s,PREFIX= %{_prefix}/local,PREFIX= %{_prefix}," Makefile
sed -i "s,%{_libexecdir},%{_libdir}," etc/luajit.pc

# Unfortunately, tar_scm doesn't use git archive (gh#openSUSE/obs-service-tar_scm#144)
%global realver 2.1.%(echo '%{version}' | cut -d. -f 6)
echo '%{version}' | cut -d. -f 6 >.relver

%build
export CFLAGS="%{optflags}"
%make_build %{?_make_output_sync} \
	Q= \
	DYNAMIC_CC="cc -fPIC" \
	LDCONFIG="true" \
	TARGET_AR="ar rcus" \
	TARGET_STRIP=: \
	MULTILIB=%{_lib}

%install
make DESTDIR=%{buildroot} install \
	INSTALL_LIB="%{buildroot}%{_libdir}" \
	DYNAMIC_CC="cc -fPIC" \
	LDCONFIG="true" \
	TARGET_AR="ar rcus" \
	TARGET_STRIP=: \
	MULTILIB=%{_lib}

# remove static lib, not needed
rm %{buildroot}%{_libdir}/*.a

# Create runnable binary
ln -sf %{_bindir}/luajit-%{lib_version}-%{realver} %{buildroot}%{_bindir}/luajit

%post -n libluajit-%{lib_version}-%{so_version} -p /sbin/ldconfig
%postun -n libluajit-%{lib_version}-%{so_version} -p /sbin/ldconfig

%files
%license COPYRIGHT
%doc README

%{_bindir}/luajit
%{_bindir}/luajit-%{lib_version}
%{_bindir}/luajit-%{lib_version}-%{realver}
%{_mandir}/man1/luajit-%{lib_version}.1%{?ext_man}
%{_datadir}/luajit-%{lib_version}-2.1

%files -n libluajit-%{lib_version}-%{so_version}
%{_libdir}/libluajit-5.1.so.*

%files devel
%{_includedir}/luajit-%{lib_version}-2.1
%{_libdir}/libluajit-5.1.so
%{_libdir}/pkgconfig/luajit.pc

%changelog
