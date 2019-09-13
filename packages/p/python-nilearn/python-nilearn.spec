#
# spec file for package python-nilearn
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-nilearn
Version:        0.5.2
Release:        0
License:        BSD-3-Clause
Summary:        Statistical learning tool for neuroimaging
Url:            http://nilearn.github.io
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/n/nilearn/nilearn-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module nibabel >= 2.0.2}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module scikit-learn}
BuildRequires:  %{python_module scipy}
# /SECTION
Requires:       python-nibabel >= 2.0.2
Requires:       python-scikit-learn
Requires:       python-scipy
BuildArch:      noarch

%python_subpackages

%description
Nilearn is a Python module for statistical learning on
NeuroImaging data.

%prep
%setup -q -n nilearn-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
