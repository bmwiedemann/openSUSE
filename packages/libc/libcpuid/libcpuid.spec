#
# spec file for package libcpuid
#
# Copyright (c) 2022 SUSE LLC
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


%define so_ver  16
Name:           libcpuid
Version:        0.6.2
Release:        0
Summary:        Library providing x86 CPU identification
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/anrieff/libcpuid
Source0:        https://github.com/anrieff/libcpuid/releases/download/v%{version}/libcpuid-%{version}.tar.gz
BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  python3-base

%description
Libcpuid provides CPU identification for the x86 (and x86_64) architectures.

%package tools
Summary:        Tools based on %{name}

%description tools
This package provides tools based on %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{so_ver} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
For details about the programming API, please see the docs
on the project's site (http://libcpuid.sourceforge.net/)

%package -n %{name}%{so_ver}
Summary:        Library providing CPU identification for x86

%description -n %{name}%{so_ver}
Libcpuid provides CPU identification for the x86 (and x86_64)
architectures.

%prep
%setup -q

%build
%configure \
  --enable-static=no
%make_build

%install
%make_install

# Drop useless libtool files
find %{buildroot} -type f -name "*.la" -delete -print

# Generate manpages
help2man ./cpuid_tool/cpuid_tool > cpuid_tool.1
install -D -p -m 0644 cpuid_tool.1 \
  %{buildroot}%{_mandir}/man1/cpuid_tool.1

%check
%make_build test

%post -n %{name}%{so_ver} -p /sbin/ldconfig
%postun -n %{name}%{so_ver} -p /sbin/ldconfig

%files tools
%{_bindir}/cpuid_tool
%{_mandir}/man1/cpuid_tool.1%{?ext_man}

%files -n %{name}%{so_ver}
%license COPYING AUTHORS
%{_libdir}/%{name}.so.%{so_ver}*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
