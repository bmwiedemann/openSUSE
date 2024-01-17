#
# spec file for package libdvbpsi-0
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libdvbpsi-0
%define _name libdvbpsi
Version:        0.2.2
Release:        0
Summary:        Library for Decoding and Generating MPEG TS and DVB PSI Tables
License:        LGPL-2.1+
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            http://www.videolan.org/developers/libdvbpsi.html
Source:         http://download.videolan.org/pub/%{_name}/%{version}/%{_name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libdvbpsi is a simple library designed for decoding and generating
   MPEG TS and DVB PSI tables. Current features: * Program
   Association Table (PAT), decoder and generator.

* Program Map Table (PMT), decoder and generator.

* All MPEG 2 descriptors, decoders and generators.

%package -n libdvbpsi7
Summary:        Library for Decoding and Generating MPEG TS and DVB PSI Tables
Group:          System/Libraries

%description -n libdvbpsi7
libdvbpsi is a simple library designed for decoding and generating
   MPEG TS and DVB PSI tables. Current features: * Program
   Association Table (PAT), decoder and generator.

* Program Map Table (PMT), decoder and generator.
* All MPEG 2 descriptors, decoders and generators.

%package devel
Summary:        Library for Decoding and Generation of MPEG TS and DVB PSI Tables
Group:          Development/Libraries/C and C++
Requires:       libdvbpsi7 = %{version}
Provides:       libdvbpsi-devel = %{version}
Conflicts:      libdvbpsi-devel >= 1.0.0

%description devel
libdvbpsi is a simple library designed for decoding and generation of
MPEG TS and DVB PSI tables.

Current features: * Program Association Table (PAT), decoder and
   generator.

* Program Map Table (PMT), decoder and generator.
* All MPEG 2 descriptors, decoders and generators.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure\
	--disable-static
%{__make} %{?_smp_mflags}

%install
%makeinstall
find %{buildroot}%{_libdir} -type f -name "*.la" -delete -print

%clean
%{__rm} -rf %{buildroot}

%post -n libdvbpsi7 -p /sbin/ldconfig

%postun -n libdvbpsi7 -p /sbin/ldconfig

%files -n libdvbpsi7
%defattr (-, root, root)
%{_libdir}/libdvbpsi.so.7
%{_libdir}/libdvbpsi.so.7.*

%files devel
%defattr (-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/libdvbpsi.so
%{_includedir}/dvbpsi
%{_libdir}/pkgconfig/libdvbpsi.pc

%changelog
