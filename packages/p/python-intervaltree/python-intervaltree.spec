#
# spec file for package python-intervaltree
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
Name:           python-intervaltree
Version:        3.0.2
Release:        0
Summary:        Editable interval tree data structure for Python
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/chaimleib/intervaltree
Source:         https://files.pythonhosted.org/packages/source/i/intervaltree/intervaltree-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sortedcontainers}
# /SECTION
Requires:       python-sortedcontainers
BuildArch:      noarch

%python_subpackages

%description
A mutable, self-balancing interval tree for Python 2 and 3. Queries may
be by point, by range overlap, or by range envelopment.

This library was designed to allow tagging text and time intervals,
where the intervals include the lower bound but not the upper bound.

%prep
%setup -q -n intervaltree-%{version}
# Fix non-executable script
sed -i -e '/^#!\//, 1d' intervaltree/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/*

%changelog
