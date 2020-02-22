#
# spec file for package libgsasl
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


Name:           libgsasl
Version:        1.8.1
Release:        0
Summary:        Implementation of the SASL framework and a few common SASL mechanisms
License:        LGPL-2.1-or-later AND GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.gnu.org/software/gsasl/
Source0:        ftp://ftp.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  krb5-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libidn-devel
BuildRequires:  libntlm-devel
BuildRequires:  pkgconfig
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif

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

%description devel
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms. SASL is
used by network servers (e.g., IMAP, SMTP) to request authentication
from clients, and in clients to authenticate against servers.

%lang_package

%prep
%setup -q

%build
%configure --disable-static --with-pic
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}
find %{buildroot} -type f -name "*.la" -delete -print
%if 0%{?fdupes:1}
%fdupes %{buildroot}/%{_prefix}
%endif

%check
make check

%post -n libgsasl7 -p /sbin/ldconfig
%postun -n libgsasl7 -p /sbin/ldconfig

%files -n libgsasl7
%license COPYING.LIB
%doc AUTHORS NEWS README THANKS
%{_libdir}/*.so.*

%files devel
%{_includedir}/gsas*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files lang -f %{name}.lang

%changelog
