#
# spec file for package opensc
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define completionsdir %(pkg-config --variable completionsdir bash-completion)
Name:           opensc
Version:        0.19.0
Release:        0
Summary:        Smart Card Utilities
License:        LGPL-2.1-or-later
Group:          Productivity/Security
URL:            https://github.com/OpenSC/OpenSC/wiki
Source:         https://github.com/OpenSC/OpenSC/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Source2:        %{name}-rpmlintrc
# Register with p11-kit
# https://web.archive.org/web/20111225073733/http://www.opensc-project.org/opensc/ticket/390
Source3:        opensc.module
Patch1:         opensc-0.19.0-rsa-pss.patch
Patch2:         opensc-0.19.0-redundant_logging.patch
Patch3:         opensc-0.19.0-piv_card_matching.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(openssl)
Requires:       pcsc-lite
# There is no more devel package.
Obsoletes:      opensc-devel < %{version}

%description
OpenSC provides a set of utilities to access smart cards. It mainly
focuses on cards that support cryptographic operations. It facilitates
their use in security applications such as mail encryption,
authentication, and digital signature. OpenSC implements the PKCS#11
API. Applications supporting this API, such as Mozilla Firefox and
Thunderbird, can use it. OpenSC implements the PKCS#15 standard and aims
to be compatible with every software that does so, too.

Before purchasing any cards, please read carefully documentation on the
web pageonly some cards are supported. Not only card type matters, but
also card version, card OS version and preloaded applet. Only subset of
possible operations may be supported for your card. Card initialization
may require third party proprietary software.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -fvi
%configure \
  --docdir=%{_docdir}/%{name} \
  --disable-static \
  --enable-doc \
  --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
cp COPYING NEWS README %{buildroot}%{_docdir}/%{name}
# Private library.
rm %{buildroot}%{_libdir}/libopensc.so
install -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pkcs11/modules/opensc.module

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc %dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/COPYING
%doc %{_docdir}/%{name}/NEWS
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/tools.html
%doc %{_docdir}/%{name}/files.html
%doc %{_docdir}/%{name}/opensc.conf
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/opensc
# Note: .la and .so must be in the main package, required by ltdl:
%{_libdir}/*.la
%{_libdir}/*.so*
%dir %{_libdir}/pkcs11
%{_libdir}/pkcs11/*.so
%{_libdir}/pkgconfig/opensc-pkcs11.pc
%{_mandir}/man?/*%{ext_man}
%config %{_sysconfdir}/opensc.conf
%dir %{_sysconfdir}/pkcs11
%config %{_sysconfdir}/pkcs11/modules/
# This is a private library. There is no reason to split it to libopensc* package.
%{_libdir}/libopensc.so.*
%{completionsdir}/*

%changelog
