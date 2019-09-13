#
# spec file for package SampleICC
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           SampleICC
Url:            http://sourceforge.net/projects/sampleicc/
Version:        1.6.8
Release:        0
Source:         %{name}-%{version}.tar.gz
Summary:        Color Management System
License:        BSD-3-Clause
Group:          Development/Libraries/Other

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  graphviz
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig

%package -n lib%{name}1
Summary:        Colour Management System Libraries
Group:          Development/Libraries/Other

%package      -n lib%{name}-devel
Summary:        Headers, Configuration and static Libs + Documentation
Group:          Development/Libraries/Other
Requires:       lib%{name}1 = %{version}

%description
SampleICC provides an open source platform independent C++ library for reading, writing, manipulating, and applying ICC profiles along with applications that make use of this library.


%description -n lib%{name}1
SampleICC provides an open source platform independent C++ library for reading, writing, manipulating, and applying ICC profiles along with applications that make use of this library.

%description -n lib%{name}-devel
Header files, libraries and documentation for development of Color Management
applications.


%prep
%setup -n %{name}-%{version}

%build
%configure

%install
make %{_smp_mflags}
make DESTDIR=%{buildroot} install
rm  %{buildroot}/%{_libdir}/lib*.la

%post -n lib%{name}1 -p /sbin/ldconfig

%postun -n lib%{name}1 -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/*

%files -n lib%{name}1
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/lib%{name}.so.*
%{_libdir}/libICC_utils.so.*

%files -n lib%{name}-devel
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/lib%{name}.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*
%{_libdir}/lib%{name}.a
%{_libdir}/libICC_utils.a
%{_libdir}/libICC_utils.so

%changelog
