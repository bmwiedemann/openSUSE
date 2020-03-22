#
# spec file for package python-pytest-ordering
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
Name:           python-pytest-ordering
Version:        0.6
Release:        0
Summary:        A pytest plugin to run your tests in a specific order
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ftobia/pytest-ordering
Source:         https://github.com/ftobia/pytest-ordering/archive/%{version}.tar.gz#/pytest-ordering-%{version}.tar.gz
Patch0:         pytest-ordering-pr55-registermarks.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A pytest plugin to run your tests in any order that you specify. It
provides custom markers that say when your tests should run in relation
to each other. They can be absolute (i.e. first, or second-to-last) or
relative (i.e. run this test before this other test).

%prep
%setup -q -n pytest-ordering-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pytest_ordering
%{python_sitelib}/pytest_ordering-%{version}-py*.egg-info

%changelog
