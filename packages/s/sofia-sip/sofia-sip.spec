#
# spec file for package sofia-sip
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


Name:           sofia-sip
Version:        1.12.11
Release:        0
%define pkg_major 1.12
#
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define with_doxygen 0
%if 0%{?sles_version} == 9
%define with_glib 0
%else
%define with_glib 1
%endif
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
%if 0%{?with_glib}
BuildRequires:  glib2-devel
%endif
%if 0%{?with_doxygen}
BuildRequires:  doxygen
BuildRequires:  graphviz
%endif
Provides:       %{name}-utils = %{version}-%{release}
#
Url:            http://sofia-sip.sf.net/
Source:         http://prdownloads.sourceforge.net/sofia-sip/sofia-sip-%{version}.tar.gz
#
Summary:        A RFC3261 compliant SIP User-Agent library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++

%description
Sofia-SIP is an open-source SIP  User-Agent library, compliant with the
IETF RFC3261 specification. It can be used as a building block for SIP
client software for uses such as VoIP, IM, and many other real-time and
person-to-person communication services. The primary target platform
for Sofia-SIP is GNU/Linux. Sofia-SIP is based on a SIP stack developed
at the Nokia Research Center.

This package holds the cli tools what ship with sofia-sip.



Authors:
--------
    Pekka Pessi <pekka.pessi -at nokia -dot com>
    Martti Mela <martti.mela -at nokia -dot com>
    Kai Vehmanen <kai.vehmanen -at nokia -dot com>

%package devel
Requires:       libsofia-sip-ua0 = %{version}
%if 0%{?with_glib}
Requires:       glib2-devel
Requires:       libsofia-sip-ua-glib3 = %{version}
%endif
Requires:       openssl-devel
#
Summary:        Development files for sofia-sip
Group:          Development/Libraries/C and C++

%description devel
Sofia-SIP is an open-source SIP  User-Agent library, compliant with the
IETF RFC3261 specification. It can be used as a building block for SIP
client software for uses such as VoIP, IM, and many other real-time and
person-to-person communication services. The primary target platform
for Sofia-SIP is GNU/Linux. Sofia-SIP is based on a SIP stack developed
at the Nokia Research Center.

This package holds the development files.



Authors:
--------
    Pekka Pessi <pekka.pessi -at nokia -dot com>
    Martti Mela <martti.mela -at nokia -dot com>
    Kai Vehmanen <kai.vehmanen -at nokia -dot com>

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



Authors:
--------
    Pekka Pessi <pekka.pessi -at nokia -dot com>
    Martti Mela <martti.mela -at nokia -dot com>
    Kai Vehmanen <kai.vehmanen -at nokia -dot com>

%if 0%{?with_glib}

%package -n libsofia-sip-ua-glib3
Provides:       %{name}-glib = %{version}-%{release}
#
Summary:        A RFC3261 compliant SIP User-Agent library  (glib2 bindings)
Group:          Development/Libraries/C and C++

%description -n libsofia-sip-ua-glib3
Sofia-SIP is an open-source SIP  User-Agent library, compliant with the
IETF RFC3261 specification. It can be used as a building block for SIP
client software for uses such as VoIP, IM, and many other real-time and
person-to-person communication services. The primary target platform
for Sofia-SIP is GNU/Linux. Sofia-SIP is based on a SIP stack developed
at the Nokia Research Center.

This package holds the glib2 bindings.



Authors:
--------
    Pekka Pessi <pekka.pessi -at nokia -dot com>
    Martti Mela <martti.mela -at nokia -dot com>
    Kai Vehmanen <kai.vehmanen -at nokia -dot com>

%endif

%prep
%setup

%build
%configure --disable-static
# TODO: --enable-ntlm --with-rt
# TODO: where to find the needed lib: --with-sigcomp
# TODO: what kernel headers do we need? --enable-sctp
%{__make}
%if 0%{?with_doxygen}
%{__make} doxygen
%endif

%check
#%{__make} check

%install
%makeinstall
%{__install} -d -m 0755 %{buildroot}%{_docdir}/%{name}/
%{__cp} -av AUTHORS ChangeLog* COPYING COPYRIGHTS README* RELEASE TODO %{buildroot}%{_docdir}/%{name}/
%if 0%{?with_doxygen}
%{__cp} -av libsofia-sip-ua/docs/html %{buildroot}%{_docdir}/%{name}/manual
%endif
%{__rm} -vf %{buildroot}%{_libdir}/*.la

%post   -n libsofia-sip-ua0      -p /sbin/ldconfig

%postun -n libsofia-sip-ua0      -p /sbin/ldconfig
%if 0%{?with_glib}

%post   -n libsofia-sip-ua-glib3 -p /sbin/ldconfig

%postun -n libsofia-sip-ua-glib3 -p /sbin/ldconfig
%endif

%clean
%{__rm} -rf %{buildroot}

%files -n libsofia-sip-ua0
%defattr(-,root,root,-)
%{_libdir}/libsofia-sip-ua.so.0*
%dir %{_docdir}/%{name}/
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_docdir}/%{name}/ChangeLog*
%doc %{_docdir}/%{name}/COPYING
%doc %{_docdir}/%{name}/COPYRIGHTS
%doc %{_docdir}/%{name}/README*
%doc %{_docdir}/%{name}/RELEASE
%doc %{_docdir}/%{name}/TODO

%files
%defattr(-,root,root,-)
%{_bindir}/addrinfo
%{_bindir}/localinfo
%{_bindir}/sip-date
%{_bindir}/sip-dig
%{_bindir}/sip-options
%{_bindir}/stunc
%{_mandir}/man1/addrinfo.1*
%{_mandir}/man1/localinfo.1*
%{_mandir}/man1/sip-date.1*
%{_mandir}/man1/sip-dig.1*
%{_mandir}/man1/sip-options.1*
%{_mandir}/man1/stunc.1*
%if 0%{?with_glib}

%files -n libsofia-sip-ua-glib3
%defattr(-,root,root,-)
%{_libdir}/libsofia-sip-ua-glib.so.3*
%endif

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/sofia-sip-%{pkg_major}/
%{_includedir}/sofia-sip-%{pkg_major}/sofia-sip/
%{_includedir}/sofia-sip-%{pkg_major}/sofia-resolv/
%{_libdir}/libsofia-sip-ua.so
%if 0%{?with_glib}
%{_libdir}/libsofia-sip-ua-glib.so
%{_libdir}/pkgconfig/sofia-sip-ua-glib.pc
%endif
%{_libdir}/pkgconfig/sofia-sip-ua.pc
%{_datadir}/sofia-sip/
%if 0%{?with_doxygen}
%doc %{_docdir}/%{name}/manual
%endif

%changelog
