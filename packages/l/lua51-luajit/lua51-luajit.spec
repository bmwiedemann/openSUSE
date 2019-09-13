#
# spec file for package lua51-luajit
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


%define lua_suffix 5_1
%define lib_suffix 2
%ifarch x86_64 aarch64 s390x
%global multilib_flag MULTILIB=lib64
%endif
%define realver 2.1.0-beta3
Name:           lua51-luajit
Version:        2.1.0~beta2
Release:        0
Summary:        JIT compiler for Lua language
License:        MIT
Group:          Development/Languages/Lua
Url:            http://www.luajit.com/
Source0:        http://luajit.org/download/LuaJIT-%{realver}.tar.gz
Source1:        baselibs.conf
Patch0:         luajit-lua-versioned.patch
Patch1:         0001-PPC64-Fix-sradi-machine-code-offsets.patch
Patch2:         0002-PPC64-Add-method-for-external-branch-by-using-got-fo.patch
Patch3:         0003-PPC64-Add-LJ_GC64-mode-interpreter-for-ppc.patch
Patch4:         0004-PPC64-Add-special-instructions-for-PIC-code-setup.patch
Patch5:         0005-PPC64-Add-ffi-support.patch
Patch6:         0006-PPC64-Enable-support-for-ppc64-little-endian.patch
Patch7:         0007-PPC64-Fix-external-branches-that-should-address-on-R.patch
Patch8:         0008-luajit-2.1-fix-fp-parameter-passing-for-ppc64.patch
Patch9:         0009-PPC64-Fix-tab-indentation-from-last-commit.patch
Patch10:        0010-PPC64-Define-13-FPs-regs-as-arguments.patch
Patch11:        0011-PPC64-Fix-indentation-code-style.patch
Patch12:        0012-Fix-debug-information-for-PPC64.patch
Patch13:        0013-Fix-TOC-pointer-value-on-ffi-callback-handling.patch
Patch14:        0014-Improve-readability-of-a-load-instruction.patch
Patch15:        0015-Fix-remaining-unwind-values-on-vm-frames.patch
BuildRequires:  pkgconfig
Requires:       libluajit-%{lua_suffix}-%{lib_suffix} = %{version}
Requires(post): update-alternatives
Requires(preun): update-alternatives
Conflicts:      luajit
Provides:       luajit = %{version}
# lj_arch.h do not support ppc64/ppc64le/s390/s390x
ExcludeArch:    ppc64 s390 s390x

%description
A Just-In-Time Compiler for Lua language

%package -n libluajit-%{lua_suffix}-%{lib_suffix}
Summary:        Library for JIT Lua compiler
Group:          System/Libraries

%description -n libluajit-%{lua_suffix}-%{lib_suffix}
Libraries to use JIT Lua compiler

%package devel
Summary:        Devel files for LuaJIT
Group:          Development/Languages/Lua
Requires:       %{name} = %{version}
Requires:       libluajit-%{lua_suffix}-%{lib_suffix} = %{version}
Conflicts:      luajit-devel
Provides:       luajit-devel = %{version}

%description devel
Devel files for luajit package

%prep
%setup -q -n LuaJIT-%{realver}
%autopatch -p1

# Fix variables
sed -i "s,PREFIX= %{_prefix}/local,PREFIX= %{_prefix}," Makefile

%build
CFLAGS="%{optflags}" \
make %{?_smp_mflags} \
	Q= \
	DYNAMIC_CC="cc -fPIC" \
	LDCONFIG="true" \
	TARGET_AR="ar rcus" \
	TARGET_STRIP=: \
	%{?multilib_flag}

%install
make DESTDIR=%{buildroot} install \
	INSTALL_LIB="%{buildroot}/%{_libdir}" \
	DYNAMIC_CC="cc -fPIC" \
	LDCONFIG="true" \
	TARGET_AR="ar rcus" \
	TARGET_STRIP=: \
	%{?multilib_flag}
# remove static lib, not needed
rm %{buildroot}/%{_libdir}/*.a

# Beta version make install does not do this
ln -sf luajit-%{lua_suffix}-%{realver} %{buildroot}/%{_bindir}/luajit-%{lua_suffix}

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/luajit
touch %{buildroot}%{_sysconfdir}/alternatives/luajit.1%{ext_man}
ln -sf %{_sysconfdir}/alternatives/luajit %{buildroot}%{_bindir}/luajit
ln -sf %{_sysconfdir}/alternatives/luajit.1%{ext_man} %{buildroot}%{_mandir}/man1/luajit.1%{ext_man}

%post
%{_sbindir}/update-alternatives --install %{_bindir}/luajit luajit %{_bindir}/luajit-%{lua_suffix}-%{realver} 60 \
	--slave %{_mandir}/man1/luajit.1%{ext_man} luajit.1%{ext_man} %{_mandir}/man1/luajit-%{lua_suffix}.1%{ext_man}

%preun
if [ "$1" = 0 ] ; then
	%{_sbindir}/update-alternatives --remove luajit %{_bindir}/luajit-%{lua_suffix}-%{realver}
fi

%post -n libluajit-%{lua_suffix}-%{lib_suffix} -p /sbin/ldconfig
%postun -n libluajit-%{lua_suffix}-%{lib_suffix} -p /sbin/ldconfig

%files
%ghost %{_sysconfdir}/alternatives/luajit
%ghost %{_sysconfdir}/alternatives/luajit.1%{ext_man}
%{_bindir}/luajit
%{_bindir}/luajit-%{lua_suffix}
%{_bindir}/luajit-%{lua_suffix}-%{realver}
%{_mandir}/man1/luajit.1%{ext_man}
%{_mandir}/man1/luajit-%{lua_suffix}.1%{ext_man}
%{_datadir}/luajit-%{lua_suffix}-%{realver}/

%files -n libluajit-%{lua_suffix}-%{lib_suffix}
%{_libdir}/libluajit-5.1.so.*

%files devel
%{_includedir}/luajit-%{lua_suffix}-2.1/
%{_libdir}/libluajit-5.1.so
%{_libdir}/pkgconfig/luajit.pc

%changelog
