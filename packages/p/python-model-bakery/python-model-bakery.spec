#
# spec file for package python-model-bakery
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
%define skip_python2 1
Name:           python-model-bakery
Version:        1.9.0
Release:        0
Summary:        Smart object creation facility for Django
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://github.com/model-bakers/model_bakery
Source:         https://files.pythonhosted.org/packages/source/m/model-bakery/model_bakery-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module pytest-django}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Django >= 2.2
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
export PYTHONPATH=${PWD}
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md docs/source/*.rst
%license LICENSE
%{python_sitelib}/model[-_]bakery*/

%changelog
