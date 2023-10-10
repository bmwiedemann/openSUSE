#
# spec file for package opensc
#
# Copyright (c) 2023 SUSE LLC
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
Version:        0.23.0
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
Patch0:         opensc-gcc11.patch
# PATCH-FIX-UPSTREAM: bsc#1211894, CVE-2023-2977 out of bounds read in pkcs15 cardos_have_verifyrc_package()
Patch1:         opensc-CVE-2023-2977.patch
# PATCH-FIX-UPSTREAM: bsc#1215762 CVE-2023-40660: PIN bypass when card tracks its own login state
Patch2:         opensc-CVE-2023-40660-1of2.patch
Patch3:         opensc-CVE-2023-40660-2of2.patch
# PATCH-FIX-UPSTREAM: bsc#1215763 CVE-2023-4535: out-of-bounds read in MyEID driver handling encryption using symmetric keys
Patch4:         opensc-NULL_pointer_fix.patch
Patch5:         opensc-CVE-2023-4535.patch
# PATCH-FIX-UPSTREAM: bsc#1215761 CVE-2023-40661: multiple memory issues with pkcs15-init (enrollment tool)
Patch6:         opensc-CVE-2023-40661-1of12.patch
Patch7:         opensc-CVE-2023-40661-2of12.patch
Patch8:         opensc-CVE-2023-40661-3of12.patch
Patch9:         opensc-CVE-2023-40661-4of12.patch
Patch10:        opensc-CVE-2023-40661-5of12.patch
Patch11:        opensc-CVE-2023-40661-6of12.patch
Patch12:        opensc-CVE-2023-40661-7of12.patch
Patch13:        opensc-CVE-2023-40661-8of12.patch
Patch14:        opensc-CVE-2023-40661-9of12.patch
Patch15:        opensc-CVE-2023-40661-10of12.patch
Patch16:        opensc-CVE-2023-40661-11of12.patch
Patch17:        opensc-CVE-2023-40661-12of12.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libpcsclite) >= 1.8.22
BuildRequires:  pkgconfig(openssl) >= 1.0.1
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
%autosetup -p1

%build
%configure \
  --docdir=%{_docdir}/%{name} \
  --disable-static \
  --enable-doc \
  --disable-silent-rules
%make_build

%install
%make_install
# Private library.
rm %{buildroot}%{_libdir}/libopensc.so
install -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pkcs11/modules/opensc.module

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS README
%doc %{_docdir}/%{name}/tools.html
%doc %{_docdir}/%{name}/files.html
%doc %{_docdir}/%{name}/opensc.conf
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_sysconfdir}/xdg/autostart/pkcs11-register.desktop
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
