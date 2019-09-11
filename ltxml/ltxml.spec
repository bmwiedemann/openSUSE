#
# spec file for package ltxml
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ltxml
BuildRequires:  automake
BuildRequires:  zlib-devel
Summary:        LT XML: An Integrated Set of XML Tools
License:        GPL-2.0+
Group:          Productivity/Publishing/XML
Version:        1.2.7
Release:        0
Requires:       python
#Provides: 
Url:            http://www.ltg.ed.ac.uk/software/ltxml/
Source0:        ftp://ftp.cogsci.ed.ac.uk/pub/LTXML/ltxml-%{version}.tar.gz
%define pyltxml PyLTXML-1.3.tar.gz
Source1:        ftp://ftp.cogsci.ed.ac.uk/pub/LTXML/PyLTXML-1.3.tar.gz
#Patch: 
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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



Authors:
--------
    Richard Tobin <richard@cogsci.ed.ac.uk>

%package devel
Summary:        Include Files and Libraries mandatory for Development
Requires:       ltxml
#Provides: 

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.



Authors:
--------
    Richard Tobin <richard@cogsci.ed.ac.uk>

%define INSTALL install -m755 -s
%define INSTALL_SCRIPT install -m755
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644

%prep
%setup -q
#%setup -n pyltxml -c -a 1 -D -T
mkdir pyltxml && cd pyltxml && tar xzf %{S:1}
# %patch

%build
pushd XML
rm config.guess config.sub
cp /usr/share/automake-*/config.{sub,guess} .
autoreconf --force --install
popd
mkdir build
cd build
CFLAGS="$RPM_OPT_FLAGS" \
  ../XML/configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir}\
                   --enable-multi-byte
make all CFLAGS="$RPM_OPT_FLAGS"

%check
cd build
make test CFLAGS="$RPM_OPT_FLAGS"

%install
if [ ! "x" = "x$RPM_BUILD_ROOT" ] ; then
   rm -fr $RPM_BUILD_ROOT
   %{INSTALL_DIR} $RPM_BUILD_ROOT
fi
pushd build
make install CFLAGS="$RPM_OPT_FLAGS" \
             prefix=$RPM_BUILD_ROOT%{_prefix} \
             libdir=$RPM_BUILD_ROOT%{_libdir} \
             MANDIR=$RPM_BUILD_ROOT%{_mandir}
# make install.man
popd
rm *.MAC
strip $RPM_BUILD_ROOT%{_bindir}/* || :

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING 00*
%doc XML/doc/xmldoc.html
%{_prefix}/bin/*
%{_mandir}/*/*
%{_prefix}/lib/ltxml*
#%{_prefix}/lib/lib*
#%{_libdir}/ltxml*
######%{_libdir}/lib*

%files devel
%defattr(-, root, root)
%{_prefix}/include/*
%{_libdir}/lib*.a

%changelog
