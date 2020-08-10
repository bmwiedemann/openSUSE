#
# spec file for package python-pytest-describe
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
Name:           python-pytest-describe
Version:        1.0.0
Release:        0
Summary:        Describe-style plugin for pytest
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pytest-dev/pytest-describe
Source:         https://files.pythonhosted.org/packages/source/p/pytest-describe/pytest-describe-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 2.6.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 2.6.0}
# /SECTION
%python_subpackages

%description
Describe-style plugin for pytest.

%prep
%setup -q -n pytest-describe-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
