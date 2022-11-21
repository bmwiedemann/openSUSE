#
# spec file for package python-fake-useragent
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python2 1
Name:           python-fake-useragent
Version:        1.0.1
Release:        0
License:        Apache-2.0
Summary:        Useragent faker package for Python
URL:            https://github.com/fake-useragent/fake-useragent
Group:          Development/Languages/Python
Source:         https://github.com/fake-useragent/fake-useragent/archive/refs/tags/%{version}.tar.gz#/fake-useragent-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module importlib-resources}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-importlib-resources
BuildArch:      noarch

%python_subpackages

%description
Useragent faker with real world database.

%prep
%setup -q -n fake-useragent-%{version}
rm pytest.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/fake[-_]useragent*/

%changelog
