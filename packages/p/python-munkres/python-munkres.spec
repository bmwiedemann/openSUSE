#
# spec file for package python-munkres
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-munkres
Version:        1.1.2
Release:        0
Summary:        Munkres implementation for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://software.clapper.org/munkres/
Source:         https://github.com/bmc/munkres/archive/release-%{version}.tar.gz
# https://github.com/bmc/munkres/pull/32
Patch0:         python-munkres-remove-nose.patch
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The Munkres module provides an O(n^3) implementation of the Munkres
algorithm (also called the Hungarian algorithm or the Kuhn-Munkres
algorithm). The algorithm models an assignment problem as an NxM cost
matrix, where each element represents the cost of assigning the i'th
worker to the j'th job, and it figures out the least-cost solution,
choosing a single item from each row and column in the matrix, such
that no row and no column are used more than once.

This particular implementation is based on
http://csclab.murraystate.edu/~bob.pilgrim/445/munkres.html.

%prep
%setup -q -n munkres-release-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%{python_expand \
sed -i -e '/^#\/usr\/bin\/env/d' %{buildroot}%{$python_sitelib}/munkres.py
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/munkres.py
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/munkres.py
chmod -x %{buildroot}%{$python_sitelib}/munkres.py
}

%check
%pytest

%files %{python_files}
%license LICENSE.md
%doc CHANGELOG.md README.md
%{python_sitelib}/*

%changelog
