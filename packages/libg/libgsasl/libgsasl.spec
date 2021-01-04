#
# spec file for package libgsasl
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


Name:           libgsasl
Version:        1.10.0
Release:        0
Summary:        Implementation of the SASL framework and a few common SASL mechanisms
License:        LGPL-2.1-or-later AND GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.gnu.org/software/gsasl/
Source0:        https://ftp.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz.sig
Source2:        https://josefsson.org/54265e8c.txt#/%{name}.keyring
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel >= 0.19.8
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(krb5-gssapi)
BuildRequires:  pkgconfig(libgcrypt) >= 1.4.4
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libntlm) >= 0.3.5

%description
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms. SASL is
used by network servers (e.g., IMAP, SMTP) to request authentication
from clients, and in clients to authenticate against servers.

%package -n libgsasl7
Summary:        Implementation of the SASL framework and a few common SASL mechanisms
# Needed to make lang package installable
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}

%description -n libgsasl7
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms. SASL is
used by network servers (e.g., IMAP, SMTP) to request authentication
from clients, and in clients to authenticate against servers.

%package devel
Summary:        Implementation of the SASL framework and a few common SASL mechanisms
Group:          Development/Libraries/C and C++
Requires:       libgsasl7 = %{version}
Requires:       pkgconfig(krb5-gssapi)
Requires:       pkgconfig(libgcrypt)
Requires:       pkgconfig(libidn)
Requires:       pkgconfig(libntlm)

%description devel
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms. SASL is
used by network servers (e.g., IMAP, SMTP) to request authentication
from clients, and in clients to authenticate against servers.

%lang_package

%prep
%setup -q

%build
%configure \
	--disable-static \
	--with-pic \
	--with-gssapi-impl=mit \
	--enable-gcc-warnings \
#
%make_build

%install
%make_install
%find_lang %{name}
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post -n libgsasl7 -p /sbin/ldconfig
%postun -n libgsasl7 -p /sbin/ldconfig

%files -n libgsasl7
%license COPYING*
%doc AUTHORS NEWS README THANKS
%{_libdir}/*.so.*

%files devel
%license COPYING*
%{_includedir}/gsas*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files lang -f %{name}.lang
%license COPYING*

%changelog
