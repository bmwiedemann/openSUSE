#
# spec file for package moonjit
#
# Copyright (c) 2019 SUSE LLC
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
%ifarch x86_64 aarch64 s390x ppc64 ppc64le
%global multilib_flag MULTILIB=lib64
%endif
Name:           moonjit
Version:        2.1.2
Release:        0
Summary:        JIT compiler for Lua language
License:        MIT
URL:            https://github.com/moonjit/moonjit
Source0:        https://github.com/moonjit/moonjit/archive/%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         luajit-lua-versioned.patch
BuildRequires:  pkgconfig
Requires(post): update-alternatives
Requires(preun): update-alternatives
Conflicts:      luajit
Provides:       lua51-luajit
Provides:       luajit = %{version}
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
ln -sf luajit-%{lua_suffix}-%{version} %{buildroot}/%{_bindir}/luajit-%{lua_suffix}

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/luajit
touch %{buildroot}%{_sysconfdir}/alternatives/luajit.1%{ext_man}
ln -sf %{_sysconfdir}/alternatives/luajit %{buildroot}%{_bindir}/luajit
ln -sf %{_sysconfdir}/alternatives/luajit.1%{ext_man} %{buildroot}%{_mandir}/man1/luajit.1%{ext_man}

%check
make %{?_smp_mflags} check

%post
%{_sbindir}/update-alternatives --install %{_bindir}/luajit luajit %{_bindir}/luajit-%{lua_suffix}-%{version} 60 \
	--slave %{_mandir}/man1/luajit.1%{ext_man} luajit.1%{ext_man} %{_mandir}/man1/luajit-%{lua_suffix}.1%{ext_man}

%preun
if [ "$1" = 0 ] ; then
	%{_sbindir}/update-alternatives --remove luajit %{_bindir}/luajit-%{lua_suffix}-%{version}
fi

%post -n libluajit-%{lua_suffix}-%{lib_suffix} -p /sbin/ldconfig
%postun -n libluajit-%{lua_suffix}-%{lib_suffix} -p /sbin/ldconfig

%files
%ghost %{_sysconfdir}/alternatives/luajit
%ghost %{_sysconfdir}/alternatives/luajit.1%{ext_man}
%{_bindir}/luajit
%{_bindir}/luajit-%{lua_suffix}
%{_bindir}/luajit-%{lua_suffix}-%{version}
%{_mandir}/man1/luajit.1%{?ext_man}
%{_mandir}/man1/luajit-%{lua_suffix}.1%{?ext_man}
%{_datadir}/luajit-%{lua_suffix}-%{version}/

%files -n libluajit-%{lua_suffix}-%{lib_suffix}
%{_libdir}/libluajit-5.1.so.*

%files devel
%{_includedir}/luajit-%{lua_suffix}-2.1/
%{_libdir}/libluajit-5.1.so
%{_libdir}/pkgconfig/luajit.pc

%changelog
