#
# spec file for package hiredis
#
# Copyright (c) 2020 SUSE LLC
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


%global libname lib%{name}1_0_0
Name:           hiredis
Version:        1.0.0
Release:        0
Summary:        Minimalistic C client for Redis
License:        BSD-3-Clause
Group:          Productivity/Databases/Clients
URL:            https://github.com/redis/hiredis
Source0:        https://github.com/redis/hiredis/archive/v%{version}.tar.gz
Patch0:         relocatable_executable.patch
BuildRequires:  pkgconfig
BuildRequires:  libopenssl-devel

%description
Hiredis is a minimalistic C client library for the
Redis database.

%package devel
Summary:        Header files and libraries for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
The %{name}-devel package contains the header files and
libraries for Redis database.

%package -n %{libname}
Summary:        Shared library for %{name}
Group:          Productivity/Databases/Clients

%description -n %{libname}
Shared library for %{name}. The %{name}-example and
%{name}-test are in %{name} package.

%prep
%setup -q
%patch0

%build
%make_build OPTIMIZATION="%{optflags}" PREFIX=%{_prefix} LIBRARY_PATH=%{_lib} USE_SSL=1

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBRARY_PATH=%{_lib} USE_SSL=1

mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name}-test %{buildroot}%{_bindir}

find %{buildroot} -type f -name '*.a' -delete

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(0644,root,root,0755)
%license COPYING
%doc README.md
%attr(0755,root,root) %{_bindir}/%{name}-test

%files devel
%defattr(0644,root,root,0755)
%doc CHANGELOG.md
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}_ssl.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}_ssl.pc

%files -n %{libname}
%defattr(0755,root,root,0755)
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}_ssl.so.*

%changelog
