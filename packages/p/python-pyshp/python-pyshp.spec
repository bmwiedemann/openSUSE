#
# spec file for package python-pyshp
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-pyshp
Version:        2.1.0
Release:        0
License:        MIT
Summary:        Python library for ESRI Shapefile format
URL:            https://github.com/GeospatialPython/pyshp
Source:         https://files.pythonhosted.org/packages/source/p/pyshp/pyshp-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
PySHP provides Python read/write support for the ESRI Shapefile
geospatial vector data format.

%prep
%setup -q -n pyshp-%{version}
# Fix wrong-file-end-of-line-encoding
sed -i 's/\r$//' changelog.txt

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec shapefile.py

%files %{python_files}
%doc README.md changelog.txt
%license LICENSE.TXT
%{python_sitelib}/shapefile.py
%pycache_only %{python_sitelib}/__pycache__/shapefile*.pyc
%{python_sitelib}/pyshp-%{version}.dist-info

%changelog
