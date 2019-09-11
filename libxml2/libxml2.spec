#
# spec file for package libxml2
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


%define lname libxml2-2
Name:           libxml2
Version:        2.9.9
Release:        0
Summary:        A Library to Manipulate XML Files
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xmlsoft.org
Source:         ftp://xmlsoft.org/libxml2/%{name}-%{version}.tar.gz
Source1:        ftp://xmlsoft.org/libxml2/%{name}-%{version}.tar.gz.asc
Source2:        baselibs.conf
Source3:        %{name}.keyring
Patch0:         fix-perl.diff
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)

%description
The XML C library was initially developed for the GNOME project. It is
now used by many programs to load and save extensible data structures
or manipulate any kind of XML files.

%package -n %{lname}
Summary:        A Library to Manipulate XML Files
Group:          System/Libraries

%description -n %{lname}
The XML C library was initially developed for the GNOME project. It is
now used by many programs to load and save extensible data structures
or manipulate any kind of XML files.

This library implements a number of existing standards related to
markup languages, including the XML standard, name spaces in XML, XML
Base, RFC 2396, XPath, XPointer, HTML4, XInclude, SGML catalogs, and
XML catalogs. In most cases, libxml tries to implement the
specification in a rather strict way. To some extent, it provides
support for the following specifications, but does not claim to
implement them: DOM, FTP client, HTTP client, and SAX.

The library also supports RelaxNG. Support for W3C XML Schemas is in
progress.

%package tools
Summary:        Tools using libxml
Group:          Productivity/Text/Utilities
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}

%description tools
This package contains xmllint, a very useful tool proving libxml's power.

%package devel
Summary:        Development files for libxml2, an XML manipulation library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       %{name}-tools = %{version}
Requires:       glibc-devel
Requires:       readline-devel
Requires:       pkgconfig(liblzma)
Requires:       pkgconfig(zlib)

%description devel
The XML C library can load and save extensible data structures
or manipulate any kind of XML files.

This subpackage contains header files for developing
applications that want to make use of libxml.

%package doc
Summary:        Documentation for libxml, an XML manipulation library
Group:          Documentation/HTML
Requires:       %{lname} = %{version}
BuildArch:      noarch

%description doc
The XML C library was initially developed for the GNOME project. It is
now used by many programs to load and save extensible data structures
or manipulate any kind of XML files.

%prep
%setup -q
%patch0

%build
%configure \
    --disable-silent-rules \
    --disable-static \
    --docdir=%{_docdir}/%{name} \
    --with-html-dir=%{_docdir}/%{name}/html \
    --with-fexceptions \
    --with-history \
    --without-python \
    --enable-ipv6 \
    --with-sax1 \
    --with-regexps \
    --with-threads \
    --with-reader \
    --with-http

make %{?_smp_mflags} BASE_DIR="%{_docdir}" DOC_MODULE="%{name}"

%install
%make_install BASE_DIR="%{_docdir}" DOC_MODULE="%{name}"
mkdir -p "%{buildroot}/%{_docdir}/%{name}"
cp -a AUTHORS NEWS README TODO* %{buildroot}%{_docdir}/%{name}/
ln -s libxml2/libxml %{buildroot}%{_includedir}/libxml
%fdupes %{buildroot}%{_datadir}

%check
# qemu-arm can't keep up atm, disabling check for arm
%ifnarch %{arm}
make %{?_smp_mflags} check
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/lib*.so.*
%license COPYING* Copyright
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/[ANRCT]*

%files tools
%{_bindir}/xmllint
%{_bindir}/xmlcatalog
%{_mandir}/man1/xmllint.1%{?ext_man}
%{_mandir}/man1/xmlcatalog.1%{?ext_man}

%files devel
%{_bindir}/xml2-config
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/libxml.m4
%{_includedir}/libxml
%{_includedir}/libxml2
%{_libdir}/lib*.so
# libxml2.la is needed for the python-libxml2 build. Deleting it breaks build of python-libxml2.
%{_libdir}/libxml2.la
%{_libdir}/*.sh
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake
%{_mandir}/man1/xml2-config.1%{?ext_man}
%{_mandir}/man3/libxml.3%{?ext_man}

%files doc
%{_datadir}/gtk-doc/html/*
%doc %{_docdir}/%{name}/examples
%doc %{_docdir}/%{name}/html
# owning these directories prevents gtk-doc <-> libxml2 build loop:
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html

%changelog
