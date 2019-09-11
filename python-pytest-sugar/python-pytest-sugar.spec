#
# spec file for package python-pytest-sugar
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
Name:           python-pytest-sugar
Version:        0.9.2
Release:        0
Summary:        Pretty printer for pytest progress
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Frozenball/pytest-sugar
Source:         https://files.pythonhosted.org/packages/source/p/pytest-sugar/pytest-sugar-%{version}.tar.gz
Patch0:         pytest4.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module termcolor}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest < 5.0
Requires:       python-termcolor
BuildArch:      noarch
%python_subpackages

%description
pytest-sugar is a plugin for py.test that shows failures and errors instantly and shows a progress bar.

%prep
%setup -q -n pytest-sugar-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_item_count_after_pytest_collection_modifyitems -  https://github.com/Frozenball/pytest-sugar/issues/180
# test_doctest - same as above
%pytest -k 'not test_item_count_after_pytest_collection_modifyitems and not test_doctest'

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
