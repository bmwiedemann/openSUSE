#
# spec file for package python-libxml2-python
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
%define oldpython python
Name:           python-libxml2-python
Version:        2.9.9
Release:        0
Summary:        Python Bindings for libxml2
License:        MIT
Group:          Development/Libraries/Python
Url:            http://xmlsoft.org
Source:         ftp://xmlsoft.org/libxml2/libxml2-%{version}.tar.gz
Patch1:         libxml2-python3-unicode-errors.patch
# PATCH-FIX-UPSTREAM libxml2-python3-string-null-check.patch bsc#1065270 mgorse@suse.com -- don't return a NULL string for an invalid UTF-8 conversion.
Patch2:         libxml2-python3-string-null-check.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module xml}
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       libxml2-2 = %{version}
%ifpython2
Obsoletes:      libxml2-python < %{version}
Provides:       libxml2-python = %{version}
Obsoletes:      %{oldpython}-libxml2 < %{version}
Provides:       %{oldpython}-libxml2 = %{version}
%endif
%python_subpackages

%description
The libxml2-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libxml2 library to manipulate XML files.

This library allows manipulation of XML files. It includes support for
reading, modifying, and writing XML and HTML files. There is DTD
support that includes parsing and validation even with complex DTDs,
either at parse time or later once the document has been modified.

%prep
%setup -q -n libxml2-%{version}
%patch1 -p1
%patch2 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
    --with-fexceptions \
    --with-history \
    --enable-ipv6 \
    --with-sax1 \
    --with-regexps \
    --with-threads \
    --with-reader \
    --with-http

pushd python
%python_build
popd

%install
pushd python
%python_install
popd
chmod a-x python/tests/*.py
# Unwanted doc stuff
rm -fr %{buildroot}%{_datadir}/doc
rm -f python/tests/Makefile*

%files %{python_files}
%doc python/TODO
%doc python/libxml2class.txt
%doc python/tests
%{python_sitearch}/*

%changelog
