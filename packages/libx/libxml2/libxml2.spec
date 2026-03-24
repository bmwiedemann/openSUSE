#
# spec file for package libxml2
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define libname    libxml2-16
Name:           libxml2
Version:        2.15.2
Release:        0
Summary:        A Library to Manipulate XML Files
License:        MIT
URL:            https://gitlab.gnome.org/GNOME/libxml2
Source0:        https://download.gnome.org/sources/%{name}/2.15/libxml2-%{version}.tar.xz
Source1:        baselibs.conf
# W3C Conformance tests
Source2:        https://www.w3.org/XML/Test/xmlts20080827.tar.gz
BuildRequires:  fdupes
BuildRequires:  pkgconfig
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(history)
BuildRequires:  pkgconfig(readline)
%else
BuildRequires:  readline-devel
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
Provides:       %{name} = %{version}-%{release}
# Use hardcoded version to avoid unwanted behavior in the future.
Obsoletes:      %{name} < 2.9.13

%description tools
This package contains xmllint, a very useful tool proving libxml's power.

%package devel
Summary:        Development files for libxml2, an XML manipulation library
Requires:       %{libname} = %{version}
Requires:       %{name} = %{version}
Requires:       %{name}-tools = %{version}
Requires:       pkgconfig(zlib)

%description devel
The XML C library can load and save extensible data structures
or manipulate any kind of XML files.

This subpackage contains header files for developing
applications that want to make use of libxml.

%prep
%autosetup -p1 -n libxml2-%{version}

%build
# TODO -- Document why are we using the -fno-strict-aliasing extra flag.
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
    --disable-silent-rules \
    --disable-static \
    --docdir=%{_docdir}/%{base_name} \
    --with-history \
    --with-sax1 \
    --with-regexps \
    --with-threads \
    --with-reader \
    --with-http \
    %{nil}

%make_build BASE_DIR="%{_docdir}" DOC_MODULE="%{name}"

%install
%make_install BASE_DIR="%{_docdir}" DOC_MODULE="%{name}"
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p "%{buildroot}/%{_docdir}/%{name}"
ln -s libxml2/libxml %{buildroot}%{_includedir}/libxml
# Remove duplicated file Copyright as not found by fdupes
rm -fr %{buildroot}%{_docdir}/%{name}/Copyright
%fdupes %{buildroot}%{_datadir}

%check
# qemu-arm can't keep up atm, disabling check for arm
%ifnarch %{arm}
tar xzvf %{SOURCE2} # add conformance tests where they are expected
%make_build check
rm -rf xmlconf/ # remove the conformance tests afterwards
%endif

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license Copyright
%{_libdir}/lib*.so.*

%files tools
%license Copyright
%{_bindir}/xmllint
%{_bindir}/xmlcatalog

%files devel
%license Copyright
%doc NEWS README.md
%{_bindir}/xml2-config
%{_includedir}/libxml
%{_includedir}/libxml2
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake

%changelog
