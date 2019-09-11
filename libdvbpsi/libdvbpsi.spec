#
# spec file for package libdvbpsi
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define libname %{name}10
Name:           libdvbpsi
Version:        1.3.2
Release:        0
Summary:        Library for Decoding and Generating MPEG TS and DVB PSI Tables
License:        LGPL-2.1+
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            http://www.videolan.org/developers/libdvbpsi.html
Source:         http://download.videolan.org/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source99:       baselibs.conf
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libdvbpsi is a simple library designed for decoding and generating
MPEG TS and DVB PSI tables. Current features: * Program Association Table
(PAT), decoder and generator.

%package -n %{libname}
Summary:        Library for Decoding and Generating MPEG TS and DVB PSI Tables
Group:          System/Libraries

%description -n %{libname}
libdvbpsi is a simple library designed for decoding and generating
MPEG TS and DVB PSI tables. Current features: * Program Association Table
(PAT), decoder and generator.

%package devel
Summary:        Development headers and libraries for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
libdvbpsi is a simple library designed for decoding and generating
MPEG TS and DVB PSI tables. Current features: * Program Association Table
(PAT), decoder and generator.

%prep
%setup -q

%build
%configure\
	--disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr (-, root, root)
%{_libdir}/libdvbpsi.so.*

%files devel
%defattr (-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/libdvbpsi.so
%{_includedir}/dvbpsi
%{_libdir}/pkgconfig/libdvbpsi.pc

%changelog
