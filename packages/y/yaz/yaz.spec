#
# spec file for package yaz
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define         libname libyaz5
Name:           yaz
Version:        5.8.1
Release:        0
Summary:        Z39.50 protocol server and client
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://www.indexdata.dk/yaz/
Source:         %{name}-%{version}.tar.gz
Source2:        baselibs.conf
# PATCH-FIX-UPSTREAM initialize variables properly
Patch0:         yaz-5.1.2-codecleanup.diff
# PATCH-FIX-UPSTREAM initialize variables properly
Patch1:         yaz-4.1.7-client.diff
# PATCH-FIX-UPSTREAM add needed ctype header
Patch2:         yaz-4.2.47-implicit_definitions.patch
BuildRequires:  libicu-devel
BuildRequires:  libpcap-devel
BuildRequires:  libxslt-devel
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  readline-devel
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(libxml-2.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains both a test-server and clients (normal & ssl) for
the ANSI/NISO Z39.50 protocol for Information Retrieval.  SRW and SRU
clients and servers are also supported.

%package doc
Summary:        Documentation for %{name} (Z39.50 Library)
Group:          Documentation/HTML
%if 0%{?suse_version} >= 1140
BuildArch:      noarch
%endif

%description doc
YAZ is a C library for developing client and server applications
using the ANSI/NISO Z39.50 protocol for Information Retrieval.

This package contains the documentation.

%package -n %{libname}
Summary:        Z39
Group:          Development/Libraries/C and C++
Provides:       libyaz = %{version}
Obsoletes:      libyaz < %{version}

%description -n %{libname}
YAZ is a C library for developing client and server applications
using the ANSI/NISO Z39.50 protocol for Information Retrieval.

%package -n libyaz-devel
Summary:        Z39
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{name} = %{version}
Requires:       libicu-devel
Requires:       libxslt-devel
Requires:       openssl-devel
Requires:       tcpd-devel

%description -n libyaz-devel
YAZ is a C library for developing client and server applications
using the ANSI/NISO Z39.50 protocol for Information Retrieval.

%prep
%setup -q
%patch0 -p 1
%patch1 -p 1
%patch2 -p 1

%build
#  --with-dsssl=/usr/share/sgml/docbook/dsssl-stylesheets \
#  --with-dtd=/usr/share/sgml/db41xml
%configure --enable-shared \
		   --enable-tcpd \
		   --with-xslt \
           --with-openssl \
           --with-icu \
		   --disable-static \
		   --with-pic
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
# Unwanted doc stuff
rm -fr %{buildroot}%{_datadir}/doc
rm -fr html
mkdir html
cp -a doc/*.html html
# cp doc/*pdf .
ln -sf introduction.html html/index.html
# yaz.pdf
%define DOCFILES README LICENSE NEWS
{
  echo "<html><head><title>%{name} documentation directory</title></head>"
  echo "<body><ul>"
  echo "<li><a href=\"html/index.html\">%{name}</a>, official documentation (local)"
  for f in %{DOCFILES} http://www.indexdata.dk/links/  ; do
    if [ "http:" = "${f%%%%/*}" ]; then
      echo "<li><a href=\"$f\">$f</a>"
      continue
    fi
    [ -f $f ] || continue
    echo "<li><a href=\"$f\">$f</a>"
  done
  echo "</li></body></html>"
} >index.html
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc %{DOCFILES} ChangeLog
%{_bindir}/yaz-client*
%{_bindir}/yaz-iconv
%{_bindir}/yaz-icu
%{_bindir}/yaz-illclient
%{_bindir}/yaz-marcdump
%{_bindir}/yaz-url
%{_bindir}/yaz-ztest*
%{_bindir}/zoomsh
%{_bindir}/yaz-json-parse
%{_mandir}/*/yaz.*
%{_mandir}/*/yaz-illclient.*
%{_mandir}/*/yaz-client.*
%{_mandir}/*/zoomsh.*
%{_mandir}/*/yaz-iconv.*
%{_mandir}/*/yaz-icu.*
%{_mandir}/*/yaz-log.*
%{_mandir}/*/yaz-url.*
%{_mandir}/*/yaz-ztest.*
%{_mandir}/*/yaz-marcdump.*
%{_mandir}/*/yaz-json-parse.*
%{_mandir}/*/bib1-attr.*
%dir %{_datadir}/yaz
%{_datadir}/yaz/etc

%files doc
%defattr(-,root,root)
%doc index.html html

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n libyaz-devel
%defattr(-,root,root)
%{_bindir}/yaz-config
%{_bindir}/yaz-asncomp
%{_includedir}/yaz
%{_libdir}/*.so
%{_datadir}/yaz/z39.50
%{_datadir}/yaz/ill
%{_datadir}/aclocal/yaz.m4
%{_mandir}/man1/yaz-config.*
%{_mandir}/man1/yaz-asncomp.*
%{_libdir}/pkgconfig/yaz.pc

%changelog
