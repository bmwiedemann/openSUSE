#
# spec file for package libxml2
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


%define base_name  libxml2
%define libname    libxml2-2
%define flavor @BUILD_FLAVOR@%nil
%if "%{flavor}" == "python"
%define dash -
%define buildpython 1
%endif

Name:           libxml2%{?dash}%{flavor}
Version:        2.12.8
Release:        0
License:        MIT
Summary:        A Library to Manipulate XML Files
URL:            https://gitlab.gnome.org/GNOME/libxml2
Source0:        https://download.gnome.org/sources/%{name}/2.12/libxml2-%{version}.tar.xz
Source1:        baselibs.conf
# W3C Conformance tests
Source2:        https://www.w3.org/XML/Test/xmlts20080827.tar.gz

### -- Upstream patches range from 0 to 999 -- ###
# PATCH-FIX-UPSTREAM libxml2-python3-unicode-errors.patch bsc#1064286 mcepl@suse.com
# remove segfault after doc.freeDoc()
Patch0:         libxml2-python3-unicode-errors.patch
# PATCH-FIX-UPSTREAM libxml2-python3-string-null-check.patch bsc#1065270 mgorse@suse.com
# https://gitlab.gnome.org/GNOME/libxml2/-/merge_requests/15
Patch1:         libxml2-python3-string-null-check.patch

#
### -- openSUSE patches range from 1000 to 1999 -- ###
# PATCH-FIX-OPENSUSE
#Patch1000:
#
### -- SUSE patches starts from 2000 -- ###
## TODO -- Is libxml2-make-XPATH_MAX_NODESET_LENGTH-configurable.patch really
## SUSE-specific? If so, shouldn't it be applied only for SLE distributions?
# PATCH-FIX-SUSE bsc#1135123 Added a new configurable variable XPATH_DEFAULT_MAX_NODESET_LENGTH to avoid nodeset limit
Patch2000:      libxml2-make-XPATH_MAX_NODESET_LENGTH-configurable.patch
#
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
%if 0%{?buildpython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xml}
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libxml-2.0)
# TW: generate subpackages for every python3 flavor
%define python_subpackage_only 1
%python_subpackages
%endif

%description
The XML C library was initially developed for the GNOME project. It is
now used by many programs to load and save extensible data structures
or manipulate any kind of XML files.

%package -n %{libname}
Summary:        A Library to Manipulate XML Files

%description -n %{libname}
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
Provides:       %{base_name} = %{version}-%{release}
# Use hardcoded version to avoid unwanted behavior in the future.
Obsoletes:      %{base_name} < 2.9.13

%description tools
This package contains xmllint, a very useful tool proving libxml's power.

%package devel
Summary:        Development files for libxml2, an XML manipulation library
Requires:       %{base_name} = %{version}
Requires:       %{base_name}-tools = %{version}
Requires:       %{libname} = %{version}
Requires:       glibc-devel
Requires:       libxml2 = %{version}
Requires:       readline-devel
Requires:       xz-devel
Requires:       pkgconfig(liblzma)
Requires:       pkgconfig(zlib)

%description devel
The XML C library can load and save extensible data structures
or manipulate any kind of XML files.

This subpackage contains header files for developing
applications that want to make use of libxml.

%package doc
Summary:        Documentation for libxml, an XML manipulation library
Requires:       %{libname} = %{version}
BuildArch:      noarch

%description doc
The XML C library was initially developed for the GNOME project. It is
now used by many programs to load and save extensible data structures
or manipulate any kind of XML files.

%package -n python-libxml2
Summary:        Python  Bindings for %{name}
Requires:       %{libname} = %{version}
Requires:       python-extras
Provides:       %{base_name}-python = %{version}-%{release}
Provides:       python-libxml2-python = %{version}-%{release}
# Use hardcoded version to avoid unwanted behavior in the future.
Obsoletes:      %{base_name}-python < 2.9.13
Obsoletes:      python-libxml2-python < 2.9.13

%description -n python-libxml2
This package contains a module that permits
applications written in the Python programming language to use the
interface supplied by the libxml2 library to manipulate XML files.

This library allows manipulation of XML files. It includes support for
reading, modifying, and writing XML and HTML files. There is DTD
support that includes parsing and validation even with complex DTDs,
either at parse time or later once the document has been modified.

%prep
%autosetup -p1 -n libxml2-%{version}
sed -i '1 s|/usr/bin/env python|/usr/bin/python3|' doc/apibuild.py

%build
%if ! 0%{?buildpython}
# TODO -- Document why are we using the -fno-strict-aliasing extra flag.
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
    --disable-silent-rules \
    --disable-static \
    --docdir=%{_docdir}/%{base_name} \
    --with-html-dir=%{_docdir}/%{base_name}/html \
    --without-python \
    --with-fexceptions \
    --with-history \
    --enable-ipv6 \
    --with-sax1 \
    --with-regexps \
    --with-threads \
    --with-reader \
    --with-ftp \
    --with-http \
    --with-legacy

%make_build BASE_DIR="%{_docdir}" DOC_MODULE="%{base_name}"
%else
%configure --with-python=%{__python3}
pushd python
export PYTHONPATH="."
%pyproject_wheel
popd
%endif

%install
%if ! 0%{?buildpython}
%make_install BASE_DIR="%{_docdir}" DOC_MODULE="%{base_name}"
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p "%{buildroot}/%{_docdir}/%{base_name}"
cp -a NEWS README.md %{buildroot}%{_docdir}/%{base_name}/
ln -s libxml2/libxml %{buildroot}%{_includedir}/libxml
# Remove duplicated file Copyright as not found by fdupes
rm -fr %{buildroot}%{_docdir}/%{base_name}/Copyright
%fdupes %{buildroot}%{_datadir}
%else
pushd python
%pyproject_install
popd
chmod a-x python/tests/*.py
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if ! 0%{?buildpython}
%check
# qemu-arm can't keep up atm, disabling check for arm
%ifnarch %{arm}
tar xzvf %{SOURCE2} # add conformance tests where they are expected
%make_build check
rm -rf xmlconf/ # remove the conformance tests afterwards
%endif

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%{_libdir}/lib*.so.*
%license Copyright
%doc %dir %{_docdir}/%{base_name}
%doc %{_docdir}/%{base_name}/[ANRCT]*

# the -n %%base_name tag is necessary so that python_subpackages does not interfere
%files -n %{base_name}-tools
%{_bindir}/xmllint
%{_bindir}/xmlcatalog
%{_mandir}/man1/xmllint.1%{?ext_man}
%{_mandir}/man1/xmlcatalog.1%{?ext_man}

%files -n %{base_name}-devel
%{_bindir}/xml2-config
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/libxml.m4
%{_includedir}/libxml
%{_includedir}/libxml2
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake
%{_mandir}/man1/xml2-config.1%{?ext_man}

%files -n %{base_name}-doc
%{_datadir}/gtk-doc/html/*
%doc %{_docdir}/%{base_name}/examples
%doc %{_docdir}/%{base_name}/tutorial
%doc %{_docdir}/%{base_name}/*.html
# owning these directories prevents gtk-doc <-> libxml2 build loop:
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html

%else

%files %{python_files libxml2}
%doc python/libxml2class.txt
%doc doc/*.py
%doc python/README
%pycache_only %{python_sitearch}/__pycache__/*libxml2*
%{python_sitearch}/*libxml2*
%endif

%changelog
