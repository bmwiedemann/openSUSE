#
# spec file for package libgsasl
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libgsasl
Version:        1.8.0
Release:        0
Source:         ftp://ftp.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz
Summary:        Implementation of the SASL framework and a few common SASL mechanisms
License:        LGPL-2.1+ and GPL-3.0+
Group:          Development/Libraries/C and C++
Url:            http://www.gnu.org/software/gsasl/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  krb5-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libidn-devel
BuildRequires:  libntlm-devel
BuildRequires:  pkgconfig

%description
GNU SASL is an implementation of the Simple Authentication and
Security Layer framework and a few common SASL mechanisms. SASL is
used by network servers (e.g., IMAP, SMTP) to request authentication
from clients, and in clients to authenticate against servers. 

%package -n libgsasl7
Summary:        Implementation of the SASL framework and a few common SASL mechanisms
Group:          Development/Libraries/C and C++
%if 0%{?suse_version}
Recommends:     %{name}-lang
%endif
# Needed to make lang package installable
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
%makeinstall
%find_lang %{name}
rm -f %{buildroot}%{_libdir}/*.la
%if 0%{?fdupes:1}
%fdupes %buildroot
%endif

%check
make check

%post -n libgsasl7 -p /sbin/ldconfig

%postun -n libgsasl7 -p /sbin/ldconfig

%files -n libgsasl7
%defattr (-, root, root)
%doc AUTHORS COPYING.LIB NEWS README THANKS
%{_libdir}/*.so.*

%files devel
%defattr (-, root, root)
%{_includedir}/gsas*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files lang -f %{name}.lang

%changelog
