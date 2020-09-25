#
# spec file for package libchipcard
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


Name:           libchipcard
Version:        5.1.5
Release:        0
%define _version 5.1.5rc2
Summary:        Library That Allows Easy Access to Smart Cards (Chipcards)
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            http://www.aquamaniac.de/sites/libchipcard/index.php
Source:         %{name}-%{_version}.tar.gz
#Source:        https://www.aquamaniac.de/rdm/attachments/download/229/libchipcard-5.1.5rc2.tar.gz
Source100:      libchipcard-rpmlintrc
Patch0:         libchipcard-buildsrcdoc.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  gwenhywfar-devel
BuildRequires:  gwenhywfar-tools
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libchipcard allows easy access to smart cards. It provides basic access
to memory and processor cards and has special support for German
medical cards, German "Geldkarten," and HBCI (home banking) cards (both
type 0 and type 1). It accesses the readers via CTAPI or PC/SC
interfaces and has successfully been tested with Towitoko, Kobil, and
Reiner-SCT readers.

%package -n libchipcard6
Summary:        Library That Allows Easy Access to Smart Cards (Chipcards)
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libchipcard6
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       gwenhywfar-devel
Requires:       libchipcard6 = %{version}
Requires:       libusb-devel
Requires:       pcsc-lite-devel
Requires:       sysfsutils

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q -n %{name}-%{_version}
%patch0 -p1
# And update clones of include files to prevent clash:
cp -a /usr/include/PCSC/*.h src/PCSC/

%build
%configure\
	--enable-release\
	--enable-full-doc\
	--disable-static\
	--with-pic \
        --with-pcsc-libs=%{_libdir}
make %{?_smp_mflags}
make srcdoc

%install
%makeinstall
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a AUTHORS COPYING ChangeLog NEWS README TODO apidoc %{buildroot}%{_docdir}/%{name}
rm %{buildroot}%{_libdir}/*.la

%fdupes %{buildroot}%{_docdir}/%{name}/apidoc

%clean
rm -rf %{buildroot}

%preun
# Unconditionally stop the service if it exists. Libchipcard 5 uses pcsc now.
[ -x /etc/init.d/chipcardd ] && /etc/init.d/chipcardd stop || true

%post -n libchipcard6 -p /sbin/ldconfig

%postun -n libchipcard6 -p /sbin/ldconfig

%files
%defattr (-, root, root)
%doc %{_docdir}/%{name}
%exclude %{_docdir}/%{name}/apidoc
%{_bindir}/*
%exclude %{_bindir}/*-config
%{_datadir}/chipcard
# Own dirs to fix build.
%dir %{_libdir}/gwenhywfar/
%dir %{_libdir}/gwenhywfar/plugins/
%dir %{_libdir}/gwenhywfar/plugins/*
%{_libdir}/gwenhywfar/plugins/*/ct
%config %{_sysconfdir}/chipcard

%files -n libchipcard6
%defattr (-, root, root)
%{_libdir}/libchipcard.so.6*

%files devel
%defattr (-, root, root)
%doc %{_docdir}/%{name}/apidoc
%{_bindir}/*-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}*.pc
%{_datadir}/aclocal/*.m4
%{_includedir}/*

%changelog
