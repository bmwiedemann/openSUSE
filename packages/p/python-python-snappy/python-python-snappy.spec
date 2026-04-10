#
# spec file for package python-python-snappy
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-python-snappy
Version:        0.7.3
Release:        0
Summary:        Python library for the snappy compression library
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/andrix/python-snappy
Source:         https://files.pythonhosted.org/packages/source/p/python-snappy/python_snappy-%{version}.tar.gz
BuildRequires:  %{python_module cramjam >= 2.6.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cramjam >= 2.6.0
BuildArch:      noarch
%python_subpackages

%description
Python library for the snappy compression library from Google.

%prep
%autosetup -p1 -n python_snappy-%{version}
sed -i -e '/^#!\//, 1d' src/snappy/snappy.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
mkdir tester
cp test_*.py tester/
pushd tester
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -B test_formats.py
}
popd

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%{python_sitelib}/snappy
%{python_sitelib}/python[-_]snappy-%{version}*-info

%changelog
