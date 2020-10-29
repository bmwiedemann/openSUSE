#
# spec file for package python-validators
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-validators
Version:        0.18.1
Release:        0
Summary:        Python Data Validation
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kvesteri/validators
Source:         https://files.pythonhosted.org/packages/source/v/validators/validators-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-decorator >= 3.4.0
Requires:       python-six >= 1.4.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module decorator >= 3.4.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.4.0}
# /SECTION
%python_subpackages

%description
Python Data Validation for Humans.

%prep
%setup -q -n validators-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
