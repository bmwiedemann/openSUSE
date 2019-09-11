#
# spec file for package python-tox-wheel
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
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-tox-wheel
Version:        0.4.2
Release:        0
Summary:        A Tox plugin that builds and installs wheels instead of sdist
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ionelmc/tox-wheel
Source:         https://files.pythonhosted.org/packages/source/t/tox-wheel/tox-wheel-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-tox >= 3.9
Requires:       python-wheel >= 0.31
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module tox >= 3.9}
BuildRequires:  %{python_module tox-no-internet}
BuildRequires:  %{python_module wheel >= 0.31}
# /SECTION
%python_subpackages

%description
A Tox plugin that builds and installs wheels instead of sdist.

%prep
%setup -q -n tox-wheel-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
