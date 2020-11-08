#
# spec file for package python-pytest-responsemock
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
Name:           python-pytest-responsemock
Version:        1.0.1
Release:        0
Summary:        Simplified requests calls mocking for pytest
License:        BSD-3-Clause
URL:            https://github.com/idlesign/pytest-responsemock
Source:         https://files.pythonhosted.org/packages/source/p/pytest-responsemock/pytest-responsemock-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
Requires:       python-responses
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module responses}
# /SECTION
%python_subpackages

%description
Simplified requests calls mocking for pytest.

%prep
%setup -q -n pytest-responsemock-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_bypass requires internet
%pytest -k 'not test_bypass'

%files %{python_files}
%doc AUTHORS CHANGELOG README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
