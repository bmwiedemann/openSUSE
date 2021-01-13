#
# spec file for package python-affine
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-affine
Version:        2.3.0
Release:        0
Summary:        Affine transformation matrices
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/sgillies/affine
Source:         https://files.pythonhosted.org/packages/source/a/affine/affine-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coveralls}
BuildRequires:  %{python_module pydocstyle}
BuildRequires:  %{python_module pytest >= 3.0}
BuildRequires:  %{python_module pytest-cov}
# /SECTION
%python_subpackages

%description
Matrices describing affine transformation of the plane.

%prep
%setup -q -n affine-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.txt CHANGES.txt README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
