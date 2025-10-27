#
# spec file for package luajit2
#
# Copyright (c) 2025 SUSE LLC and contributors
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

%define abi_ver 5.1
%define so_ver 2
%define lib_ver 5_1-%{so_ver}
%define major 2.1
%define minor 20250826
%define upstream 1756211046
Name:           luajit
Version:        %{major}.%{minor}
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Release:        0
Summary:        JIT compiler for Lua language
License:        MIT
URL:            https://github.com/openresty/%{name}

Source0:        https://github.com/openresty/luajit2/archive/refs/tags/v%{major}-%{minor}.tar.gz#/luajit2-%{major}-%{minor}.tar.gz
Source1:        baselibs.conf
# https://patch-diff.githubusercontent.com/raw/openresty/luajit2/pull/236.patch#/riscv64-support.patch#/riscv64-support.patch
Patch0:         riscv64-support.patch
# https://github.com/openresty/luajit2/pull/245/commits/8e40aca7b3a919456b15698273e9b00e9250e769.patch#/loong64-support.patch
Patch1:         loong64-support.patch
BuildRequires:  pkgconfig
BuildRequires:  lua-macros
Requires:       lib%{name}-%{lib_ver} = %{version}
Provides:       lua51-luajit = %{version}-%{release}
Obsoletes:      lua51-luajit < %{version}
Provides:       moonjit = %{version}-%{release}
Obsoletes:      moonjit < %{version}
Provides:       lua = %{version}-%{release}
Provides:       Lua(API) = %{major}
# lj_arch.h:441:2: error: #error "No target architecture defined"
# ExclusiveArch:  x86_64 %%{ix86} aarch64 %%{arm} ppc mips mips64 mips64el s390x
# Both lua51 and luajit use %%{_libdir}/lua/%%{abi_ver}
Provides:      lua51
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
A Just-In-Time Compiler for Lua language.

%package -n lib%{name}-%{lib_ver}
Summary:        Library for LuaJIT2 compiler
Provides:       lib%{name}-%{lib_ver} = %{version}
%ifarch aarch64 x86_64 ppc64 ppc64le s390x riscv64
Provides:       liblua.so.5.1()(64bit)
%else
Provides:       liblua.so.5.1
%endif

%description -n lib%{name}-%{lib_ver}
Libraries to use LuaJIT2 compiler.

%package devel
Summary:        Devel files for %{name}
Requires:       %{name} = %{version}
Requires:       lib%{name}-%{lib_ver} = %{version}
Requires: 	lua-macros
Conflicts:      lua-devel
Provides:       moonjit-devel = %{version}-%{release}
Obsoletes:      moonjit-devel < %{version}
Provides:       libluajit-devel = %{version}-%{release}
Provides:       lua-devel = %{version}
Provides:       Lua(devel) = %{abi_ver}
Provides:       pkgconfig(lua) = %{version}

%description devel
Devel files for %{name} package.

%prep
%autosetup -p1 -n luajit2-%{major}-%{minor}

%build
%make_build %{?_make_output_sync} \
	Q= \
	DYNAMIC_CC="cc -fPIC" \
	LDCONFIG="true" \
	TARGET_AR="ar rcus" \
	TARGET_STRIP=: \
	PREFIX=%{_prefix} \
	MULTILIB=%{_lib} \
	CFLAGS="%{optflags}"

%install
%make_install \
	DYNAMIC_CC="cc -fPIC" \
	LDCONFIG="true" \
	TARGET_AR="ar rcus" \
	TARGET_STRIP=: \
	PREFIX=%{_prefix} \
	MULTILIB=%{_lib}

# remove static lib, not needed
rm %{buildroot}%{_libdir}/*.a

# Create runnable binary
ln -sf %{_bindir}/luajit-%{major}.%{upstream} %{buildroot}%{_bindir}/luajit
%if %{with libalternatives}
# alternatives - create configuration file
mkdir -p %{buildroot}%{_datadir}/libalternatives/lua
cat > %{buildroot}%{_datadir}/libalternatives/lua/52.conf <<EOF
binary=%{_bindir}/luajit
man=luajit
EOF
%else
# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch "%{buildroot}%{_sysconfdir}/alternatives/%{name}"
ln -sf "%{_sysconfdir}/alternatives/%{name}" "%{buildroot}%{_bindir}/%{name}"
touch "%{buildroot}%{_sysconfdir}/alternatives/%{name}.1%{ext_man}"
ln -sf "%{_sysconfdir}/alternatives/%{name}.1%{ext_man}" \
    "%{buildroot}%{_mandir}/man1/%{name}.1%{ext_man}"
%endif

# Compat link with older unprefixed library and with soname 0 from deb/etc
chmod +x %{buildroot}%{_libdir}/*
ln -s libluajit-%{abi_ver}.so.%{so_ver} \
	%{buildroot}%{_libdir}/liblua%{abi_ver}.so.%{abi_ver}.%{so_ver}
ln -s libluajit-%{abi_ver}.so.%{so_ver} \
	%{buildroot}%{_libdir}/liblua%{abi_ver}.%{so_ver}.so
ln -s %{_libdir}/liblua%{abi_ver}.%{so_ver}.so \
    %{buildroot}%{_libdir}/liblua.so
ln -s luajit.pc %{buildroot}%{_libdir}/pkgconfig/lua.pc

%if %{without libalternatives}
%post
%{_sbindir}/update-alternatives --install                                                 \
            %{_bindir}/lua            lua       %{_bindir}/lua%{abi_ver}         52 \
    --slave %{_mandir}/man1/lua.1%{ext_man}  lua.1%{ext_man}  %{_mandir}/man1/lua%{abi_ver}.1%{ext_man}

%postun
if [ "$1" = 0 ] ; then
    %{_sbindir}/update-alternatives --remove lua %{_bindir}/lua%{abi_ver}
fi
%endif

%ldconfig_scriptlets -n lib%{name}-%{lib_ver}

%files
%{_bindir}/%{name}-%{major}.%{upstream}
%{_bindir}/%{name}
%{_datadir}/%{name}-%{major}
%dir %{_libdir}/lua
%dir %{_libdir}/lua/%{abi_ver}
%dir %{_datadir}/lua
%dir %{_datadir}/lua/%{abi_ver}
%{_mandir}/man1/%{name}.1%{?ext_man}
%if %{with libalternatives}
%{_datadir}/libalternatives/lua/52.conf
%else
# alternatives
%{_bindir}/lua
%{_mandir}/man1/lua.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/lua
%ghost %{_sysconfdir}/alternatives/lua.1%{ext_man}
%endif

%files -n lib%{name}-%{lib_ver}
%{_libdir}/lib%{name}-%{abi_ver}.so.%{so_ver}
%{_libdir}/lib%{name}-%{abi_ver}.so.%{major}.%{upstream}

%files devel
%{_includedir}/luajit-%{major}
%{_libdir}/libluajit-%{abi_ver}.so
%{_libdir}/liblua.so
%{_libdir}/liblua%{abi_ver}.%{so_ver}.so
%{_libdir}/liblua%{abi_ver}.so.%{abi_ver}.%{so_ver}
%{_libdir}/pkgconfig/luajit.pc
%{_libdir}/pkgconfig/lua.pc

%changelog
