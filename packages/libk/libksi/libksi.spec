#
# spec file for package libksi
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


%define sover 13
Name:           libksi
Version:        3.21.3087
Release:        0
Summary:        GuardTime KSI API
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/guardtime/libksi/archive/refs/tags/v%{version}.tar.gz
Source:         %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  curl-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
LibKSI - Keyless Signature Infrastructure GuardTime client library

%package -n %{name}%{sover}
Summary:        GuardTime KSI API
Group:          System/Libraries

%description -n %{name}%{sover}
LibKSI - Keyless Signature Infrastructure GuardTime client library

%package devel
Summary:        Development files for the %{name} package
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
LibKSI - Keyless Signature Infrastructure GuardTime client library
The libksi-devel package contains the header files and libraries
needed to develop applications using libksi.

%prep
%autosetup -p1
autoreconf -ifv

%build
%configure \
	--disable-static \
	--with-cafile=%{_sysconfdir}/ssl/ca-bundle.pem
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
rm -v %{buildroot}/%{_datadir}/doc/%{name}/license.txt
rm -v %{buildroot}/%{_datadir}/doc/%{name}/changelog

%check
#make check
#make test

%post -n %{name}%{sover} -p /sbin/ldconfig

%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%defattr(-,root,root)
%doc license.txt changelog
%{_libdir}/libksi.so.*

%files devel
%defattr(-,root,root)
%doc license.txt changelog doc/
%{_includedir}/ksi
%{_libdir}/libksi.so
%{_libdir}/pkgconfig/libksi.pc

%changelog
