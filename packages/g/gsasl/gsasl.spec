#
# spec file for package gsasl
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gsasl
Version:        2.2.1
Release:        0
Summary:        Implementation of the SASL framework and a few common SASL mechanisms
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.gnu.org/software/gsasl/
Source:         https://ftp.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz
Source2:        https://ftp.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz.sig
# https://josefsson.org/54265e8c.txt#/libgsasl.keyring
Source3:        %{name}.keyring
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel >= 0.19.8
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(krb5-gssapi)
BuildRequires:  pkgconfig(libgcrypt) >= 1.4.4
BuildRequires:  pkgconfig(libidn)

%description
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms. SASL is
used by network servers (e.g. IMAP, SMTP) to request authentication
from clients, and in clients to authenticate against servers.

%package -n libgsasl18
Summary:        Implementation of the SASL framework and a few common SASL mechanisms
# Needed to make lang package installable
Group:          System/Libraries

%description -n libgsasl18
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms. SASL is
used by network servers (e.g. IMAP, SMTP) to request authentication
from clients, and in clients to authenticate against servers.

%package devel
Summary:        Headers for GNU SASL, an implementation of the SASL framework
Group:          Development/Libraries/C and C++
Requires:       libgsasl18 = %{version}
Requires:       pkgconfig(krb5-gssapi)
Requires:       pkgconfig(libgcrypt)
Requires:       pkgconfig(libidn)
Obsoletes:      libgsasl-devel < %{version}-%{release}
Provides:       libgsasl-devel = %{version}-%{release}

%description devel
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms. SASL is
used by network servers (e.g. IMAP, SMTP) to request authentication
from clients, and in clients to authenticate against servers.

%lang_package

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--disable-ntlm \
	--with-gssapi-impl=mit \
#
%make_build

%install
%make_install
%find_lang %{name}
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post   -n libgsasl18 -p /sbin/ldconfig
%postun -n libgsasl18 -p /sbin/ldconfig

%files
%{_bindir}/gsasl
%{_mandir}/man1/*.1*
%{_infodir}/*.info*

%files -n libgsasl18
%license COPYING*
%{_libdir}/*.so.*

%files devel
%{_includedir}/gsas*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3*
%doc NEWS README

%files lang -f %{name}.lang

%changelog
