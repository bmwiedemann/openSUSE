#
# spec file for package IccXML
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011-2014 Kai-Uwe Behrmann
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


%define         somajor 2
Name:           IccXML
Version:        0.9.8
Release:        0
Summary:        Color Management XML tools
License:        BSD-3-Clause
Group:          Development/Libraries/Other
Url:            http://sourceforge.net/projects/iccxml/
Source:         http://sourceforge.net/projects/iccxml/files/IccXML-Src/IccXML-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libSampleICC-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tools to read convert ICC profiles to and from XML files

%package -n lib%{name}%{somajor}
Summary:        Colour Management Libraries
Group:          Development/Libraries/Other

%description -n lib%{name}%{somajor}
IccLibXML library acts as an extension of SampleICC's IccProfLib.
This extension provides inherited classes for the classes in IccProfLib
that provide additional I/O routines to read and write the classes as
XML files

%package      -n lib%{name}-devel
Summary:        Headers, Configuration and static Libs + Documentation
Group:          Development/Libraries/Other
Requires:       lib%{name}%{somajor} = %{version}

%description -n lib%{name}-devel
Header files, libraries and documentation for development of Color Management
applications.

%prep
%setup -q

%build
%configure \
	--disable-static

%install
make
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n lib%{name}%{somajor} -p /sbin/ldconfig

%postun -n lib%{name}%{somajor} -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/*

%files -n lib%{name}2
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README
%doc XMLSchema/SampleIccRELAX.rng XMLSchema/SampleIccRELAX.rnc
%{_libdir}/lib%{name}.so.%{somajor}*

%files -n lib%{name}-devel
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/lib%{name}.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/iccxml.pc

%changelog
