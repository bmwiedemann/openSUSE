#
# spec file for package python-xmlsec
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-xmlsec
Version:        1.3.6
Release:        0
Summary:        Python bindings for the XML Security Library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mehcode/python-xmlsec
Source:         https://github.com/mehcode/python-xmlsec/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/mehcode/python-xmlsec/pull/91
Patch0:         reproducible.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module lxml >= 3.0}
BuildRequires:  %{python_module lxml-devel}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
# we need at least one backend
BuildRequires:  libxmlsec1-openssl1
BuildRequires:  pkgconfig(xmlsec1)
# we need at least one xmlsec backend on runtime
Recommends:     libxmlsec1-openssl1
Requires:       python-lxml >= 3.0
Requires:       python-pkgconfig
%python_subpackages

%description
Python bindings for the XML Security Library

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# tests currently quite fail see upstream https://github.com/mehcode/python-xmlsec/issues/84
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} py.test-%{$python_bin_suffix} tests/ || :

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
