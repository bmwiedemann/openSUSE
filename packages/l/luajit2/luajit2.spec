#
# spec file for package luajit2
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


%define abi_ver 5.1
%define so_ver 2
%define lib_ver 5_1-%{so_ver}
%define major 2.1
%define minor 20241104
%define upstream 1728714540
Name:           luajit2
Version:        %{major}.%{minor}
Release:        0
Summary:        OpenResty's maintained branch of LuaJIT
License:        MIT
URL:            https://github.com/openresty/%{name}
Source0:        https://github.com/openresty/%{name}/archive/refs/tags/v%{major}-%{minor}.tar.gz#/%{name}-%{major}-%{minor}.tar.gz
Source1:        baselibs.conf
Patch0:         %{name}-name.patch
BuildRequires:  pkgconfig
Requires:       lib%{name}-%{lib_ver} = %{version}

%description
This is the official OpenResty branch of LuaJIT. It is not to be considered a fork,
since we still regularly synchronize changes from the upstream LuaJIT project.

%package -n lib%{name}-%{lib_ver}
Summary:        Library for LuaJIT2 compiler

%description -n lib%{name}-%{lib_ver}
Libraries to use LuaJIT2 compiler.

%package devel
Summary:        Devel files for %{name}
Requires:       %{name} = %{version}
Requires:       lib%{name}-%{lib_ver} = %{version}

%description devel
Devel files for %{name} package.

%prep
%autosetup -p1 -n %{name}-%{major}-%{minor}

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

%post -n lib%{name}-%{lib_ver} -p /sbin/ldconfig
%postun -n lib%{name}-%{lib_ver} -p /sbin/ldconfig

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/%{name}-%{major}

%files -n lib%{name}-%{lib_ver}
%{_libdir}/lib%{name}-%{abi_ver}.so.%{so_ver}
%{_libdir}/lib%{name}-%{abi_ver}.so.%{major}.%{upstream}

%files devel
%{_includedir}/%{name}-%{major}
%{_libdir}/lib%{name}-%{abi_ver}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
