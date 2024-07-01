#
# spec file for package python-flake8-comprehensions
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


Name:           python-flake8-comprehensions
Version:        3.15.0
Release:        0
Summary:        A flake8 plugin to help you write better list/set/dict comprehensions
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/adamchainz/flake8-comprehensions
Source:         https://github.com/adamchainz/flake8-comprehensions/archive/%{version}.tar.gz#/flake8-comprehensions-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM flake8-comprehensions-pr559-notnormalized.patch gh#adamchainz/flake8-comprehensions#559
Patch0:         flake8-comprehensions-pr559-notnormalized.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pytest-flake8-path}
BuildRequires:  %{python_module pytest-randomly}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A flake8 plugin that helps you write better list/set/dict comprehensions.

%prep
%autosetup -p1 -n flake8-comprehensions-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest %{?jobs: -n %jobs}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/flake8_comprehensions
%{python_sitelib}/flake8_comprehensions-%{version}.dist-info

%changelog
