#
# spec file for package python-model-bakery
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-model-bakery
Version:        1.20.0
Release:        0
Summary:        Smart object creation facility for Django
License:        Apache-2.0
URL:            https://github.com/model-bakers/model_bakery
Source:         https://github.com/model-bakers/model_bakery/archive/refs/tags/%{version}.tar.gz#/model-bakery-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 3.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 3.2}
BuildRequires:  %{python_module pytest-django}
# /SECTION
%python_subpackages

%description
Smart object creation facility for Django.

%prep
%setup -q -n model_bakery-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=${PWD}
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/model_bakery
%{python_sitelib}/model_bakery-%{version}.dist-info

%changelog
