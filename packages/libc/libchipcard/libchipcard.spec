#
# spec file for package libchipcard
#
# Copyright (c) 2021 SUSE LLC
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
Version:        5.1.6
Release:        0
%define _version 5.1.6
Summary:        Library That Allows Access to Smart Cards (Chipcards)
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            https://www.aquamaniac.de/rdm/projects/libchipcard/
Source:         https://www.aquamaniac.de/rdm/attachments/download/382/libchipcard-5.1.6.tar.gz
Source1:        https://www.aquamaniac.de/rdm/attachments/download/381/libchipcard-5.1.6.tar.gz.asc
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

%description
Libchipcard allows access to smart cards. It provides basic access
to memory and processor cards and has special support for German
medical cards, German "Geldkarten," and HBCI (home banking) cards (both
type 0 and type 1). It accesses the readers via CTAPI or PC/SC
interfaces and has successfully been tested with Towitoko, Kobil, and
Reiner-SCT readers.

%package -n libchipcard6
Summary:        Library That Allows Access to Smart Cards (Chipcards)
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libchipcard6
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package devel
Summary:        Header files for libchipcard, a library for accessing smartcards
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
        --with-pcsc-libs=%{_libdir}
%make_build
make srcdoc

%install
%make_install
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a AUTHORS COPYING ChangeLog NEWS README TODO apidoc %{buildroot}%{_docdir}/%{name}
rm %{buildroot}%{_libdir}/*.la

%fdupes %{buildroot}%{_docdir}/%{name}/apidoc

%preun
# Unconditionally stop the service if it exists. Libchipcard 5 uses pcsc now.
[ -x /etc/init.d/chipcardd ] && /etc/init.d/chipcardd stop || true

%post -n libchipcard6 -p /sbin/ldconfig

%postun -n libchipcard6 -p /sbin/ldconfig

%files
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
%{_libdir}/libchipcard.so.6*

%files devel
%doc %{_docdir}/%{name}/apidoc
%{_bindir}/*-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}*.pc
%{_datadir}/aclocal/*.m4
%{_includedir}/*

%changelog
