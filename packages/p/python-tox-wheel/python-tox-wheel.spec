#
# spec file for package python-tox-wheel
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


Name:           python-tox-wheel
Version:        1.0.0
Release:        0
Summary:        A Tox plugin that builds and installs wheels instead of sdist
License:        BSD-2-Clause
URL:            https://github.com/ionelmc/tox-wheel
Source:         https://files.pythonhosted.org/packages/source/t/tox-wheel/tox-wheel-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-tox >= 3.9
Requires:       python-wheel >= 0.33.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tox >= 3.9}
BuildRequires:  %{python_module tox-no-internet}
BuildRequires:  %{python_module wheel >= 0.33.1}
# /SECTION
%python_subpackages

%description
A Tox plugin that builds and installs wheels instead of sdist.

%prep
%setup -q -n tox-wheel-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Testlayout needs old virtualenv AND python2 interpreter to really work -> Disable for now
#%%pytest

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/tox_wheel
%{python_sitelib}/tox_wheel-%{version}.dist-info

%changelog
