#
# spec file for package python-csv23
#
# Copyright (c) 2023 SUSE LLC
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
%bcond_without python2
%{?sle15_python_module_pythons}
Name:           python-csv23
Version:        0.3.4
Release:        0
License:        MIT
Summary:        Python 2/3 unicode CSV compatibility layer
URL:            https://github.com/xflr6/csv23
Group:          Development/Languages/Python
# Only ZIP archive on PyPI
Source:         https://files.pythonhosted.org/packages/source/c/csv23/csv23-%{version}.zip
BuildRequires:  %{python_module pytest >= 4.6}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python2-mock
%endif
%ifpython2
Requires:       python-mock
%endif
%python_subpackages

%description
Python 2/3 unicode CSV compatibility layer

%prep
%setup -q -n csv23-%{version}
sed -i -e '/--cov/ d' -e '/mock_use_standalone_module/ d' setup.cfg
dos2unix CHANGES.rst README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitelib}/csv23
%{python_sitelib}/csv23-%{version}*-info

%changelog
