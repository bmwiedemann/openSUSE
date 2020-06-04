#
# spec file for package sofia-sip
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


%define pkg_major 1.12
%define with_doxygen 0
Name:           sofia-sip
Version:        1.12.11+20110422
Release:        0
Summary:        A RFC3261 compliant SIP User-Agent library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://sofia-sip.sf.net/
Source0:        http://deb.debian.org/debian/pool/main/s/sofia-sip/sofia-sip_%{version}.1.orig.tar.gz
Patch0:         http://deb.debian.org/debian/pool/main/s/sofia-sip/sofia-sip_%{version}.1-2.1.diff.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  openssl-devel
%if 0%{?with_doxygen}
BuildRequires:  doxygen
BuildRequires:  graphviz
%endif
Provides:       %{name}-utils = %{version}-%{release}

%description
Sofia-SIP is an open-source SIP  User-Agent library, compliant with the
IETF RFC3261 specification. It can be used as a building block for SIP
client software for uses such as VoIP, IM, and many other real-time and
person-to-person communication services. The primary target platform
for Sofia-SIP is GNU/Linux. Sofia-SIP is based on a SIP stack developed
at the Nokia Research Center.

This package holds the cli tools what ship with sofia-sip.

%package devel
Summary:        Development files for sofia-sip
Group:          Development/Libraries/C and C++
Requires:       glib2-devel
Requires:       libsofia-sip-ua-glib3 = %{version}
Requires:       libsofia-sip-ua0 = %{version}
Requires:       openssl-devel

%description devel
Sofia-SIP is an open-source SIP  User-Agent library, compliant with the
IETF RFC3261 specification. It can be used as a building block for SIP
client software for uses such as VoIP, IM, and many other real-time and
person-to-person communication services. The primary target platform
for Sofia-SIP is GNU/Linux. Sofia-SIP is based on a SIP stack developed
at the Nokia Research Center.

This package holds the development files.

%package -n libsofia-sip-ua0
#
Summary:        A RFC3261 compliant SIP User-Agent library
Group:          Development/Libraries/C and C++

%description -n libsofia-sip-ua0
Sofia-SIP is an open-source SIP  User-Agent library, compliant with the
IETF RFC3261 specification. It can be used as a building block for SIP
client software for uses such as VoIP, IM, and many other real-time and
person-to-person communication services. The primary target platform
for Sofia-SIP is GNU/Linux. Sofia-SIP is based on a SIP stack developed
at the Nokia Research Center.

This package holds the shared libraries.

%package -n libsofia-sip-ua-glib3
#
Summary:        A RFC3261 compliant SIP User-Agent library  (glib2 bindings)
Group:          Development/Libraries/C and C++
Provides:       %{name}-glib = %{version}-%{release}

%description -n libsofia-sip-ua-glib3
Sofia-SIP is an open-source SIP  User-Agent library, compliant with the
IETF RFC3261 specification. It can be used as a building block for SIP
client software for uses such as VoIP, IM, and many other real-time and
person-to-person communication services. The primary target platform
for Sofia-SIP is GNU/Linux. Sofia-SIP is based on a SIP stack developed
at the Nokia Research Center.

This package holds the glib2 bindings.

%prep
%setup -q -n %{name}-%{version}.1
%patch0 -p1
find . -name "*.awk" -exec sed -i 's|#! /usr/bin/env awk|#!/usr/bin/awk|g' {} \;

%build
%configure --disable-static
%make_build
%if 0%{?with_doxygen}
%make_build doxygen
%endif

%check
#%%make_build check

%install
%make_install
%if 0%{?with_doxygen}
cp -av libsofia-sip-ua/docs/html %{buildroot}%{_docdir}/%{name}/manual
%endif
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}

%post   -n libsofia-sip-ua0      -p /sbin/ldconfig
%postun -n libsofia-sip-ua0      -p /sbin/ldconfig
%post   -n libsofia-sip-ua-glib3 -p /sbin/ldconfig
%postun -n libsofia-sip-ua-glib3 -p /sbin/ldconfig

%files -n libsofia-sip-ua0
%license COPYRIGHTS COPYING
%doc AUTHORS ChangeLog* README* RELEASE
%{_libdir}/libsofia-sip-ua.so.0*

%files
%{_bindir}/addrinfo
%{_bindir}/localinfo
%{_bindir}/sip-date
%{_bindir}/sip-dig
%{_bindir}/sip-options
%{_bindir}/stunc
%{_mandir}/man1/addrinfo.1%{?ext_man}
%{_mandir}/man1/localinfo.1%{?ext_man}
%{_mandir}/man1/sip-date.1%{?ext_man}
%{_mandir}/man1/sip-dig.1%{?ext_man}
%{_mandir}/man1/sip-options.1%{?ext_man}
%{_mandir}/man1/stunc.1%{?ext_man}

%files -n libsofia-sip-ua-glib3
%{_libdir}/libsofia-sip-ua-glib.so.3*

%files devel
%dir %{_includedir}/sofia-sip-%{pkg_major}/
%{_includedir}/sofia-sip-%{pkg_major}/sofia-sip/
%{_includedir}/sofia-sip-%{pkg_major}/sofia-resolv/
%{_libdir}/libsofia-sip-ua.so
%{_libdir}/libsofia-sip-ua-glib.so
%{_libdir}/pkgconfig/sofia-sip-ua-glib.pc
%{_libdir}/pkgconfig/sofia-sip-ua.pc
%{_datadir}/sofia-sip/
%if 0%{?with_doxygen}
%doc %{_docdir}/%{name}/manual
%endif

%changelog
