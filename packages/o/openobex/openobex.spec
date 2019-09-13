#
# spec file for package openobex
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           openobex
Version:        1.7.2
Release:        0
Summary:        Object Exchange (OBEX) Protocol
License:        GPL-2.0+ AND LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://openobex.sourceforge.net/
Source:         http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}-Source.tar.gz
Patch1:         openobex-1.7.1-fix_udev_rules.patch
Patch2:         xopen-source.patch
BuildRequires:  bluez-devel
BuildRequires:  cmake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_4
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libusb-1_0-devel
BuildRequires:  libxml2-tools
BuildRequires:  pkgconfig
BuildRequires:  xsltproc

%description
OBEX is a session protocol and can best be described as a binary HTTP
protocol. OBEX is optimized for ad-hoc wireless links and can be used
to exchange all kind of objects, like files, pictures, calendar entries
(vCal), and business cards (vCard).

%package -n libopenobex2
Summary:        Open Source Implementation of the Object Exchange (OBEX) Protocol
License:        GPL-2.0+ AND LGPL-2.1+
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}

%description -n libopenobex2
OBEX is a session protocol and can best be described as a binary HTTP
protocol. OBEX is optimized for ad-hoc wireless links and can be used
to exchange all kind of objects, like files, pictures, calendar entries
(vCal), and business cards (vCard).

%package apps
Summary:        Open Source Implementation of the Object Exchange (OBEX) Protocol
License:        GPL-2.0+ AND LGPL-2.1+
Group:          Productivity/Networking/Web/Utilities

%description apps
Various applications and ools using the Object Exchange (OBEX) Protocol libraries.

%package devel
Summary:        Development package for openobex
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Requires:       libopenobex2 = %{version}

%description devel
Files needed for software development using openobex.

%prep
%setup -q -n openobex-%{version}-Source
%patch1 -p1
%patch2 -p1
# openobex runs some tests with g++
sed -i -e 's:openobex C:openobex C CXX:' CMakeLists.txt
# do not compile and install the udev part
sed -i    '/add_subdirectory.*udev/d' CMakeLists.txt
# doxygen no timestamp
sed -i -e '4 iHTML_TIMESTAMP=NO' doc/Doxyfile.in

%build
%cmake \
	-DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}
make %{?_smp_mflags}
make %{?_smp_mflags} openobex-apps

%install
%cmake_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_docdir}
# don't ship obex_test program, that is for testing purposes only
# and has some problems (multiple buffer overflows etc.)
rm -f %{buildroot}%{_bindir}/obex_test
rm -f %{buildroot}%{_mandir}/man1/obex_test.1*

%post -n libopenobex2 -p /sbin/ldconfig
%postun -n libopenobex2 -p /sbin/ldconfig

%files -n libopenobex2
# NEWS is empty
%doc AUTHORS COPYING COPYING.LIB ChangeLog README
%{_libdir}/libopenobex.so.*

%files apps
%{_bindir}/ircp
%{_bindir}/irobex_palm3
%{_bindir}/irxfer
%{_bindir}/obex_find
%{_bindir}/obex_tcp
%{_mandir}/man1/*

%files devel
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*
%{_includedir}/openobex/
%{_libdir}/libopenobex.so
%{_libdir}/pkgconfig/openobex.pc
%{_libdir}/cmake/OpenObex-%{version}/

%changelog
