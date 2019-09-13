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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# Define "python" as a package in _multibuild file
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "python"
%define pysuffix -python
%define oldpython python
%bcond_without python
%else
%define pysuffix %{nil}
%bcond_with python
%endif
%define bname libxml2
%define lname libxml2-2
Name:           %{bname}%{pysuffix}
Version:        2.9.9
Release:        0
Summary:        A Library to Manipulate XML Files
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xmlsoft.org
Source:         ftp://xmlsoft.org/libxml2/%{bname}-%{version}.tar.gz
Source1:        ftp://xmlsoft.org/libxml2/%{bname}-%{version}.tar.gz.asc
Source2:        baselibs.conf
Source3:        libxml2.keyring
Patch0:         fix-perl.diff
Patch1:         libxml2-python3-unicode-errors.patch
# PATCH-FIX-UPSTREAM libxml2-python3-string-null-check.patch bsc#1065270 mgorse@suse.com
# don't return a NULL string for an invalid UTF-8 conversion.
Patch2:         libxml2-python3-string-null-check.patch
# PATCH-FIX-SUSE bsc#1135123 Added a new configurable variable XPATH_DEFAULT_MAX_NODESET_LENGTH to avoid nodeset limit
Patch3:         libxml2-make-XPATH_MAX_NODESET_LENGTH-configurable.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
%if %{with python}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module xml}
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       libxml2-2 = %{version}
%if "%{python_flavor}" == "python2"
Obsoletes:      %{bname}-python < %{version}
Provides:       %{bname}-python = %{version}
Obsoletes:      %{oldpython}-libxml2 < %{version}
Provides:       %{oldpython}-libxml2 = %{version}
%endif
%endif

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
Provides:       %{bname} = %{version}-%{release}
Obsoletes:      %{bname} < %{version}-%{release}

%description tools
This package contains xmllint, a very useful tool proving libxml's power.

%package devel
Summary:        Development files for libxml2, an XML manipulation library
Group:          Development/Libraries/C and C++
Requires:       %{bname}-tools = %{version}
Requires:       %{lname} = %{version}
Requires:       glibc-devel
Requires:       readline-devel
Requires:       xz-devel
Requires:       zlib-devel
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

%package -n python2-libxml2
Summary:        Python 2 Bindings for libxml2
Group:          Development/Libraries/Python
Obsoletes:      libxml2-python
Provides:       python2-libxml2-python
Obsoletes:      python2-libxml2-python

%description -n python2-libxml2
The python2-libxml2 package contains a module that permits
applications written in the Python programming language to use the
interface supplied by the libxml2 library to manipulate XML files.

This library allows manipulation of XML files. It includes support for
reading, modifying, and writing XML and HTML files. There is DTD
support that includes parsing and validation even with complex DTDs,
either at parse time or later once the document has been modified.

%package -n python3-libxml2
Summary:        Python 3 Bindings for libxml2
Group:          Development/Libraries/Python
Obsoletes:      libxml2-python
Provides:       python3-libxml2-python
Obsoletes:      python3-libxml2-python

%description -n python3-libxml2
The python3-libxml2 package contains a module that permits
applications written in the Python programming language to use the
interface supplied by the libxml2 library to manipulate XML files.

This library allows manipulation of XML files. It includes support for
reading, modifying, and writing XML and HTML files. There is DTD
support that includes parsing and validation even with complex DTDs,
either at parse time or later once the document has been modified.

%prep
%setup -q -n libxml2-%{version}
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
    --disable-silent-rules \
    --disable-static \
    --docdir=%{_docdir}/%{bname} \
    --with-html-dir=%{_docdir}/%{bname}/html \
    --without-python \
    --with-fexceptions \
    --with-history \
    --enable-ipv6 \
    --with-sax1 \
    --with-regexps \
    --with-threads \
    --with-reader \
    --with-http

make %{?_smp_mflags} BASE_DIR="%{_docdir}" DOC_MODULE="%{bname}"
%if %{with python}
pushd python
%python_build
popd
%endif

%install
%if !%{with python}
%make_install BASE_DIR="%{_docdir}" DOC_MODULE="%{bname}"
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p "%{buildroot}/%{_docdir}/%{bname}"
cp -a AUTHORS NEWS README TODO* %{buildroot}%{_docdir}/%{bname}/
ln -s libxml2/libxml %{buildroot}%{_includedir}/libxml
# Remove duplicated file Copyright as not found by fdupes
rm -fr %{buildroot}%{_docdir}/%{bname}/Copyright
%fdupes %{buildroot}%{_datadir}
%else
pushd python
%python_install
popd
chmod a-x python/tests/*.py
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%check
# qemu-arm can't keep up atm, disabling check for arm
%ifnarch %{arm}
make %{?_smp_mflags} check
%endif

%if !%{with python}
%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/lib*.so.*
%license COPYING* Copyright
%doc %dir %{_docdir}/%{bname}
%doc %{_docdir}/%{bname}/[ANRCT]*

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
%{_libdir}/*.sh
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake
%{_mandir}/man1/xml2-config.1%{?ext_man}
%{_mandir}/man3/libxml.3%{?ext_man}

%files doc
%{_datadir}/gtk-doc/html/*
%doc %{_docdir}/%{bname}/examples
%doc %{_docdir}/%{bname}/html
# owning these directories prevents gtk-doc <-> libxml2 build loop:
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html

%else
%files -n python2-libxml2
%doc python/TODO
%doc python/libxml2class.txt
%doc doc/*.py
%doc doc/python.html
%{python2_sitearch}/libxml2.py*
%{python2_sitearch}/drv_libxml2.py*
%{python2_sitearch}/libxml2mod*.so
%{python2_sitearch}/*.egg-info

%files -n python3-libxml2
%doc python/TODO
%doc python/libxml2class.txt
%doc doc/*.py
%doc doc/python.html
%{python3_sitearch}/libxml2.py
%{python3_sitearch}/__pycache__/libxml2.*
%{python3_sitearch}/drv_libxml2.py
%{python3_sitearch}/__pycache__/drv_libxml2.*
%{python3_sitearch}/libxml2mod*.so
%{python3_sitearch}/*.egg-info

%endif

%changelog
