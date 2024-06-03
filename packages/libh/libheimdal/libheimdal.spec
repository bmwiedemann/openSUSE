#
# spec file for package libheimdal
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


Name:           libheimdal
Version:        7.8.0
Release:        0
Summary:        The Heimdal implementation of the Kerberos 5 protocol
License:        BSD-3-Clause
Group:          Productivity/Networking/Security
URL:            https://www.h5l.org
# patched source can be created with script heimdal-patch-source.sh:
# ./heimdal-patch-source.sh heimdal-%{version}.tar.gz
Source0:        heimdal-%{version}-patched.tar.bz2
Source2:        heimdal-patch-source.sh
Patch0:         heimdal-patched.diff
# PATCH-FIX-UPSTREAM bmwiedemann -- make build reproducible (boo#1047218)
Patch1:         reproducible.patch
# PATCH-FIX-UPSTREAM https://www.openwall.com/lists/oss-security/2023/02/08/1
Patch2:         heimdal-CVE-2022-45142.patch
Patch3:         https://patch-diff.githubusercontent.com/raw/heimdal/heimdal/pull/1229.patch
BuildRequires:  automake >= 1.11
BuildRequires:  bison
BuildRequires:  db-devel >= 4.8
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  texinfo
BuildRequires:  perl(JSON)
BuildRequires:  pkgconfig(com_err)
BuildRequires:  pkgconfig(ncurses) >= 5.3
BuildRequires:  pkgconfig(sqlite3)

%description
Heimdal is an implementation of Kerberos 5 (and some more stuff) largely written
in Sweden (which was important when we started writing it, less so now).
It is freely available under a three clause BSD style license.

Other free implementations include the one from MIT, and Shishi.
Also Microsoft Windows and Sun's Java come with implementations of Kerberos.

This package only provides libraries and devel files (binaries have been removed),
libraries are required by 64-bit package of ICAClient version 13.2.

%package -n libasn1-8
Summary:        ASN.1 implementation from Heimdal Kerberos
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libasn1-8
This package contains the ASN.1 parser required for Heimdal.

%package -n libgssapi3
Summary:        GSSAPI implementation from Heimdal Kerberos
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libgssapi3
GSSAPI implementation from Heimdal.

%package -n libhcrypto4
Summary:        Cryptographic library from Heimdal Kerberos
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libhcrypto4
This package contains the cryptographic library required for Heimdal.

%package -n libhdb9
Summary:        Heimdal database backend library
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libhdb9
libhdb provides the backend support for Heimdal kdc and kadmind. Its
here where plugins for diffrent database engines can be pluged in and
extend support for here Heimdal get the principal and policy data
from.

Example of Heimdal backend are: Berkeley DB (BDB), NDB, LDAP.

%package -n libheimbase1
Summary:        Base library for Heimdal Kerberos
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libheimbase1
This package contains the base library for Heimdal Kerberos.

%package -n libheimedit0
Summary:        libedit fork of the Heimdal Kerberos project
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libheimedit0
libedit is a command line editing and history library. It is
designed to be used by interactive programs that allow the user
to type commands at a terminal prompt.

%package -n libheimntlm0
Summary:        NTLM implementation from Heimdal Kerberos
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libheimntlm0
This package contains the NTLM support library from and for Heimdal Kerberos.

%package -n libhx509-5
Summary:        X.509 implementation from Heimdal Kerberos
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libhx509-5
This package contains the X.509 support library from and for Heimdal Kerberos.

%package -n libkadm5clnt7
Summary:        Client library for Heimdal Kerberos
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libkadm5clnt7
This package contains the client library for Heimdal's kadmin program.

%package -n libkadm5srv8
Summary:        Server library for Heimdal Kerberos
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libkadm5srv8
This package contains the server library for Heimdal's kadmin program.

%package -n libkafs0
Summary:        KAFS support for Heimdal Kerberos
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libkafs0
This package contains the library for supporting the in-kernel Andrew File System.

%package -n libkdc2
Summary:        Key Distribution Center library for Heimdal Kerberos
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libkdc2
This package contains the KDC support library.

%package -n libkrb5-26
Summary:        Kerberos 5 API for Heimdal Kerberos
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libkrb5-26
This package contains the Kerberos 5 library.

%package -n libotp0
Summary:        One Time Password library for Heimdal Kerberos
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libotp0
This package contains the library for One Time Password support.

%package -n libroken18
Summary:        OS abstraction library for Heimdal Kerberos
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libroken18
This package contains a library that wraps or adds utility functions
missing from certain operating systems.

%package -n libsl0
Summary:        Implementation of a suggestion lister
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libsl0
This package contains a library that suggests commands in a "did you
mean" fashion.

%package -n libwind0
Summary:        An implementation of RFC 3454 (stringprep)
Group:          System/Libraries
Conflicts:      libheimdal < %{version}-%{release}

%description -n libwind0
This package contains an implementation of the stringprep library.

%package devel
Summary:        The Heimdal implementation of the Kerberos 5 protocol
Group:          Development/Libraries/C and C++
Requires:       db-devel >= 4.8
Requires:       glibc-devel
Requires:       libasn1-8 = %{version}-%{release}
Requires:       libgssapi3 = %{version}-%{release}
Requires:       libhcrypto4 = %{version}-%{release}
Requires:       libhdb9 = %{version}-%{release}
Requires:       libheimbase1 = %{version}-%{release}
Requires:       libheimedit0 = %{version}-%{release}
Requires:       libheimntlm0 = %{version}-%{release}
Requires:       libhx509-5 = %{version}-%{release}
Requires:       libkadm5clnt7 = %{version}-%{release}
Requires:       libkadm5srv8 = %{version}-%{release}
Requires:       libkafs0 = %{version}-%{release}
Requires:       libkdc2 = %{version}-%{release}
Requires:       libkrb5-26 = %{version}-%{release}
Requires:       libotp0 = %{version}-%{release}
Requires:       libroken18 = %{version}-%{release}
Requires:       libsl0 = %{version}-%{release}
Requires:       libwind0 = %{version}-%{release}
Requires:       pkgconfig(com_err)
Requires:       pkgconfig(ncurses) >= 5.3
Requires:       pkgconfig(sqlite3)
Conflicts:      krb5-devel
Conflicts:      krb5-mini-devel
Provides:       libheimdal = %{version}-%{release}
Obsoletes:      libheimdal < %{version}-%{release}

%description devel
Heimdal is an implementation of Kerberos 5 (and some more stuff) largely written
in Sweden (which was important when we started writing it, less so now).
It is freely available under a three clause BSD style license.

Other free implementations include the one from MIT, and Shishi.
Also Microsoft Windows and Sun's Java come with implementations of Kerberos.

This package only provides libraries and devel files (binaries have been removed),
libraries are required by 64-bit package of ICAClient version 13.2.

%prep
%autosetup -p1 -n heimdal-%{version}

%build
export SOURCE_HOST=OBS # for reproducible builds (boo#1084909)
autoreconf -fi
%configure \
  --with-sqlite3=%{_prefix}
%make_build

%install
%make_install

rm -rf %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig -n libasn1-8
%postun -p /sbin/ldconfig -n libasn1-8
%post -p /sbin/ldconfig -n libgssapi3
%postun -p /sbin/ldconfig -n libgssapi3
%post -p /sbin/ldconfig -n libhcrypto4
%postun -p /sbin/ldconfig -n libhcrypto4
%post -p /sbin/ldconfig -n libhdb9
%postun -p /sbin/ldconfig -n libhdb9
%post -p /sbin/ldconfig -n libheimbase1
%postun -p /sbin/ldconfig -n libheimbase1
%post -p /sbin/ldconfig -n libheimedit0
%postun -p /sbin/ldconfig -n libheimedit0
%post -p /sbin/ldconfig -n libheimntlm0
%postun -p /sbin/ldconfig -n libheimntlm0
%post -p /sbin/ldconfig -n libhx509-5
%postun -p /sbin/ldconfig -n libhx509-5
%post -p /sbin/ldconfig -n libkadm5clnt7
%postun -p /sbin/ldconfig -n libkadm5clnt7
%post -p /sbin/ldconfig -n libkadm5srv8
%postun -p /sbin/ldconfig -n libkadm5srv8
%post -p /sbin/ldconfig -n libkafs0
%postun -p /sbin/ldconfig -n libkafs0
%post -p /sbin/ldconfig -n libkdc2
%postun -p /sbin/ldconfig -n libkdc2
%post -p /sbin/ldconfig -n libkrb5-26
%postun -p /sbin/ldconfig -n libkrb5-26
%post -p /sbin/ldconfig -n libotp0
%postun -p /sbin/ldconfig -n libotp0
%post -p /sbin/ldconfig -n libroken18
%postun -p /sbin/ldconfig -n libroken18
%post -p /sbin/ldconfig -n libsl0
%postun -p /sbin/ldconfig -n libsl0
%post -p /sbin/ldconfig -n libwind0
%postun -p /sbin/ldconfig -n libwind0

%files -n libasn1-8
%{_libdir}/libasn1.so.8*

%files -n libgssapi3
%{_libdir}/libgssapi.so.3*

%files -n libhcrypto4
%{_libdir}/libhcrypto.so.4*

%files -n libhdb9
%{_libdir}/libhdb.so.9*

%files -n libheimbase1
%{_libdir}/libheimbase.so.1*

%files -n libheimedit0
%{_libdir}/libheimedit.so.0*

%files -n libheimntlm0
%{_libdir}/libheimntlm.so.0*

%files -n libhx509-5
%{_libdir}/libhx509.so.5*

%files -n libkadm5clnt7
%{_libdir}/libkadm5clnt.so.7*

%files -n libkadm5srv8
%{_libdir}/libkadm5srv.so.8*

%files -n libkafs0
%{_libdir}/libkafs.so.0*

%files -n libkdc2
%{_libdir}/libkdc.so.2*

%files -n libkrb5-26
%{_libdir}/libkrb5.so.26*

%files -n libotp0
%{_libdir}/libotp.so.0*

%files -n libroken18
%{_libdir}/libroken.so.18*

%files -n libsl0
%{_libdir}/libsl.so.0*

%files -n libwind0
%{_libdir}/libwind.so.0*

%files devel
%license LICENSE
%doc NEWS README TODO
%{_includedir}/*.h
%dir %{_includedir}/gssapi
%{_includedir}/gssapi/*.h
%dir %{_includedir}/hcrypto
%{_includedir}/hcrypto/*.h
%dir %{_includedir}/kadm5
%{_includedir}/kadm5/*.h
%dir %{_includedir}/krb5
%{_includedir}/krb5/*.h
%dir %{_includedir}/roken
%{_includedir}/roken/*.h
%{_libdir}/*.so
%{_infodir}/*.info%{?ext_info}

%changelog
