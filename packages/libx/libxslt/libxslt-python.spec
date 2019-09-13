#
# spec file for package libxslt-python
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


%define libname libxslt1
Name:           libxslt-python
Version:        1.1.33
Release:        0
Summary:        Python Bindings for libxslt
License:        MIT
Group:          Development/Libraries/Python
URL:            http://xmlsoft.org/XSLT/
Source0:        ftp://xmlsoft.org/libxslt/libxslt-%{version}.tar.gz
Source1:        ftp://xmlsoft.org/libxslt/libxslt-%{version}.tar.gz.asc
Source2:        libxslt.keyring
Patch0:         libxslt-1.1.24-linkflags.patch
# pbleser: don't build the doc subdir as it's broken and we don't install
# it anyway; neither build the xsltproc subdir (not packaged here, faster)
Patch1:         libxslt-do_not_build_doc_nor_xsltproc.patch
Patch2:         libxslt-random-seed.patch
# PATCH-FIX-UPSTREAM bsc#1132160 CVE-2019-11068 Fix security framework bypass
Patch4:         libxslt-CVE-2019-11068.patch
# PATCH-FIX-UPSTREAM bsc#1140095 CVE-2019-13117 Fix uninitialized read of xsl:number token     
Patch5:         libxslt-CVE-2019-13117.patch
# PATCH-FIX-UPSTREAM bsc#1140101 CVE-2019-13118 Fix uninitialized read with UTF-8 grouping chars
Patch6:         libxslt-CVE-2019-13118.patch
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-tools
BuildRequires:  python-devel
BuildRequires:  python-libxml2
BuildRequires:  python-xml
#!BuildIgnore:  python
Requires:       %{libname} = %{version}

%description
The libxslt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libxslt library to apply XSLT transformations.

This library allows parsing stylesheets. It uses the libxml2-python to
load and save XML and HTML files. Direct access to XPath and the XSLT
transformation context are possible. Thus it is possible to extend the
XSLT language with XPath functions written in Python.

%prep
%setup -q -n libxslt-%{version}
%patch0
%patch1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
autoreconf -fvi
%configure \
  --with-python=python \
  --disable-static \
  --disable-silent-rules
make %{?_smp_mflags} PYTHON_SITE_PACKAGES=%{py_sitedir} pythondir=%{py_sitedir}

%install
make install PYTHON_SITE_PACKAGES=%{py_sitedir} pythondir=%{py_sitedir} DESTDIR=%{buildroot}
# Unwanted doc stuff
rm -fr %{buildroot}%{_datadir}/doc
# #223696
find %{buildroot} -type f -name "*.la" -delete -print

# Stuff we won't package
rm -rf %{buildroot}/%{_bindir}/* %{buildroot}/%{_libdir}/lib** %{buildroot}/%{_includedir}/*
rm -rf %{buildroot}/%{_mandir}/* %{buildroot}/%{_libdir}/pkgconfig/*
rm -rf %{buildroot}/%{_libdir}/xsltConf.sh %{buildroot}/%{_datadir}/aclocal/libxslt.m4

%check
make %{?_smp_mflags} tests -C python

%files
%{py_sitedir}/*
%doc python/libxslt-python-api.xml

%changelog
