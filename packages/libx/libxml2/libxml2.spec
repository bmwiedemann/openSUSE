#
# spec file for package libxml2
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# Define "python" as a package in _multibuild file
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "python"
%global pprefix python-
%define oldpython python
%bcond_without python
%bcond_without python2
%else
%global pprefix %{nil}
%bcond_with python
%endif
%define bname libxml2
%define lname libxml2-2
Name:           %{pprefix}%{bname}
Version:        2.9.10
Release:        0
%if !%{with python}
Summary:        A Library to Manipulate XML Files
License:        MIT
%else
Summary:        Python  Bindings for libxml2
License:        MIT
%endif
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
# PATCH-FIX-UPSTREAM bsc#1157450 This commit breaks perl-XML-LibXSLT
Patch4:         libxml2-xmlFreeNodeList-recursive.patch
# PATCH-FIX-UPSTREAM bsc#1161517 CVE-2020-7595 Infinite loop in xmlStringLenDecodeEntities
Patch5:         libxml2-CVE-2020-7595.patch
# PATCH-FIX-UPSTREAM bsc#1159928 CVE-2019-19956 Revert usptream commit
Patch6:         libxml2-CVE-2019-19956.patch
# PATCH-FIX-UPSTREAM bsc#1176179 CVE-2020-24977 xmllint: global-buffer-overflow in xmlEncodeEntitiesInternal
Patch7:         libxml2-CVE-2020-24977.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%if !%{with python}
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
%else
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module xml}
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       %{lname} = %{version}
Provides:       python-libxml2-python = %{version}-%{release}
Obsoletes:      %{bname}-python < %{version}-%{release}
Obsoletes:      python-libxml2-python < %{version}-%{release}
%if "%{python_flavor}" == "python2"
Provides:       %{bname}-python = %{version}-%{release}
Provides:       %{oldpython}-libxml2 = %{version}-%{release}
Obsoletes:      %{oldpython}-libxml2 < %{version}-%{release}
%endif
%endif
%python_subpackages

%description
The XML C library was initially developed for the GNOME project. It is
now used by many programs to load and save extensible data structures
or manipulate any kind of XML files.
%if %{with python}
This package contains a module that permits
applications written in the Python programming language to use the
interface supplied by the libxml2 library to manipulate XML files.

This library allows manipulation of XML files. It includes support for
reading, modifying, and writing XML and HTML files. There is DTD
support that includes parsing and validation even with complex DTDs,
either at parse time or later once the document has been modified.
%endif

%package -n %{lname}
Summary:        A Library to Manipulate XML Files

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
Provides:       %{bname} = %{version}-%{release}
Obsoletes:      %{bname} < %{version}-%{release}

%description tools
This package contains xmllint, a very useful tool proving libxml's power.

%package devel
Summary:        Development files for libxml2, an XML manipulation library
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
Requires:       %{lname} = %{version}
BuildArch:      noarch

%description doc
The XML C library was initially developed for the GNOME project. It is
now used by many programs to load and save extensible data structures
or manipulate any kind of XML files.

%prep
%setup -q -n libxml2-%{version}
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1 -R
%patch5 -p1
%patch6 -p1 -R
%patch7 -p1

%build
%if !%{with python}
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

%make_build BASE_DIR="%{_docdir}" DOC_MODULE="%{bname}"
%else
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
%if !%{with python}
# qemu-arm can't keep up atm, disabling check for arm
%ifnarch %{arm}
%make_build check
%endif
%endif

%if !%{with python}
%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/lib*.so.*
%license COPYING* Copyright
%doc %dir %{_docdir}/%{bname}
%doc %{_docdir}/%{bname}/[ANRCT]*

# the -n %%bname tag is necessary so that python_subpackages does not interfere
%files -n %{bname}-tools
%{_bindir}/xmllint
%{_bindir}/xmlcatalog
%{_mandir}/man1/xmllint.1%{?ext_man}
%{_mandir}/man1/xmlcatalog.1%{?ext_man}

%files -n %{bname}-devel
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

%files -n %{bname}-doc
%{_datadir}/gtk-doc/html/*
%doc %{_docdir}/%{bname}/examples
%doc %{_docdir}/%{bname}/html
# owning these directories prevents gtk-doc <-> libxml2 build loop:
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html

%else
%files %{python_files}
%doc python/TODO
%doc python/libxml2class.txt
%doc doc/*.py
%doc doc/python.html
%pycache_only %{python_sitearch}/__pycache__/*libxml2*
%{python_sitearch}/*libxml2*

%endif

%changelog
