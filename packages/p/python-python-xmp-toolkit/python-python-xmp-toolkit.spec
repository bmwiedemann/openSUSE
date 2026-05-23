#
# spec file for package python-python-xmp-toolkit
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


%{?sle15_python_module_pythons}
Name:           python-python-xmp-toolkit
Version:        2.0.2
Release:        0
Summary:        Python XMP Toolkit for working with metadata
License:        BSD-3-Clause
URL:            https://github.com/python-xmp-toolkit/python-xmp-toolkit
Source:         https://files.pythonhosted.org/packages/source/p/python-xmp-toolkit/python-xmp-toolkit-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on one commit of gh#python-xmp-toolkit/python-xmp-toolkit#96
Patch0:         support-python-313.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytz
BuildArch:      noarch
%python_subpackages

%description
A Python XMP Toolkit for working with metadata.

%prep
%autosetup -p1 -n python-xmp-toolkit-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not (test_single_namspace_single_path_leaf_names or test_exempi or test_files)'

%files %{python_files}
%doc AUTHORS CHANGELOG README.rst
%license LICENSE
%{python_sitelib}/libxmp
%{python_sitelib}/python_xmp_toolkit-%{version}.dist-info

%changelog
