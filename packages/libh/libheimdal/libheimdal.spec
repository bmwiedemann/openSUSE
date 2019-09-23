#
# spec file for package libheimdal
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libheimdal
Summary:        The Heimdal implementation of the Kerberos 5 protocol
License:        BSD-3-Clause
Group:          Productivity/Networking/Security
Version:        7.7.0
Release:        0
Url:            http://www.h5l.org
# patched source can be created with script heimdal-patch-source.sh:
# ./heimdal-patch-source.sh heimdal-%{version}.tar.gz
Source0:        heimdal-%{version}-patched.tar.bz2
Source2:        heimdal-patch-source.sh
Patch0:         heimdal-patched.diff
# PATCH-FIX-UPSTREAM bmwiedemann -- make build reproducible (boo#1047218)
Patch1:         reproducible.patch
%if 0%{?sles_version} == 11
BuildRequires:  libcom_err-devel
BuildRequires:  sqlite3-devel
%else
BuildRequires:  pkgconfig(com_err)
BuildRequires:  pkgconfig(sqlite3)
%endif
%if 0%{suse_version} > 1315
BuildRequires:  pkgconfig(ncurses) >= 5.3
%else
BuildRequires:  ncurses-devel >= 5.3
%endif
BuildRequires:  automake >= 1.11
BuildRequires:  bison
BuildRequires:  db-devel >= 4.8
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  pkg-config
BuildRequires:  readline-devel
BuildRequires:  texinfo
BuildRequires:  perl(JSON)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Heimdal is an implementation of Kerberos 5 (and some more stuff) largely written
in Sweden (which was important when we started writing it, less so now).
It is freely available under a three clause BSD style license.

Other free implementations include the one from MIT, and Shishi.
Also Microsoft Windows and Sun's Java come with implementations of Kerberos.

This package only provides libraries and devel files (binaries have been removed),
libraries are required by 64-bit package of ICAClient version 13.2.

%package devel
Summary:        The Heimdal implementation of the Kerberos 5 protocol
Group:          Development/Libraries/C and C++
Requires:       libheimdal = %{version}
%if 0%{?sles_version} == 11
Requires:       libcom_err-devel
Requires:       sqlite3-devel
%else
Requires:       pkgconfig(com_err)
Requires:       pkgconfig(sqlite3)
%endif
%if 0%{suse_version} > 1315
Requires:       pkgconfig(ncurses) >= 5.3
%else
Requires:       ncurses-devel >= 5.3
%endif
Requires:       db-devel >= 4.8
Requires:       glibc-devel
Conflicts:      krb5-devel
Conflicts:      krb5-mini-devel

%description devel
Heimdal is an implementation of Kerberos 5 (and some more stuff) largely written
in Sweden (which was important when we started writing it, less so now).
It is freely available under a three clause BSD style license.

Other free implementations include the one from MIT, and Shishi.
Also Microsoft Windows and Sun's Java come with implementations of Kerberos.

This package only provides libraries and devel files (binaries have been removed),
libraries are required by 64-bit package of ICAClient version 13.2.

%prep
%setup -q -n heimdal-%{version}
%patch0 -p1
%patch1 -p1

%build
export SOURCE_HOST=OBS # for reproducible builds (boo#1084909)
autoreconf -fi
%configure \
  --with-sqlite3=%{_prefix}
make %{?_smp_mflags}

%install
%make_install

rm -rf %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig
%install_info --info-dir=%{_infodir} %{_infodir}/heimdal.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/hx509.info.gz

%postun -p /sbin/ldconfig

%preun
/sbin/ldconfig
%install_info_delete --info-dir=%{_infodir} %{_infodir}/heimdal.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/hx509.info.gz

%files
%defattr(-,root,root)
%doc LICENSE NEWS README TODO
%{_libdir}/libasn1.so.8*
%{_libdir}/libgssapi.so.3*
%{_libdir}/libhcrypto.so.4*
%{_libdir}/libhdb.so.9*
%{_libdir}/libheimbase.so.1*
%{_libdir}/libheimedit.so.0*
%{_libdir}/libheimntlm.so.0*
%{_libdir}/libhx509.so.5*
%{_libdir}/libkadm5clnt.so.7*
%{_libdir}/libkadm5srv.so.8*
%{_libdir}/libkafs.so.0*
%{_libdir}/libkdc.so.2*
%{_libdir}/libkrb5.so.26*
%{_libdir}/libotp.so.0*
%{_libdir}/libroken.so.18*
%{_libdir}/libsl.so.0*
%{_libdir}/libwind.so.0*
%{_infodir}/*.info.gz

%files devel
%defattr(-,root,root)
%doc LICENSE
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

%changelog
