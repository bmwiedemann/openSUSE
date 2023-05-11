#
# spec file for package python-inflect
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


%{?sle15_python_module_pythons}
Name:           python-inflect
Version:        6.0.4
Release:        0
Summary:        Methods for working on numbers and nouns
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/inflect
Source0:        https://files.pythonhosted.org/packages/source/i/inflect/inflect-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydantic >= 1.9.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pydantic >= 1.9.1
Requires:       python-toml
BuildArch:      noarch
%python_subpackages

%description
Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words.

%prep
%setup -q -n inflect-%{version}
# sed -i 's/addopts=--doctest-modules --flake8 --black --cov/addopts=--doctest-modules/g' pytest.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
