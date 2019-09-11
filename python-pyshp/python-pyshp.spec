#
# spec file for package python-pyshp
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyshp
Version:        2.1.0
Release:        0
License:        MIT
Summary:        Python library for ESRI Shapefile format
Url:            https://github.com/GeospatialPython/pyshp
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pyshp/pyshp-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec shapefile.py

%files %{python_files}
%doc README.md changelog.txt
%license LICENSE.TXT
%{python_sitelib}/*

%changelog
