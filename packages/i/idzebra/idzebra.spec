#
# spec file for package idzebra
#
# Copyright (c) 2022 SUSE LLC
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


Name:           idzebra
Version:        2.2.5
Release:        0
Summary:        Fielded Free Text Engine with a Z39.50 Frontend
License:        GPL-2.0-or-later
Group:          Productivity/Databases/Servers
URL:            https://www.indexdata.com/resources/software/zebra/
Source:         http://ftp.indexdata.dk/pub/zebra/idzebra-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(tcl)
BuildRequires:  pkgconfig(yaz)
Requires:       yaz

%description
Zebra is a fielded free text indexing and retrieval engine with a
Z39.50 front-end. You can use any compatible, commercial, or freeware
Z39.50 client to access data stored in Zebra.

%package devel
Summary:        Fielded Free Text Engine with a Z39.50 Frontend
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glibc-devel
Requires:       libyaz-devel

%description devel
Zebra is a fielded free text indexing and retrieval engine with a
Z39.50 front-end. You can use any compatible, commercial, or freeware
Z39.50 client to access data stored in Zebra.

%package doc
Summary:        Documentation for the idzebra Package
Group:          Productivity/Databases/Servers
Requires:       %{name} = %{version}

%description doc
This package contains the documentation for Zebra.  Zebra is a fielded
free text indexing and retrieval engine with a Z39.50 front-end.

%prep
%setup -q

%build
CFLAGS="%{optflags} -fno-strict-aliasing" \
%configure --disable-static --with-pic --with-yaz=pkg
%make_build
for f in examples/marcxml/*.x?l; do
  tr -d '\15' <$f >$f.tmp && mv $f.tmp $f
done

%check
%ifarch ix86
  # 2004-11-17 07:44:55 CET -ke-
  # there are problems with killing zebrasrv reliably
  %make_build check
%endif

%install
%make_install
# pushd doc
# make DESTDIR=%{buildroot} install
# popd
# Unwanted doc stuff
rm -fr %{buildroot}%{_datadir}/doc
#
rm -fr html
mkdir html
#ln -sf zebra.html html/index.html
cp doc/*html html
#cp doc/*.pdf .
%define DOCFILES README.md LICENSE.* NEWS
#*.pdf
{
  echo "<html><head><title>%{name} documentation directory</title></head>"
  echo "<body><ul>"
  echo "<li><a href=\"html/index.html\">%{name}</a>, official documentation (local)"
  for f in %{DOCFILES}  ; do
    if [ "http:" = "${f%%%%/*}" ]; then
      echo "<li><a href=\"$f\">$f</a>"
      continue
    fi
    [ -f $f ] || continue
    echo "<li><a href=\"$f\">$f</a>"
  done
  echo "</li></body></html>"
} >index.html
pushd %{buildroot}
  mkdir -p etc/idzebra usr/share/idzebra
  cp -a usr/share/idzebra*/tab/* etc/idzebra
  rm -fr usr/share/idzebra*/tab
  pushd %{buildroot}%{_datadir}/idzebra
  ln -sf ../../..%{_sysconfdir}/idzebra tab
  popd
popd
rm examples/*/Makefile*
rm -fr %{buildroot}%{_datadir}/idzebra-2.0-examples
find %{buildroot} -type f -name "*.la" -delete -print
find examples -type f -name '*.pl' -exec chmod -x {} \;

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%dir %{_datadir}/idzebra
%{_datadir}/idzebra/tab
%config %{_sysconfdir}/idzebra
%{_libdir}/lib*.so.*
%dir %{_libdir}/idzebra-2.0
%dir %{_libdir}/idzebra-2.0/modules
%{_libdir}/idzebra-2.0/modules/*.so
%{_bindir}/zebrasrv*
%{_bindir}/zebraidx*
%{_bindir}/idzebra*
%{_mandir}/*/*

%files devel
%{_includedir}/*
%{_datadir}/aclocal/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/zebra.pc

%files doc
%doc %{DOCFILES}
%doc index.html html
%doc examples
%doc doc/marc_indexing.xml

%changelog
