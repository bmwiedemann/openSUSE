#
# spec file for package python-csv23
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-csv23
Version:        0.3.2
Release:        0
License:        MIT
Summary:        Python 2/3 unicode CSV compatibility layer
Url:            https://github.com/xflr6/csv23
Group:          Development/Languages/Python
# Only ZIP archive on PyPI
Source:         https://files.pythonhosted.org/packages/source/c/csv23/csv23-%{version}.zip
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  dos2unix
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest >= 4.6}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
Python 2/3 unicode CSV compatibility layer

%prep
%setup -q -n csv23-%{version}
sed -i '/--cov/ d' setup.cfg
dos2unix CHANGES.txt README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.txt README.rst
%license LICENSE.txt
%{python_sitelib}/csv23
%{python_sitelib}/csv23-%{version}*-info

%changelog
