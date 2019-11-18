#
# spec file for package lib3270
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) <2008> <Banco do Brasil S.A.>
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


Name:           lib3270
Version:        5.2
Release:        0
Summary:        TN3270 Access library
License:        LGPL-3.0-only
URL:            https://github.com/PerryWerneck/lib3270
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf >= 2.61
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  m4
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  xz

%description
TN3270 access library, originally designed as part of the pw3270 application.

For more details, see https://softwarepublico.gov.br/social/pw3270/ .

%define MAJOR_VERSION %(echo %{version} | cut -d. -f1)
%define MINOR_VERSION %(echo %{version} | cut -d. -f2)
%define _libvrs %{MAJOR_VERSION}_%{MINOR_VERSION}

%package -n %{name}-%{_libvrs}
Summary:    TN3270 Access library

%description -n %{name}-%{_libvrs}
TN3270 access library, originally designed as part of the pw3270 application.

For more details, see https://softwarepublico.gov.br/social/pw3270/ .

%package devel
Summary:    TN3270 Access library development files
Requires:   %{name}-%{_libvrs} = %{version}

%description devel
Header files for the TN3270 access library.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh
%configure

%build
make all %{?_smp_mflags}

%install
%make_install

# configure --disable-static is non-functional
rm -f %{buildroot}/%{_libdir}/*.a

%fdupes %{buildroot}/%{_prefix}

%files -n %{name}-%{_libvrs}
%doc AUTHORS README.md
%license LICENSE

%{_libdir}/%{name}.so.*
%{_libdir}/%{name}++.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/%{name}++.so
%dir %{_datadir}/pw3270
%dir %{_datadir}/pw3270/pot
%{_datadir}/pw3270/pot/*.pot
%{_includedir}/*.h
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*.pc

%post -n %{name}-%{_libvrs} -p /sbin/ldconfig
%postun -n %{name}-%{_libvrs} -p /sbin/ldconfig

%changelog
