#
# spec file for package python-model-bakery
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-model-bakery
Version:        1.1.1
Release:        0
License:        Apache-2.0
Summary:        Smart object creation facility for Django
Url:            http://github.com/model-bakers/model_bakery
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/m/model-bakery/model_bakery-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module django >= 1.11.0}
BuildRequires:  %{python_module pytest-django}
# /SECTION
BuildRequires:  fdupes
Requires:       python-django >= 1.11.0
BuildArch:      noarch

%python_subpackages

%description
Smart object creation facility for Django.

%prep
%setup -q -n model_bakery-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=.
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
