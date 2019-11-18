#
# spec file for package libv3270
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2008 Banco do Brasil S.A.
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


Name:           libv3270
Version:        5.2
Release:        0
Summary:        3270 Virtual Terminal for GTK
License:        LGPL-3.0-only
URL:            https://github.com/PerryWerneck/libv3270
Source:         libv3270-%{version}.tar.xz
BuildRequires:  autoconf >= 2.61
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  m4
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lib3270) >= 5.2
%if 0%{?centos_version}
# CENTOS Genmarshal doesn't depend on python!
BuildRequires:  python
%endif

%description

Originally designed as part of the pw3270 application, this library
provides a TN3270 virtual terminal widget for GTK 3.

For more details, see https://softwarepublico.gov.br/social/pw3270/ .

%define MAJOR_VERSION %(echo %{version} | cut -d. -f1)
%define MINOR_VERSION %(echo %{version} | cut -d. -f2)
%define _libvrs %{MAJOR_VERSION}_%{MINOR_VERSION}

%package -n %{name}-%{_libvrs}
Summary:    TN3270 access library

%description -n %{name}-%{_libvrs}
Originally designed as part of the pw3270 application, this library
provides a TN3270 virtual terminal widget for GTK 3.

For more details, see https://softwarepublico.gov.br/social/pw3270/ .

%package devel
Summary:    Header files for the 3270 Virtual Terminal library
Requires:   %{name}-%{_libvrs} = %{version}

%description devel
GTK development files for the 3270 Virtual Terminal.

%package -n glade-catalog-v3270
Summary:    Glade catalog for the TN3270 terminal emulator library
Requires:   glade

%description -n glade-catalog-v3270
This package provides a catalog for Glade to allow the use of V3270
widgets in Glade.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh
%configure

%build
%make_build

%install
%make_install

# configure --disable-static has no effect
rm -f %{buildroot}/%{_libdir}/*.a

%files -n %{name}-%{_libvrs}
%license LICENSE
%doc AUTHORS README.md
%{_libdir}/%{name}.so.*

%files devel
%{_datadir}/pw3270/pot/*.pot
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/v3270.h
%{_includedir}/v3270

%files -n glade-catalog-v3270
%{_datadir}/glade/

%post -n %{name}-%{_libvrs} -p /sbin/ldconfig
%postun -n %{name}-%{_libvrs} -p /sbin/ldconfig

%changelog
