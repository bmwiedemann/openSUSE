#
# spec file for package ltxml
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


%define pyltxml PyLTXML-1.3.tar.gz
Name:           ltxml
Version:        1.2.7
Release:        0
Summary:        Integrated Set of XML Tools
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/XML
URL:            https://www.ltg.ed.ac.uk/software/ltxml/
Source0:        ftp://ftp.cogsci.ed.ac.uk/pub/LTXML/ltxml-%{version}.tar.gz
Source1:        ftp://ftp.cogsci.ed.ac.uk/pub/LTXML/PyLTXML-1.3.tar.gz
BuildRequires:  automake
BuildRequires:  zlib-devel
Requires:       python

%description
LT XML is an integrated set of XML tools and a developers' tool kit,
including a C-based API.

The LT XML tool kit includes stand-alone tools for a wide range of
processing of well-formed XML documents, including searching and
extracting, down-translation (for example, report generation,
formatting), tokenizing and sorting.

For special purposes beyond what the pre-constructed tools can achieve,
extending their functionality and/or creating new tools is easy using
the LT XML API. Minimal applications require less than one-half page of
C code to express.

LT XML provides two views of an XML file; one as a flat stream of
markup elements and text; a second as a sequence of tree-structured XML
elements. The two views can be mixed, allowing great flexibility in the
manipulation of XML documents. It also includes a powerful, yet simple,
querying language, which allows the user to quickly and easily select
those parts of an XML document which are of interest.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       ltxml
#Provides:

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%define INSTALL install -m755 -s
%define INSTALL_SCRIPT install -m755
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644

%prep
%setup -q
mkdir pyltxml && cd pyltxml && tar xzf %{SOURCE1}

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
pushd XML
rm config.guess config.sub
cp %{_datadir}/automake-*/config.{sub,guess} .
autoreconf --force --install
popd
mkdir build
cd build
CFLAGS="%{optflags}" \
  ../XML/configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir}\
                   --enable-multi-byte
make %{?_smp_mflags} all CFLAGS="%{optflags}"

%check
cd build
make %{?_smp_mflags} test CFLAGS="%{optflags}"

%install
if [ ! "x" = "x$RPM_BUILD_ROOT" ] ; then
   %{INSTALL_DIR} %{buildroot}
fi
pushd build
make install CFLAGS="%{optflags}" \
             prefix=%{buildroot}%{_prefix} \
             libdir=%{buildroot}%{_libdir} \
             MANDIR=%{buildroot}%{_mandir}
# make install.man
popd
rm *.MAC
strip %{buildroot}%{_bindir}/* || :

%files
%license COPYING
%doc 00*
%doc XML/doc/xmldoc.html
%{_bindir}/*
%{_mandir}/*/*
%{_prefix}/lib/ltxml*

%files devel
%{_includedir}/*
%{_libdir}/lib*.a

%changelog
