#
# spec file for package python-pip-api
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
Name:           python-pip-api
Version:        0.0.13
Release:        0
Summary:        The official unofficial pip API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/di/pip-api
Source:         https://files.pythonhosted.org/packages/source/p/pip-api/pip-api-%{version}.tar.gz
Patch0:         unvendor.patch
BuildRequires:  %{python_module packaging >= 16.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging >= 16.1
Requires:       python-pip
BuildArch:      noarch
%python_subpackages

%description
The official unofficial pip API.

%prep
%setup -q -n pip-api-%{version}
%patch0 -p1
rm -Rf ./pip_api/_vendor

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# All the following download stuff using pip thus skip them:
#   test_installed_distributions
#   test_all_the_right_pips
#   test_isolation
%pytest -v -k 'not (test_installed_distributions or test_all_the_right_pips or test_isolation)'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
